def evaluate_policy(environment, policy, number_of_episodes):
    V = dict()
    returns = dict()

    gamma = 0.9

    for episode_number in range(number_of_episodes):
        steps = []

        environment.reset()
        T = 0

        while not environment.is_done():
            state = environment.request_state()
            action = policy.request_action(state)
            reward = environment.act(action)

            step = (state, action, reward)
            steps.append(step)

            T += 1

        unvisited_states = set(state for state, action, reward in steps)

        G = 0
        for t in range(T - 2, 0, -1):
            state, action, reward = steps[t]
            G = gamma * G + reward
            if state in unvisited_states:
                if state not in returns:
                    returns[state] = []
                returns[state].append(reward)
                V[state] = average(returns[state])

    return V


def average(values):
    return sum(values) / float(len(values))