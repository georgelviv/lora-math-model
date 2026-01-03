from .models import Config, State, EnvironmentModel
import logging
from .utils import lora_log
from .logger import default_logger
from .environment import LORA_SIMULATION_ENVIRONMENTS

class LoraMathModel():

  def __init__(
      self, logger: logging.Logger = default_logger, 
      env_model: EnvironmentModel = LORA_SIMULATION_ENVIRONMENTS['open_field']
    ):
    self.config: Config = None
    self.logger = logger
    self.env_model = env_model

  async def start(self):
    pass

  async def stop(self):
    pass

  async def config_sync(self, id: int, params: Config) -> bool:
    self.logger.info(lora_log("CONFIG_SYNC", params))
    self.config = params
    return True

  async def config_get(self) -> Config:
    return self.config
  
  async def ping(self, id: int) -> State:
    state: State = {
      'BPS': 1,
      'CHC': 1,
      'DELAY': 1,
      'RSSI': 1,
      'SNR': 1,
      'RTOA': 1,
      'TOA': 1,
      'ETX': 1,
      'ATT': 1
    }

    state = { key: round(value, 3) if isinstance(value, (float, int)) else value for key, value in state.items() }

    self.logger.info(lora_log("PING", state))

    return state
