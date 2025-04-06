import imageio
import os
import numpy as np
import matplotlib.pyplot as plt
from search_algo.dfbnb import dfbnb
from search_algo.ida_star import ida_star
from search_algo.hill_climb import hill_climb, total_distance_hc
from search_algo.simulated_annealing import simulated_annealing, total_distance_sa

def save_gif(env, path_actions, filename="output.gif"):
    frames = []
    obs, _ = env.reset()
    frames.append(env.render())

    for action in path_actions:
        obs, _, terminated, truncated, _ = env.step(action)
        frame = env.render()
        if frame is not None:
            frames.append(frame)
        if terminated or truncated:
            break

    print(f"Collected {len(frames)} frames for the GIF.")
    if frames:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        imageio.mimsave(filename, frames, duration=0.5)
        print(f"GIF saved as {filename}")
    else:
        print("No frames captured. GIF not created.")

def plot_results_dfbnb_ida(dfbnb_times, ida_times):
    x = np.arange(1, len(dfbnb_times) + 1)
    plt.plot(x, dfbnb_times, marker='o', label="DFBnB", color='skyblue')
    plt.plot(x, ida_times, marker='o', label="IDA*", color='salmon')
    plt.xlabel("Episode")
    plt.ylabel("Time Taken (s)")
    plt.title("Time Taken per Episode on Frozen Lake by DFBnB and IDA*")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results/search_times_plot.png")
    plt.show()
    
def plot_average_results(dfbnb_times, ida_times):
    dfbnb_avg = np.mean(dfbnb_times)
    ida_avg = np.mean(ida_times)
    plt.bar(['DFBnB', 'IDA*'], [dfbnb_avg, ida_avg], color=['skyblue', 'salmon'])
    plt.ylabel("Average Time Taken (s)")
    plt.title("Average Time Taken by DFBnB and IDA*")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig("results/average_search_times.png")
    plt.show()
    
def hill_climb_cost_vs_iterations(costs, stats_path):
    plt.figure(figsize=(10, 5))
    plt.plot(costs, color='blue', label='Tour Cost')
    plt.title("Hill Climbing - Tour Cost over Iterations")
    plt.xlabel("Iteration")
    plt.ylabel("Tour Cost")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(stats_path)
    plt.show()
    print(f"Stats saved to: {stats_path}")
    
def animated_tour_gif(coords, path, gif_name="animated_tour.gif", title="Final Tour Animation"):
    os.makedirs("frames", exist_ok=True)
    frames = []

    for i in range(2, len(path) + 1):
        fig, ax = plt.subplots(figsize=(6, 6))
        sub_path = path[:i]
        x = coords[sub_path, 0]
        y = coords[sub_path, 1]
        ax.plot(x, y, 'o-', color='blue', label="Tour Progress")
        ax.scatter(coords[:, 0], coords[:, 1], c='red', s=10, zorder=5)
        ax.set_title(f"{title}\nStep {i}/{len(path)}")
        ax.axis("off")
        
        filename = f"frames/frame_{i:03d}.png"
        fig.savefig(filename)
        frames.append(imageio.imread(filename))
        plt.close(fig)

    # Add final frame with closed loop and cost
    fig, ax = plt.subplots(figsize=(6, 6))
    x = coords[path, 0].tolist() + [coords[path[0], 0]]
    y = coords[path, 1].tolist() + [coords[path[0], 1]]
    ax.plot(x, y, 'o-', color='green', label="Final Tour")
    ax.scatter(coords[:, 0], coords[:, 1], c='red', s=10)
    ax.set_title(f"{title}\nFinal Tour | Cost: {total_distance_hc(path, coords):.2f}")
    ax.axis("off")
    final_frame_path = "frames/final_frame.png"
    fig.savefig(final_frame_path)
    frames.append(imageio.imread(final_frame_path))
    plt.close(fig)

    # Save GIF
    gif_path = os.path.join(".", gif_name)
    imageio.mimsave(gif_path, frames, fps=4)
    print(f"Animated GIF saved to: {gif_path}")
    
def simulated_annealing_cost_vs_iterations(costs, stats_path):
    plt.figure(figsize=(10, 5))
    plt.plot(costs, color='green', label='Tour Cost (SA)')
    plt.title("Simulated Annealing - Tour Cost over Iterations")
    plt.xlabel("Iteration")
    plt.ylabel("Tour Cost")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(stats_path)
    plt.show()
    print(f"Stats saved to: {stats_path}")
    
def plot_time(hc,sa):
    plt.bar(['Hill Climbing', 'Simulated Annealing'], [hc, sa], color=['skyblue', 'salmon'])
    plt.ylabel("Average Time Taken (s)")
    plt.title("Average Time Taken by HC and SA")
    plt.grid(axis='y')
    plt.tight_layout()
    plt.savefig("results/times_for_hc_and_sa.png")
    plt.show()