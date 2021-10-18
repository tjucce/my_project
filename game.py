from board import Board
from placement import Placement
from blue_player import BluePlayer
from red_player import RedPlayer


class Game:
    def __init__(self):
        self.blue_player = BluePlayer(Placement(0))
        self.red_player = RedPlayer(Placement(0))
        self.running = True
        self.blue_name = input("Blue player what is you name: ")
        self.red_name = input("Red player what is you name: ")
        self.board = Board([
                [7, 1, 7, 7],
                [4, 0, 0, 2],
                [7, 0, 0, 7],
                [7, 3, 7, 7]
            ])
        self.turn = 1

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
            self.blue_player.roll_dice()
            self.board.current_placement(self.blue_player.my_position())
            print(self.blue_player.my_position())
        elif blue_command.lower() == "buy":
            if self.blue_player.my_position() == 1:
                self.board.__init__([
                [7, 5, 7, 7],
                [4, 0, 0, 2],
                [7, 0, 0, 7],
                [7, 3, 7, 7]
            ])
            #  self.board.check_owner(self.board.current_placement(self.blue_player.my_position()))
        elif blue_command.lower() == "done":
            self.turn = 2
        elif blue_command.lower() == "quit" or "exit":
            self.running = False
        else:
            print("Input not valid")

    def red_player_input(self):
        print(f"{self.red_name} what do you want to do? ")
        red_command = input("> ")

        if red_command.lower() == "roll":
            self.red_player.roll_dice()
            print(self.blue_player.my_position())
        elif red_command.lower() == "done":
            self.turn = 1
        elif red_command.lower() == "quit" or "exit":
            self.running = False
