from terminal_color import color_print
from houses import houses


class Board:
    def __init__(self, board):
        self.board = board

    def print_board(self):
        for row in self.board:
            for cell in row:
                color = "white"
                if cell == 1:
                    color = "yellow"
                elif cell == 2:
                    color = "magenta"
                elif cell == 3:
                    color = "green"
                elif cell == 4:
                    color = "black"
                elif cell == 5:
                    color = "blue"
                elif cell == 6:
                    color = "red"
                elif cell == 7:
                    color = "grey"
                color_print(color, "⬜", end=" ")
            print()

    def current_placement(self, placement):
        if placement == 0:
            #  position = a1
            print("You are at A1")
        elif placement == 1:
            #  position = a2
            print("You are at A2")
            if self.board[0][1] == 1:
                print("A yellow house for sale")
            elif self.board[0][1] == 5:
                print("You are on your own house")
            elif self.board[0][1] == 6:
                print("You are on red players house, time to pay")

        elif placement == 2:
            #  position = a3
            print("You are at A3")
        elif placement == 3:
            #  position = a4
            print("You are at A4")
        elif placement == 4:
            #  position = b4
            print("You are at B4")
        elif placement == 5:
            #  position = c4
            print("You are at C4")
        elif placement == 6:
            #  position = d4
            print("You are at D4")
        elif placement == 7:
            #  position = d3
            print("You are at D3")
        elif placement == 8:
            #  position = d2
            print("You are at D2")
        elif placement == 9:
            #  position = d1
            print("You are at D1")
        elif placement == 10:
            #  position = c1
            print("You are at C1")
        elif placement == 11:
            #  position = b1
            print("You are at B1")

    def check_owner(self, position):
        if position == 1:
            self.board[0][1] = 5
            print("Congratz you bought the house")
            


