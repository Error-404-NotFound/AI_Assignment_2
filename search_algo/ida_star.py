import time
from collections import deque
from .helpers import get_successors, heuristic

def ida_star(env, start_state, goal_state, max_time=600):
    grid_size = int(env.observation_space.n ** 0.5)
    start_time = time.time()
    best_path = []
    best_actions = []

    def dfs(path, actions, g, threshold):
        node = path[-1]
        f = g + heuristic(node, goal_state, grid_size)
        if f > threshold:
            return f, None, None
        if node == goal_state:
            return f, list(path), list(actions)

        min_threshold = float('inf')
        for succ, action, cost in get_successors(env, node):
            if succ not in path:
                path.append(succ)
                actions.append(action)
                t, result_path, result_actions = dfs(path, actions, g + cost, threshold)
                if result_path is not None:
                    return t, result_path, result_actions
                if t < min_threshold:
                    min_threshold = t
                path.pop()
                actions.pop()
        return min_threshold, None, None

    threshold = heuristic(start_state, goal_state, grid_size)
    path = [start_state]
    actions = []

    while time.time() - start_time < max_time:
        temp, best_path, best_actions = dfs(path, actions, 0, threshold)
        if best_path is not None:
            return best_path, best_actions, len(best_actions), time.time() - start_time
        if temp == float('inf'):
            break
        threshold = temp

    return [], [], None, time.time() - start_time