import imageio
import os
import numpy as np
import matplotlib.pyplot as plt
from search_algo.dfbnb import dfbnb
from search_algo.ida_star import ida_star

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