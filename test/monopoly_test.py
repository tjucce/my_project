import unittest
from game import Game


class MyTestCase(unittest.TestCase):
    def test_buy_house(self):
        game = Game()
        game.blue_player.placement = 1
        position = game.blue_player.placement
        game.blue_player.buy_property(position)
        game.board.check_owner_blue_player(position)
        self.assertEqual(game.blue_player.portfolio, ["A yellow house"])

    def test_buy_to_expensive(self):
        game = Game()
        game.blue_player.placement = 8
        position = game.blue_player.placement
        game.blue_player.buy_property(position)
        self.assertEqual(game.blue_player.portfolio, [])

    def test_buy_no_house(self):
        game = Game()
        game.blue_player.placement = 2
        position = game.blue_player.placement
        game.blue_player.buy_property(position)
        game.board.check_owner_blue_player(position)
        self.assertEqual(game.blue_player.portfolio, [])

    def test_money_update(self):
        game = Game()
        game.blue_player.placement = 4
        position = game.blue_player.placement
        print(f"Money before buy {game.blue_player.money}$")
        game.blue_player.buy_property(position)
        game.board.check_owner_blue_player(position)
        print(f"Money after buy {game.blue_player.money}$")
        self.assertEqual(game.blue_player.money, 0)

    def test_sell_house(self):
        game = Game()
        game.red_player.placement = 1
        position = game.red_player.placement
        game.red_player.sell_property(position)
        self.assertEqual(game.blue_player.portfolio, [])

    def test_sell_owned_house(self):
        game = Game()
        game.red_player.placement = 1
        position = game.red_player.placement
        game.red_player.buy_property(position)
        self.assertEqual(game.red_player.portfolio, ["A yellow house"])
        self.assertEqual(game.red_player.money, 100)
        game.red_player.sell_property(position)
        self.assertEqual(game.blue_player.portfolio, [])
        self.assertEqual(game.red_player.money, 200)


if __name__ == '__main__':
    unittest.main()
