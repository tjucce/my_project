from terminal_color import color_print
from houses import houses


class Board:
    def __init__(self):
        self.board = [
                [7, 1, 7, 7],
                [4, 0, 0, 2],
                [7, 0, 0, 7],
                [7, 3, 7, 7]
            ]

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
            if self.board[1][3] == 2:
                print("A purple house for sale")
            elif self.board[1][3] == 5:
                print("You are on your own house")
            elif self.board[1][3] == 6:
                print("You are on red players house, time to pay")
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
            if self.board[3][1] == 3:
                print("A green house for sale")
            elif self.board[3][1] == 5:
                print("You are on your own house")
            elif self.board[3][1] == 6:
                print("You are on red players house, time to pay")
        elif placement == 9:
            #  position = d1
            print("You are at D1")
        elif placement == 10:
            #  position = c1
            print("You are at C1")
        elif placement == 11:
            #  position = b1
            print("You are at B1")
            if self.board[1][0] == 4:
                print("A black house for sale")
            elif self.board[1][0] == 5:
                print("You are on your own house")
            elif self.board[1][0] == 6:
                print("You are on red players house, time to pay")

    def check_owner_blue_player(self, position):
        if position == 1:
            if self.board[0][1] == 5:
                print("You already own this house")
            else:
                self.board[0][1] = 5
                print("Congratulations you bought the house")
        if position == 2:
            print("No house to buy on this position")
        if position == 3:
            print("No house to buy on this position")
        if position == 4:
            if self.board[1][3] == 5:
                print("You already own this house")
            else:
                self.board[1][3] = 5
                print("Congratulations you bought the house")
        if position == 5:
            print("No house to buy on this position")
        if position == 6:
            print("No house to buy on this position")
        if position == 7:
            print("No house to buy on this position")
        if position == 8:
            if self.board[3][1] == 5:
                print("You already own this house")
            else:
                self.board[3][1] = 5
                print("Congratulations you bought the house")
        if position == 9:
            print("No house to buy on this position")
        if position == 10:
            print("No house to buy on this position")
        if position == 11:
            if self.board[1][0] == 5:
                print("You already own this house")
            else:
                self.board[1][0] = 5
                print("Congratulations you bought the house")
