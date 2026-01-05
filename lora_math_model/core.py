from .models import Config, State, EnvironmentModel
import logging
from .utils import (
  lora_log, calculate_toa, bytes_per_second, chunks_count,
  compute_rssi, compute_snr, calculate_delay
)
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
    freq = self.config.get('FQ') * 10e6
    sf = self.config.get('SF')
    bw = self.config.get('BW') * 1000
    cr = self.config.get('CR')
    pl = self.config.get('PL')
    ih = self.config.get('IH')
    tx_power_dbm = self.config.get('TP')

    payload_size = 10

    rssi = compute_rssi(
      distance_m=self.env_model.distance_m,
      freq_hz=freq,
      path_loss_exponent=self.env_model.path_loss_exponent,
      shadow_sigma_db=self.env_model.shadow_sigma_db,
      tx_power_dbm=tx_power_dbm
    )
    snr = compute_snr(
      rssi_dbm=rssi,
      bandwidth_hz=bw
    )
    toa = calculate_toa(sf, bw, payload_size, cr, pl)
    delay = calculate_delay(toa)

    state: State = {
      'BPS': bytes_per_second(payload_size, toa),
      'CHC': chunks_count(payload_size, ih, pl),
      'DELAY': delay,
      'RSSI': rssi,
      'SNR': snr,
      'RTOA': toa,
      'TOA': toa,
      'ETX': 1,
      'ATT': 1
    }

    state = { key: round(value, 3) if isinstance(value, (float, int)) else value for key, value in state.items() }

    self.logger.info(lora_log("PING", state))

    return state
