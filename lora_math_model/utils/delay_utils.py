TOA_COEF_500_CR8 = {
  12: (181.50493096646943, 13.249506903353057),
  11: (84.61341222879685,  7.238658777120316),
  10: (55.24654832347140,  3.97534516765286),
  9:  (25.94871794871795,  2.2051282051282053),
  8:  (11.554240631163708, 1.244575936883629),
  7:  (6.9092702169625255, 0.7090729783037475),
  6:  (2.8579881656804735, 0.41420118343195267),
}

def calculate_toa(
  sf: int,
  bw_hz: float,
  payload_bytes: int,
  cr: int = 8,
  preamble_sym: int = 10,
) -> float:
  if sf not in TOA_COEF_500_CR8:
    raise ValueError(f"SF {sf} not supported in current TOA model")

  base_500, slope_500 = TOA_COEF_500_CR8[sf]

  toa_500 = base_500 + slope_500 * payload_bytes

  bw_scale = 500_000.0 / bw_hz
  toa = toa_500 * bw_scale

  cr_scale = cr / 8.0
  toa *= cr_scale

  tsym_ms = (2**sf) / bw_hz * 1000.0
  toa += (preamble_sym - 10) * tsym_ms

  return toa