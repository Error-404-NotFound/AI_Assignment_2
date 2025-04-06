import numpy as np
import matplotlib.pyplot as plt
import imageio
import random
import os
import sys
# Get the absolute path to the VRP-GYM directory
vrp_gym_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'VRP-GYM'))
sys.path.append(vrp_gym_path)

# Now you can import tsp.py
from gym_vrp.envs import TSPEnv

# num_nodes = 100
# iterations = 10000

def total_distance_hc(route, coords):
    return sum(
        np.linalg.norm(coords[route[i]] - coords[route[(i + 1) % len(route)]])
        for i in range(len(route))
    )

def hill_climb(num_nodes=100, iterations=10000):
    print(f"Running Hill Climbing with {num_nodes} nodes and {iterations} iterations.")
    frame_folder = "frames_hc"
    env = TSPEnv(num_nodes=num_nodes, batch_size=1, num_draw=1)
    state = env.reset()[0]  # Get state for a single graph
    coords = state[:, :2]

    def total_distance(route):
        return sum(np.linalg.norm(coords[route[i]] - coords[route[(i + 1) % len(route)]])
                   for i in range(len(route)))

    def run_hill_climb(init_route, iterations=1000):
        current_route = init_route.copy()
        current_cost = total_distance(current_route)
        best_route = current_route.copy()
        best_cost = current_cost
        costs = []
        images = []

        os.makedirs(frame_folder, exist_ok=True)

        for k in range(iterations):
            i, j = np.random.choice(len(current_route), size=2, replace=False)
            new_route = current_route.copy()
            new_route[i], new_route[j] = new_route[j], new_route[i]
            new_cost = total_distance(new_route)

            if new_cost < current_cost:
                current_route = new_route
                current_cost = new_cost
                if new_cost < best_cost:
                    best_route = new_route
                    best_cost = new_cost

            if k % 50 == 0 or k == iterations - 1:
                fig, ax = plt.subplots(figsize=(6, 6))
                tour_coords = coords[best_route + [best_route[0]]]
                ax.plot(tour_coords[:, 0], tour_coords[:, 1], 'o-', color='blue')
                ax.set_title(f"Hill_Climb_Simulation_across_different_iterations \nStep {k}\nCost: {best_cost:.2f}")
                ax.axis("off")
                frame_path = f"{frame_folder}/frame_{k:03d}.png"
                plt.savefig(frame_path)
                images.append(imageio.imread(frame_path))
                plt.close()

            costs.append(current_cost)

        imageio.mimsave("results/hill_climb_simulation_across_different_iterations.gif", images, duration=0.5)
        print("GIF saved")
        return coords, best_route, best_cost, costs

    initial_route = list(range(num_nodes))
    np.random.shuffle(initial_route)
    return run_hill_climb(initial_route, iterations=iterations)

