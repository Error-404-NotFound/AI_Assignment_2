import gymnasium as gym

custom_map = [
    "SHFFFFFFFF",
    "FHHHHFFFFF",
    "FFFHFFHFFF",
    "FHFFFHFFHF",
    "FHFHFHFFFF",
    "FFHFFFHFFF",
    "FFFFHFHFFF",
    "FHHHFHFFHF",
    "FFFHHFHFHF",
    "FFFFHFFFFG"
]

def create_frozen_lake_env(render_mode="rgb_array", is_slippery=False):
    return gym.make("FrozenLake-v1", is_slippery=is_slippery, render_mode=render_mode, desc=custom_map)