from numbers import Number
import unittest
from parameterized import parameterized

import snake
import player


class PlayerTest(unittest.TestCase):
    @parameterized.expand([
        ["positive number", 5, 5],
        ["zero", 0, 0],
        ["negative number", -5, -5],
        # ["nan", float('nan'), float('nan')]
    ])
    def test_add_score(self, test_case_name, score, expected_score):
        test_player = player.Player('Test Player')

        test_player.add_score(score)

        self.assertEqual(expected_score, test_player.score)   
        # assertTrue(math.isnan(nan_value))

if __name__ == '__main__':
    unittest.main()