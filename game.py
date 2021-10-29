from board import Board
from blue_placement import BluePlacement
from red_placement import RedPlacement
from blue_player import BluePlayer
from red_player import RedPlayer


class Game:
    def __init__(self):
        self.blue_player = BluePlayer(BluePlacement(0))
        self.red_player = RedPlayer(RedPlacement(0))
        self.running = True
        self.blue_name = input("Blue player what is you name: ")
        self.red_name = input("Red player what is you name: ")
        self.board = Board()
        self.turn = 1
        self.rolls = 1

    def run(self):
        print(f"Welcome {self.blue_name} and {self.red_name} lets play monopoly")
        while self.running:
            if self.turn == 1:
                self.board.print_board()
                self.blue_player_input()
            elif self.turn == 2:
                self.board.print_board()
                self.red_player_input()

    def blue_player_input(self):
        print(f"{self.blue_name} what do you want to do? ")
        blue_command = input("> ")

        if blue_command.lower() == "roll":
            if self.rolls > 1:
                print(f"You can only roll the dice once")
                print(f"Its {self.red_name}s turn now")
                self.rolls = 1
                self.turn = 2
            elif self.rolls == 1:
                self.blue_player.roll_dice()
                owner = self.board.current_placement_blue_player(self.blue_player.my_position())
                if owner == 2:
                    self.turn = 2
                    self.rolls = 1
                elif owner == 1:
                    self.rolls += 1
                else:
                    self.rolls += 1
                print(self.blue_player.my_position())

        elif blue_command.lower() == "buy":
            enough = self.blue_player.buy_property(self.blue_player.my_position())
            if enough == "yes":
                self.board.check_owner_blue_player(self.blue_player.my_position())
                print(f"Its {self.red_name}s turn now")
                self.turn = 2
                self.rolls = 1
            elif enough == "no":
                print(f"Not enough money, its {self.red_name}s turn now")
                self.turn = 2
                self.rolls = 1
            elif enough == "no house":
                self.board.check_owner_blue_player(self.blue_player.my_position())
                print(f"Its {self.red_name}s turn now")
                self.turn = 2
                self.rolls = 1

        elif blue_command.lower() == "done":
            self.turn = 2
            self.rolls = 1
        elif blue_command.lower() == "portfolio":
            self.blue_player.show_portfolio()
        elif blue_command.lower() == "quit" or "exit":
            self.running = False
        else:
            pass

    def red_player_input(self):
        print(f"{self.red_name} what do you want to do? ")
        red_command = input("> ")

        if red_command.lower() == "roll":
            if self.rolls > 1:
                print(f"You can only roll the dice once, its {self.blue_name}s turn now")
                self.rolls = 1
                self.turn = 1
            elif self.rolls == 1:
                self.red_player.roll_dice()
                owner = self.board.current_placement_red_player(self.red_player.my_position())
                if owner == 1:
                    self.turn = 1
                    self.rolls = 1
                elif owner == 2:
                    self.rolls += 1
                else:
                    self.rolls += 1
                print(self.red_player.my_position())
        elif red_command.lower() == "done":
            self.turn = 1
            self.rolls = 1
        elif red_command.lower() == "quit" or "exit":
            self.running = False
