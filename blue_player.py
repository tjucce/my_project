import random
from houses import houses


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
                return "no"
        elif position == 4:
            if self.money >= 200:
                self.money -= houses[1]["price"]
                self.portfolio.append("A purple house")
                return "yes"
            else:
                return "no"
        elif position == 8:
            if self.money >= 300:
                self.money -= houses[2]["price"]
                self.portfolio.append("A green house")
                return "yes"
            else:
                return "no"
        elif position == 11:
            if self.money >= 400:
                self.money -= houses[3]["price"]
                self.portfolio.append("A black house")
                return "yes"
            else:
                return "no"
        else:
            return "no house"

    def sell_property(self, position):
        if position == 1:
            if "A yellow house" in self.portfolio:
                self.money += houses[0]["price"]
                self.portfolio.remove("A yellow house")
                return 1
            else:
                print("You need to own the house before you can sell it")
        elif position == 4:
            if "A purple house" in self.portfolio:
                self.money += houses[1]["price"]
                self.portfolio.remove("A purple house")
                return 1
            else:
                print("You need to own the house before you can sell it")
        elif position == 8:
            if "A green house" in self.portfolio:
                self.money += houses[2]["price"]
                self.portfolio.remove("A green house")
                return 1
            else:
                print("You need to own the house before you can sell it")
        elif position == 11:
            if "A black house" in self.portfolio:
                self.money += houses[3]["price"]
                self.portfolio.remove("A black house")
                return 1
            else:
                print("You need to own the house before you can sell it")

    def show_portfolio(self):
        if len(self.portfolio) > 0:
            print(self.portfolio)
        else:
            print("Your portfolio is empty")

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
