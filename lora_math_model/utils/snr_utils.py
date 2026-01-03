import random
import math
from ..models import AreaType

def compute_noise_floor(bw_hz: float, noise_figure_db: float = 6.0) -> float:
  return -174 + 10 * math.log10(bw_hz) + noise_figure_db

def compute_snr(rssi_dbm: float, bw_hz: float, noise_figure_db: float = 6.0) -> float:
  noise_floor = compute_noise_floor(bw_hz, noise_figure_db)
  return rssi_dbm - noise_floor

def env_noise_floor_125khz(area: AreaType) -> float:
  if area == AreaType.RURAL:
    return -97.0
  if area == AreaType.SUBURBAN:
    return -90.0
  if area == AreaType.URBAN:
    return -85.0
  if area == AreaType.LARGE_URBAN:
    return -82.0
  return -90.0

def env_noise_floor(area: AreaType, bw_hz: float) -> float:
  base_125 = env_noise_floor_125khz(area)
  bw_scale_db = 10 * math.log10(bw_hz / 125_000.0)
  return base_125 + bw_scale_db

def lora_snr_chip_2(
  rssi_dbm: float,
  bw_hz: float,
  area: AreaType,
  sigma_noise_db: float = 1.5,
):
  base_noise = env_noise_floor(area, bw_hz)
  interference_boost = max(0, 20 + rssi_dbm)

  mean_noise = base_noise + interference_boost
  noise = mean_noise + random.gauss(0.0, sigma_noise_db)

  snr = rssi_dbm - noise
  snr = round(snr * 4.0) / 4.0
  return snr
