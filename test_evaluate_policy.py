import unittest

from go_when_1.main import GoWhen1
from evaluate_policy import evaluate_policy


class Policy:
    def request_action(self, state):
        return state


class TestEvaluatePolicy(unittest.TestCase):
    def test_evaluate_policy(self):
        go_when_1 = GoWhen1(100)
        policy = Policy()
        V = evaluate_policy(go_when_1, policy, 3)
        self.assertEqual(V, {0: 1, 1: 1})


if __name__ == '__main__':
    unittest.main()
