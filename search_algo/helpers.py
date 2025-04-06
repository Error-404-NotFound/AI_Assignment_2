def heuristic(state, goal_state, grid_size):
    x1, y1 = state % grid_size, state // grid_size
    x2, y2 = goal_state % grid_size, goal_state // grid_size
    return abs(x1 - x2) + abs(y1 - y2)

def get_successors(env, state):
    successors = []
    for action in range(env.action_space.n):
        for prob, next_state, reward, done in env.unwrapped.P[state][action]:
            if prob > 0:
                successors.append((next_state, action, 1))
                break
    return successors