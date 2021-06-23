import unittest

from go_when_1.main import GoWhen1
from main import evaluate_policy


class Policy:
    def request_action(self, state):
        return state


class TestMain(unittest.TestCase):
    def test_main(self):
        go_when_1 = GoWhen1(100)
        policy = Policy()
        V = evaluate_policy(go_when_1, policy, 3)
        self.assertEquals(V, {0: 1, 1: 1})


if __name__ == '__main__':
    unittest.main()
