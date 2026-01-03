from .models import EnvironmentModel, AreaType

LORA_SIMULATION_ENVIRONMENTS = {
  "open_field": EnvironmentModel(
    name="open_field",
    path_loss_exponent=2.0,
    shadow_sigma_db=1.0,
    sigma_noise_db=1.0,
    distance_m=100,
    hb_m = 1.2,
    hm_m = 1.0,
    area_type=AreaType.RURAL,
    description="Clear line-of-sight, almost no obstructions."
  ),
  "suburban": EnvironmentModel(
    name="suburban",
    path_loss_exponent=2.5,
    shadow_sigma_db=3.0,
    sigma_noise_db=2.0,
    distance_m=200,
    hb_m = 1.2,
    hm_m = 1.0,
    area_type=AreaType.SUBURBAN,
    description="Light obstacles, trees, small buildings."
  ),
  "urban": EnvironmentModel(
    name="urban",
    path_loss_exponent=2.9,
    shadow_sigma_db=6.0,
    sigma_noise_db=2.5,
    distance_m=100,
    hb_m = 1.2,
    hm_m = 1.0,
    area_type=AreaType.URBAN,
    description="City area with buildings and partial obstructions."
  ),
  "dense_urban": EnvironmentModel(
    name="dense_urban",
    path_loss_exponent=3.5,
    shadow_sigma_db=10.0,
    sigma_noise_db=3,
    distance_m=100,
    hb_m = 1.2,
    hm_m = 1.0,
    area_type=AreaType.LARGE_URBAN,
    description="Dense buildings, non-line-of-sight."
  ),
  "indoor": EnvironmentModel(
    name="indoor",
    path_loss_exponent=4.0,
    shadow_sigma_db=8.0,
    sigma_noise_db=4,
    distance_m=20,
    hb_m = 1.2,
    hm_m = 1.0,
    area_type=AreaType.LARGE_URBAN,
    description="Office or indoor environment with walls."
  ),
  "industrial": EnvironmentModel(
    name="industrial",
    path_loss_exponent=5.0,
    shadow_sigma_db=12.0,
    sigma_noise_db=3.0,
    distance_m=50,
    hb_m = 1.2,
    hm_m = 1.0,
    area_type=AreaType.LARGE_URBAN,
    description="Heavy metal/industrial environment with strong attenuation."
  ),
}
