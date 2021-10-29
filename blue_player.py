import random
from houses import houses


class BluePlayer:
    def __init__(self, placement):
        self.placement = placement
        self.portfolio = []
        #self.add_house_by_id("id4")
        self.money = 200
        #self.remove_house_by_id('id2')

    def add_house_by_id(self, house_id):
        for house in houses:
            if house["id"] == house_id:
                self.portfolio.append(house)
                print(self.portfolio[0]["description"])

    def remove_house_by_id(self, house_id):
        remove_index = -1
        for i, house in enumerate(self.portfolio):
            if house["id"] == house_id:
                remove_index = i
        if remove_index >= 0:
            self.portfolio.pop(remove_index)

    def roll_dice(self):
        dice = random.choice([1, 2, 3, 4, 5, 6])
        print(f"You rolled a {dice}")
        self.placement.position += dice
        if self.placement.position >= 12:
            self.money += 100
            print("You have walked around the hole block, you get 100$")
            print(f"You now have {self.money}$")
            self.placement.position -= 12

    def buy_property(self, house):
        if house == 1:
            if self.money >= 100:
                self.money -= houses[0]["price"]
                self.portfolio.append("A yellow house")
                print(self.portfolio)
                print(f"{self.money}$")
                return "yes"
            else:
                return "no"
        elif house == 4:
            if self.money >= 200:
                self.money -= houses[1]["price"]
                self.portfolio.append("A purple house")
                return "yes"
            else:
                return "no"
        elif house == 8:
            if self.money >= 300:
                self.money -= houses[2]["price"]
                self.portfolio.append("A green house")
                return "yes"
            else:
                return "no"
        elif house == 11:
            if self.money >= 400:
                self.money -= houses[3]["price"]
                self.portfolio.append("A black house")
                return "yes"
            else:
                return "no"
        else:
            return "no house"

    def sell_property(self):
        pass

    def show_portfolio(self):
        if len(self.portfolio) > 0:
            print(self.portfolio)
        else:
            print("Your portfolio is empty")

    def my_position(self):
        return self.placement.position
