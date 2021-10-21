import random


class BluePlayer:
    def __init__(self, placement):
        self.placement = placement
        self.portfolio = []
        self.money = 200

    def roll_dice(self):
        dice = random.choice([1, 2, 3, 4, 5, 6])
        print(f"You rolled a {dice}")
        self.placement.position += dice
        if self.placement.position >= 12:
            self.placement.position -= 12

    def buy_property(self, house):
        if house == 1:
            if self.money >= 100:
                self.money -= 100
                return "yes"
            else:
                return "no"
        elif house == 4:
            if self.money >= 200:
                self.money -= 200
                return "yes"
            else:
                return "no"
        elif house == 8:
            if self.money >= 300:
                self.money -= 300
                return "yes"
            else:
                return "no"
        elif house == 11:
            if self.money >= 400:
                self.money -= 400
                return "yes"
            else:
                return "no"

    def sell_property(self):
        pass

    def show_portfolio(self):
        pass

    def my_position(self):
        return self.placement.position
