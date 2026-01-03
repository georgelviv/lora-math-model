from ..models import AreaType
import random

BASE_SNR_BY_BW = {
  125_000: 10.5,
  250_000: 12.0,
  500_000: 7.5,
}

def lora_snr_chip(
    rssi_dbm: float,
    bw_hz: float,
    area: AreaType,
    sigma_noise_db: float = 2.0,
) -> float:
  base = BASE_SNR_BY_BW.get(int(bw_hz), 8.0)

  if area == AreaType.RURAL:
    base += 0.5
  elif area == AreaType.LARGE_URBAN:
    base -= 0.5

  rssi_ref = -75.0
  alpha = 0.10
  mean_snr = base + alpha * (rssi_dbm - rssi_ref)
  snr = random.gauss(mean_snr, sigma_noise_db)
  snr = max(3.5, min(13.0, snr))
  snr = round(snr * 4.0) / 4.0

  return snr
