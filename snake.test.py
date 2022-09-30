import unittest
import snake
import player

class SnakeTest(unittest.TestCase):
    venomous_snake = snake.Snake('', '.. ', True, '', '', '', [0, 0, 0])
    nonvenomous_snake = snake.Snake('', '.. ', False, '', '', '', [0, 0, 0])
    # test venomous snake bite
    def test_bite_venomous(self):
        #arrange
        test_player = player.Player('Test Player')
        #act
        self.venomous_snake.bite(test_player)
        #assert
        self.assertEqual(-5, test_player.score, "Player's score wasn't decreased by 5")
        self.assertGreater(5, test_player.health, "Player's health wasn't decreased after venomous bite.")
    # test nonvenomous snake bite
    def test_bite_nonvenomous(self):
        #test_player = None
        test_player = player.Player('Test Player')
        self.nonvenomous_snake.bite(test_player)
        self.assertEqual(-2, test_player.score, "Player's score wasn't decreased by 2")
        #4<=test_player.health
        self.assertLessEqual(4, test_player.health, "Player's health was decreased by more than 1 point.")
    # test venomous snake hiss
    def test_hiss_venomous(self):
        test_player = player.Player('Test Player')
        self.venomous_snake.hiss(test_player)
        self.assertEqual(5, test_player.score, "Player's score wasn't increased by 5")
        self.assertEqual(4, test_player.health, "Player's health wasn't decreased by 1.")
    # test nonvenomous snake hiss
    def test_hiss_nonvenomous(self):
        test_player = player.Player('Test Player')
        self.nonvenomous_snake.hiss(test_player)
        self.assertEqual(5, test_player.score, "Player's score wasn't increased by 5")
        self.assertEqual(4, test_player.health, "Player's health wasn't decreased by 1.")

    def test_coil_venomous(self):
        test_player = player.Player('Test Player')
        self.venomous_snake.coil(test_player)
        self.assertEqual(10, test_player.score, "Player's score wasn't increased by 10 points")

    def test_none_player(self):
        test_player = None
        with self.assertRaises(AttributeError):
            self.venomous_snake.bite(test_player)

if __name__ == '__main__':
    unittest.main()


