import random


class RedPlayer:
    def __init__(self, position):
        self.position = position
        self.portfolio = []

    def roll_dice(self):
        dice = random.choice([1, 2, 3, 4, 5, 6])
        print(f"You rolled a {dice}")

    def buy_property(self):
        pass

    def sell_property(self):
        pass

    def show_portfolio(self):
        pass
