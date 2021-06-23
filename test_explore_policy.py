import unittest

from explore_policy import explore_policy
from go_when_1.main import GoWhen1


class TestExplorePolicy(unittest.TestCase):
    def test_explore_policy(self):
        environment = GoWhen1(100)
        policy = explore_policy(environment, 3)
        self.assertEqual(policy.request_action(0, (0, 1)), 0)
        self.assertEqual(policy.request_action(1, (0, 1)), 1)
