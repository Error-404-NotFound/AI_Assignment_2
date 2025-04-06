from environment import create_frozen_lake_env
import matplotlib.pyplot as plt
import numpy as np
from utils import *
from search_algo import dfbnb, ida_star

def run_search_algorithms(env, episodes=5):
    dfbnb_times = []
    ida_times = []

    for i in range(episodes):
        print(f"\nEpisode {i+1}")
        obs, _ = env.reset()
        start_state = obs
        ncols = env.unwrapped.ncol
        nrows = env.unwrapped.nrow
        goal_state = nrows * ncols - 1

        print("Running DFBnB...")
        path_dfbnb, actions_dfbnb, cost_dfbnb, time_dfbnb = dfbnb(env, start_state, goal_state)
        print(f"DFBnB: Time = {time_dfbnb:.6f}s, Cost = {cost_dfbnb}, \nPath = {path_dfbnb}, \nAction = {actions_dfbnb}")
        dfbnb_times.append(time_dfbnb)

        if i == 0 and path_dfbnb:
            save_gif(env, actions_dfbnb, filename="results/dfbnb_frozenlake.gif")

        print("Running IDA*...")
        path_ida, actions_ida, cost_ida, time_ida = ida_star(env, start_state, goal_state)
        print(f"IDA*: Time = {time_ida:.6f}s, Cost = {cost_ida}, \nPath = {path_ida}, \nAction = {actions_ida}")
        ida_times.append(time_ida)

        if i == 0 and path_ida:
            save_gif(env, actions_ida, filename="results/ida_star_frozenlake.gif")

    return dfbnb_times, ida_times

if __name__ == "__main__":
    env = create_frozen_lake_env()
    dfbnb_times, ida_times = run_search_algorithms(env, episodes=5)
    plot_results_dfbnb_ida(dfbnb_times, ida_times)
    plot_average_results(dfbnb_times, ida_times)
    print("All algorithms executed successfully.")