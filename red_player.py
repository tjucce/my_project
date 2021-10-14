import random


class RedPlayer:
    def __init__(self, placement):
        self.placement = placement
        self.portfolio = []

    def roll_dice(self):
        dice = random.choice([1, 2, 3, 4, 5, 6])
        print(f"You rolled a {dice}")
        self.placement.position += dice

    def buy_property(self):
        pass

    def sell_property(self):
        pass

    def show_portfolio(self):
        pass

    def my_position(self):
        return self.placement.position
