from board import Board
from blue_player import BluePlayer
from red_player import RedPlayer


class Game:
    def __init__(self):
        self.blue_player = BluePlayer(0)
        self.red_player = RedPlayer(0)
        self.running = True
        self.blue_name = input("Blue player what is you name: ")
        self.red_name = input("Red player what is you name: ")
        self.board = Board()

    def run(self):
        print(f"Welcome {self.blue_name} and {self.red_name} lets play monopoly")
        while self.running:
            self.blue_board_info()
            self.blue_player_input()
            self.red_board_info()
            self.red_player_input()

    def blue_board_info(self):
        self.board.print_board()

    def blue_player_input(self):
        print(f"{self.blue_name} what do you want to do? ")
        blue_command = input("> ")

        if blue_command.lower() == "roll":
            self.blue_player.roll_dice()

    def red_board_info(self):
        self.board.print_board()

    def red_player_input(self):
        print(f"{self.red_name} what do you want to do? ")
        red_command = input("> ")

        if red_command.lower() == "roll":
            self.red_player.roll_dice()
