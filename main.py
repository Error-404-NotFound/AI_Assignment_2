import os
import subprocess

repo_url = "https://github.com/kevin-schumann/VRP-GYM.git"
destination = "./VRP-GYM"

if not os.path.exists(destination):
    subprocess.run(["git", "clone", repo_url, destination], check=True)
else:
    print(f"Repository already exists at {destination}, skipping clone.")


from environment import create_frozen_lake_env
import matplotlib.pyplot as plt
import numpy as np
from utils import *
from search_algo import dfbnb, ida_star, hill_climb, simulated_annealing

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
    print("DFBnb and IDA* executed successfully.")
    
    coords, best_route, best_cost, costs = hill_climb(num_nodes=100, iterations=10000)
    print("Best route:", best_route)
    print("Best cost:", best_cost)
    hill_climb_cost_vs_iterations(costs, "results/hill_climb_costs.png")
    animated_tour_gif(coords, best_route, gif_name="results/hc_tour.gif", title="Hill Climbing Final Tour")
    
    coords, best_route, best_cost, costs = simulated_annealing(num_nodes=100, iterations=10000, initial_temp=100.0, cooling_rate=0.995)
    print("Best route:", best_route)
    print("Best cost:", best_cost)
    simulated_annealing_cost_vs_iterations(costs, "results/simulated_annealing_costs.png")
    animated_tour_gif(coords, best_route, gif_name="results/sa_tour.gif", title="Simulated Annealing Final Tour")
    print("Hill Climbing and Simulated Annealing executed successfully.")