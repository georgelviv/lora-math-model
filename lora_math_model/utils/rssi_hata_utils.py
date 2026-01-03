import math
import numpy as np
import random
from ..models import AreaType

def hata_mobile_correction(f_mhz: float, hm_m: float, large_city: bool = False) -> float:
  if large_city:
    return 3.2 * (math.log10(11.75 * hm_m))**2 - 4.97
  else:
    return (1.1 * math.log10(f_mhz) - 0.7) * hm_m - (1.56 * math.log10(f_mhz) - 0.8)

def path_loss_hata(
  distance_m: float,
  freq_hz: float,
  hb_m: float = 1.0,
  hm_m: float = 1.0,
  area: AreaType = AreaType.URBAN
) -> float:
  
  large_city = AreaType.LARGE_URBAN == area

  f_mhz = freq_hz / 1e6
  d_km = max(distance_m / 1000.0, 0.001)
  a_hm = hata_mobile_correction(f_mhz, hm_m, large_city)

  pl = (
    46.3
    + 33.9 * math.log10(f_mhz)
    - 13.82 * math.log10(hb_m)
    - a_hm
    + (44.9 - 6.55 * math.log10(hb_m)) * math.log10(d_km)
  )

  if area == AreaType.URBAN or area == AreaType.LARGE_URBAN:
    C = 3 if large_city else 0
    pl += C

  elif area == AreaType.SUBURBAN:
    pl -= 2 * (math.log10(f_mhz / 28))**2 - 5.4

  elif area == AreaType.RURAL:
    pl -= (
      4.78 * (math.log10(f_mhz))**2
      - 18.33 * math.log10(f_mhz)
      + 40.94
    )

  return pl

def shadowing(sigma_db: float) -> float:
  return random.gauss(0, sigma_db)

def rayleigh_fading_db() -> float:
  r = np.random.rayleigh(1.0)
  fading_db = 20 * math.log10(r)
  return fading_db

def compute_rssi_hata(
  distance_m: float,
  freq_hz: float,
  tx_power_dbm: float,
  shadow_sigma_db: float,
  hb_m: float,
  hm_m: float,
  area: AreaType
) -> float:
  pl = path_loss_hata(distance_m, freq_hz, hb_m, hm_m, area)
  sh = shadowing(shadow_sigma_db)
  ff = rayleigh_fading_db()
  rssi = tx_power_dbm - pl + sh + ff

  return rssi

def lora_rssi_hata_chip(
    distance_m: float,
    freq_hz: float,
    tx_power_dbm: float,
    shadow_sigma_db: float,
    hb_m: float,
    hm_m: float,
    area: AreaType,
    sf: float):
  rssi_physical = compute_rssi_hata(
    distance_m, freq_hz,
    tx_power_dbm, shadow_sigma_db,
    hb_m, hm_m, area
  )
  bias = 1.5 + 0.7 * (sf - 7)
  rssi_chip = rssi_physical + bias
  return round(rssi_chip, 3)