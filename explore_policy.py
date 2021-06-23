import random


class Policy:
    DEFAULT_ACTION_INDEX = 0

    def __init__(self):
        self.policy = dict()

    def request_action(self, state, available_actions):
        if len(available_actions) >= 1:
            if state in self.policy:
                action = self.policy[state]
                if action not in available_actions:
                    action = available_actions[Policy.DEFAULT_ACTION_INDEX]
            else:
                action = available_actions[Policy.DEFAULT_ACTION_INDEX]
        else:
            action = None

        return action


DEFAULT_ESTIMATED_VALUE = 0


def explore_policy(environment, number_of_episodes):
    """
    Reference: [Monte Carlo ES (Exploring Starts) π ≈ π* (p. 121)](http://incompleteideas.net/book/RLbook2020.pdf)
    """
    policy = Policy()
    Q = dict()
    returns = dict()

    available_actions_at_state = dict()

    exploration_rate = 0.5

    for episode_number in range(number_of_episodes):
        steps = []

        environment.reset()
        T = 0

        while not environment.is_done():
            state = environment.request_state()
            available_actions = environment.request_available_actions()
            available_actions_at_state[state] = available_actions
            if random.random() <= exploration_rate:
                action = random.choice(available_actions)
            else:
                action = policy.request_action(state, available_actions)
            reward = environment.act(action)

            step = (state, action, reward)
            steps.append(step)

            T += 1

        unvisited_states = set(state for state, action, reward in steps)

        for t in range(T - 2, 0, -1):
            state, action, reward = steps[t]
            if state in unvisited_states:
                if state not in returns:
                    returns[(state, action)] = []
                returns[(state, action)].append(reward)
                Q[(state, action)] = average(returns[(state, action)])
                policy.policy[state] = argmax(
                    available_actions_at_state[state],
                    lambda action: Q[(state, action)] if (state, action) in Q else DEFAULT_ESTIMATED_VALUE
                )

    return policy


def average(values):
    return sum(values) / float(len(values))


def argmax(values, predicate):
    return max(values, key=predicate)
