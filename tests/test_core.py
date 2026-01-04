import random
import numpy as np
import pytest
from lora_math_model import (
  Config, EnvironmentModel, State, LoraMathModel, AreaType, calculate_toa
)

random.seed(1)
np.random.seed(1)

@pytest.mark.asyncio
async def test_lora_simulation():
  env_model = EnvironmentModel(
    name="math-120-meters",
    path_loss_exponent=2.5,
    shadow_sigma_db=3.0,
    sigma_noise_db=2.0,
    distance_m=120,
    hb_m = 1.2,
    hm_m = 1.0,
    area_type=AreaType.SUBURBAN,
    description="Suburban 120 meters"
  )

  lora_sim = LoraMathModel(env_model=env_model)
  lora_config: Config = {
    "SF": 12,
    "FQ": 878,
    "BW": 500.0,
    "CR": 8.0,
    "TP": 20,
    "IH": 0.0,
    "HS": 100.0,
    "PL": 10.0,
    "CL": 80.0,
    "RT": 1.0
  }

  await lora_sim.config_sync(
    1, 
    lora_config
  )

  cfg = await lora_sim.config_get()
  assert cfg == lora_config

  state = await lora_sim.ping(1)
  assert state == {
    'BPS': 31.847,
    'CHC': 1,
    'DELAY': 1,
    'RSSI': -79.096,
    'SNR': 1,
    'TOA': 314,
    'ATT': 1,
    'ETX': 1, 
    'RTOA': 314
  }

@pytest.mark.asyncio
async def test_lora_simulation_v2():
  env_model = EnvironmentModel(
    name="math-120-meters",
    path_loss_exponent=2.5,
    shadow_sigma_db=3.0,
    sigma_noise_db=2.0,
    distance_m=120,
    hb_m = 1.2,
    hm_m = 1.0,
    area_type=AreaType.SUBURBAN,
    description="Suburban 120 meters"
  )

  lora_sim = LoraMathModel(env_model=env_model)
  lora_config: Config = {
    "SF": 12,
    "FQ": 878,
    "BW": 125.0,
    "CR": 8.0,
    "TP": 20,
    "IH": 0.0,
    "HS": 100.0,
    "PL": 10.0,
    "CL": 80.0,
    "RT": 1.0
  }

  await lora_sim.config_sync(
    1, 
    lora_config
  )

  cfg = await lora_sim.config_get()
  assert cfg == lora_config

  state = await lora_sim.ping(1)
  assert state == {
    'BPS': 7.962,
    'CHC': 1,
    'DELAY': 1,
    'RSSI': -74.88,
    'SNR': 1,
    'TOA': 1256,
    'ATT': 1,
    'ETX': 1, 
    'RTOA': 1256
  }

def test_calculate_toa():
  assert calculate_toa(12, 125 * 1000, 10, 8, 10) == 1256.0