import unittest
from game import Game


class MyTestCase(unittest.TestCase):
    def test_buy_house(self):
        game = Game()
        game.blue_player.placement = 1
        position = game.blue_player.placement
        game.blue_player.buy_property(position)
        print(game.board.check_owner_blue_player(position))
        self.assertEqual(game.blue_player.portfolio, ["A yellow house"])  # add assertion here

    def test_buy_to_expensive(self):
        game = Game()
        game.blue_player.placement = 8
        position = game.blue_player.placement
        game.blue_player.buy_property(position)
        self.assertEqual(game.blue_player.portfolio, [])  # add assertion here


if __name__ == '__main__':
    unittest.main()
