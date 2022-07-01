import unittest

import snake
import player


class SnakeTest(unittest.TestCase):
    venomousSnake = snake.Snake(True, '', '', '', [0, 0, 0])
    def test_bite_venomous(self):
        #arrange
        test_player = player.Player('Test Player')

        #act
        self.venomousSnake.bite(test_player)

        #assert
        self.assertEqual(-5, test_player.score, "Player's score wasn't dicreased by 5")
        self.assertGreater(5, test_player.health, "Player's health wasn't dicreased after venomous bite.")

if __name__ == '__main__':
    unittest.main()