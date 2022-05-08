# Created by Giuseppe Paolo 
# Date: 11/09/2020

from gym.envs.registration import register

register(
    id='RedundantArm-v0',
    entry_point='redundant_arm.envs:ArmEnv',
    # timestep_limit=1000,
)
