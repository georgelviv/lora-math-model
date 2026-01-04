import math

def compute_snr(
  rssi_dbm: float,
  bandwidth_hz: float,
  noise_figure_db: float = 6.0
) -> float:
  noise_dbm = -174 + 10 * math.log10(bandwidth_hz) + noise_figure_db
  return rssi_dbm - noise_dbm