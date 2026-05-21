import unittest

from probability import can_attack_hit
from probability import calculate_probability


class TestProbability(unittest.TestCase):

    def test_attack_hits(self):
        self.assertTrue(can_attack_hit(7000, 1000))

    def test_attack_fails(self):
        self.assertFalse(can_attack_hit(5000, 2000))

    def test_probability(self):
        attacks = [7000, 8000, 5000]

        result = calculate_probability(attacks, 1000)

        self.assertEqual(result, 66.67)


if __name__ == "__main__":
    unittest.main()
