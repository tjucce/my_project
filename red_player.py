import random
from houses import houses


class RedPlayer:
    def __init__(self, placement):
        self.placement = placement
        self.portfolio = []
        self.money = 200

    def roll_dice(self):
        dice = random.choice([1, 2, 3, 4, 5, 6])
        print(f"You rolled a {dice}")
        self.placement.position += dice
        if self.placement.position >= 12:
            self.money += 50
            print("You have walked around the hole block, you get 50$")
            print(f"You now have {self.money}$")
            self.placement.position -= 12

    def buy_property(self, position):
        if position == 1:
            if self.money >= 100:
                self.money -= houses[0]["price"]
                self.portfolio.append("A yellow house")
                return "yes"
            else:
                print("You don't have enough money")
        elif position == 4:
            if self.money >= 200:
                self.money -= houses[1]["price"]
                self.portfolio.append("A purple house")
                return "yes"
            else:
                print("You don't have enough money")
        elif position == 8:
            if self.money >= 300:
                self.money -= houses[2]["price"]
                self.portfolio.append("A green house")
                return "yes"
            else:
                print("You don't have enough money")
        elif position == 11:
            if self.money >= 400:
                self.money -= houses[3]["price"]
                self.portfolio.append("A black house")
                return "yes"
            else:
                print("You don't have enough money")
        else:
            return "no house"

    def sell_property(self, position):
        if position == 1:
            self.money += houses[0]["price"]
            self.portfolio.remove("A yellow house")
            print(f"You sold your house, you now have {self.money}$ left in your bank")
        elif position == 4:
            self.money += houses[1]["price"]
            self.portfolio.remove("A purple house")
            print(f"You sold your house, you now have {self.money}$ left in your bank")
        elif position == 8:
            self.money += houses[2]["price"]
            self.portfolio.remove("A green house")
            print(f"You sold your house, you now have {self.money}$ left in your bank")
        elif position == 11:
            self.money += houses[3]["price"]
            self.portfolio.remove("A black house")
            print(f"You sold your house, you now have {self.money}$ left in your bank")

    def show_portfolio(self):
        if len(self.portfolio) > 0:
            print(self.portfolio)
        else:
            print("You have no house in your portfolio")

    def my_position(self):
        return self.placement.position

    def pay_rent(self, position):
        if position == 1:
            self.money -= houses[0]["rent"]
            print("You just payed 50$ in rent")
        elif position == 4:
            self.money -= houses[1]["rent"]
            print("You just payed 100$ in rent")
        elif position == 8:
            self.money -= houses[2]["rent"]
            print("You just payed 150$ in rent")
        elif position == 11:
            self.money -= houses[3]["rent"]
            print("You just payed 200$ in rent")

    def collect_rent(self, position):
        if position == 1:
            self.money += houses[0]["rent"]
        elif position == 4:
            self.money += houses[1]["rent"]
        elif position == 8:
            self.money += houses[2]["rent"]
        elif position == 11:
            self.money += houses[3]["rent"]
