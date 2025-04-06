from collections import deque
import time
from .helpers import get_successors, heuristic

def dfbnb(env, start_state, goal_state, max_time=600):
    grid_size = int(env.observation_space.n ** 0.5)
    best_cost = float('inf')
    best_path = []
    best_actions = []
    visited = {}  # state -> cost
    stack = deque()

    # stack holds: (state, path, actions, cost)
    stack.append((start_state, [start_state], [], 0))

    start_time = time.time()

    while stack and time.time() - start_time < max_time:
        state, path, actions, cost = stack.pop()

        if cost >= best_cost:
            continue

        if state in visited and visited[state] <= cost:
            continue
        visited[state] = cost

        if state == goal_state:
            best_cost = cost
            best_path = path
            best_actions = actions
            continue

        successors = list(get_successors(env, state))
        # Optional: Sort by heuristic to improve pruning
        successors.sort(key=lambda x: heuristic(x[0], goal_state, grid_size))

        for successor, action, step_cost in successors:
            total_cost = cost + step_cost
            if total_cost < best_cost:
                stack.append((successor, path + [successor], actions + [action], total_cost))

    time_elapsed = time.time() - start_time
    return best_path, best_actions, best_cost if best_path else None, time_elapsed