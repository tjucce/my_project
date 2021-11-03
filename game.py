from board import Board
from blue_placement import BluePosition
from red_placement import RedPosition
from blue_player import BluePlayer
from red_player import RedPlayer
from rules import rules


class Game:
    def __init__(self):
        self.blue_player = BluePlayer(BluePosition(0))
        self.red_player = RedPlayer(RedPosition(0))
        self.running = True
        self.blue_name = input("Blue player what is you name: ")
        self.red_name = input("Red player what is you name: ")
        self.board = Board()
        self.turn = 1
        self.rolls = 1

    def run(self):
        print(f"Welcome {self.blue_name} and {self.red_name} lets play monopoly\n This is the rules")
        print(rules)
        while self.running:
            if self.turn == 1:
                self.board.print_board()
                self.blue_player_input()
            elif self.turn == 2:
                self.board.print_board()
                self.red_player_input()

    def blue_player_input(self):
        print(f"{self.blue_name} what do you want to do? ")
        list_of_commands = ["roll", "buy", "sell", "done", "portfolio", "money", "rules", "quit", "exit"]
        blue_command = input("> ")

        if blue_command.lower() not in list_of_commands:
            print("Invalid input, try again")

        elif blue_command.lower() == "roll":
            if self.rolls > 1:
                print(f"You can only roll the dice once \nIts {self.red_name}s turn now")
                self.rolls = 1
                self.turn = 2
            elif self.rolls == 1:
                self.blue_player.roll_dice()
                owner = self.board.current_placement_blue_player(self.blue_player.my_position())
                if owner == 2:
                    self.blue_player.pay_rent(self.blue_player.my_position())
                    self.red_player.collect_rent(self.blue_player.my_position())
                    if self.blue_player.money < 0:
                        print(f"Game over, {self.blue_name} won")
                        self.running = False
                    self.turn = 2
                    self.rolls = 1
                elif owner == 1:
                    self.rolls += 1
                else:
                    self.rolls += 1

        elif blue_command.lower() == "buy":
            if self.board.owner(self.blue_player.my_position()) == "yes":
                enough = self.blue_player.buy_property(self.blue_player.my_position())
                if enough == "yes":
                    self.board.check_owner_blue_player(self.blue_player.my_position())
                    print(f"You now have {self.blue_player.money}$ left in your bank \nIts {self.red_name}s turn now")
                    self.turn = 2
                    self.rolls = 1
                elif enough == "no house":
                    self.board.check_owner_blue_player(self.blue_player.my_position())
            elif self.board.owner(self.blue_player.my_position()) == "blue":
                print("You already own this house")
            elif self.board.owner(self.blue_player.my_position()) == "red":
                print(f"{self.red_name} already owns this house")

        elif blue_command.lower() == "sell":
            position = self.blue_player.my_position()
            place = [1, 4, 8, 11]
            if position in place:
                if self.board.owner(position) == "blue":
                    self.board.sold_house(position)
                    self.blue_player.sell_property(position)
                else:
                    print("You need to own the house before you can sell it")
            else:
                print("You can't sell, you need to be standing on your house to sell")

        elif blue_command.lower() == "done":
            self.turn = 2
            self.rolls = 1

        elif blue_command.lower() == "portfolio":
            self.blue_player.show_portfolio()

        elif blue_command.lower() == "money":
            print(f"You have {self.blue_player.money}$ in your bank")

        elif blue_command.lower() == "rules":
            print(rules)

        elif blue_command.lower() == "quit" or "exit":
            self.running = False

    def red_player_input(self):
        print(f"{self.red_name} what do you want to do? ")
        list_of_commands = ["roll", "buy", "sell", "done", "portfolio", "money", "rules", "quit", "exit"]
        red_command = input("> ")

        if red_command.lower() not in list_of_commands:
            print("Invalid input, try again")

        elif red_command.lower() == "roll":
            if self.rolls > 1:
                print(f"You can only roll the dice once \nIts {self.blue_name}s turn now")
                self.rolls = 1
                self.turn = 1
            elif self.rolls == 1:
                self.red_player.roll_dice()
                owner = self.board.current_placement_red_player(self.red_player.my_position())
                if owner == 1:
                    self.red_player.pay_rent(self.red_player.my_position())
                    self.blue_player.collect_rent(self.red_player.my_position())
                    self.turn = 1
                    self.rolls = 1
                    if self.red_player.money < 0:
                        print(f"Game over, {self.blue_name} won")
                        self.running = False
                elif owner == 2:
                    self.rolls += 1
                else:
                    self.rolls += 1

        elif red_command.lower() == "buy":
            if self.board.owner(self.red_player.my_position()) == "yes":
                enough = self.red_player.buy_property(self.red_player.my_position())
                if enough == "yes":
                    self.board.check_owner_red_player(self.red_player.my_position())
                    print(f"You now have {self.red_player.money}$ left in your bank \nIts {self.blue_name}s turn now")
                    self.turn = 1
                    self.rolls = 1
                elif enough == "no house":
                    self.board.check_owner_red_player(self.red_player.my_position())
            elif self.board.owner(self.red_player.my_position()) == "red":
                print("You already own this house")
            elif self.board.owner(self.red_player.my_position()) == "blue":
                print(f"{self.blue_name} already owns this house")

        elif red_command.lower() == "sell":
            position = self.red_player.my_position()
            place = [1, 4, 8, 11]
            if position in place:
                if self.board.owner(position) == "red":
                    self.board.sold_house(position)
                    self.red_player.sell_property(position)
                else:
                    print("You need to own the house before you can sell it")
            else:
                print("You can't sell, you need to be standing on your house to sell")

        elif red_command.lower() == "done":
            self.turn = 1
            self.rolls = 1

        elif red_command.lower() == "portfolio":
            self.red_player.show_portfolio()

        elif red_command.lower() == "money":
            print(f"You have {self.red_player.money}$ in your bank")

        elif red_command.lower() == "rules":
            print(rules)

        elif red_command.lower() == "quit" or "exit":
            self.running = False
