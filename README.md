# Gym Redundant arm

Gym implementation of the redundant arm with N degrees of freedom.

Original implementation by Pontus Loviken can be found at https://github.com/Loviken/MCGB

Forked from https://github.com/GPaolo/redundant-arm, added a setup.py (allowing installation through pip) and easier change in the number of DOF through gym arguments.

**NB**: The number of degrees of freedom can be changed passing `dof` arg to `gym_redarm/envs/arm_env:ArmEnv.__init__()`. Best practice is to pass the arg during environment instantiation with gym: `gym_args = {'dof':100}; env = gym.make('RedundantArm-v0', **gym_args)`
