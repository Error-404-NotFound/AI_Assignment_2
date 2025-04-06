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

def total_distance_sa(route, coords):
    return sum(
        np.linalg.norm(coords[route[i]] - coords[route[(i + 1) % len(route)]])
        for i in range(len(route))
    )

def simulated_annealing(num_nodes=100, iterations=1000, initial_temp=100.0, cooling_rate=0.995):
    print(f"Running Simulated Annealing with {num_nodes} nodes, {iterations} iterations, temperature {initial_temp}, and cooling rate {cooling_rate}.")
    frame_folder = "frames_sa"
    env = TSPEnv(num_nodes=num_nodes, batch_size=1, num_draw=1)
    state = env.reset()[0]  # Get state for a single graph
    coords = state[:, :2]

    def total_distance(route):
        return sum(np.linalg.norm(coords[route[i]] - coords[route[(i + 1) % len(route)]])
                   for i in range(len(route)))

    def run_simualted_annealing(init_route, iterations=1000, initial_temp=100.0, cooling_rate=0.995):
        current_route = init_route.copy()
        current_cost = total_distance(current_route)
        best_route = current_route.copy()
        best_cost = current_cost
        temp = initial_temp
        costs = []
        images = []

        os.makedirs(frame_folder, exist_ok=True)

        for i in range(iterations):
            a, b = np.random.choice(len(current_route), size=2, replace=False)
            new_route = current_route.copy()
            new_route[a], new_route[b] = new_route[b], new_route[a]
            new_cost = total_distance(new_route)

            # Acceptance condition
            if new_cost < current_cost or np.random.rand() < np.exp((current_cost - new_cost) / temp):
                current_route = new_route
                current_cost = new_cost

                if new_cost < best_cost:
                    best_route = new_route
                    best_cost = new_cost

            temp *= cooling_rate
            costs.append(current_cost)

            if i % 50 == 0 or i == iterations - 1:
                fig, ax = plt.subplots(figsize=(6, 6))
                tour_coords = coords[best_route + [best_route[0]]]
                ax.plot(tour_coords[:, 0], tour_coords[:, 1], 'o-', color='green')
                ax.set_title(f"Simulated_Annealing_Simulation_across_different_iterations \nStep {i}\nCost: {best_cost:.2f}")
                ax.axis("off")
                frame_path = f"{frame_folder}/frame_{i:03d}.png"
                plt.savefig(frame_path)
                images.append(imageio.imread(frame_path))
                plt.close()

        imageio.mimsave("results/simulated_annealing_simulation_across_different_iterations.gif", images, duration=0.5)
        print(f"GIF saved")
        return coords, best_route, best_cost, costs

    initial_route = list(range(num_nodes))
    np.random.shuffle(initial_route)
    return run_simualted_annealing(initial_route, iterations=iterations, initial_temp=initial_temp, cooling_rate=cooling_rate)

