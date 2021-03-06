from terminal_color import color_print


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

    def current_placement_blue_player(self, placement):
        if placement == 0:
            print("You are at A1")
        elif placement == 1:
            print("You are at A2")
            if self.board[0][1] == 1:
                print("A yellow house for sale\nPrice: 100$ Rent: 50$")
            elif self.board[0][1] == 5:
                print("You are on your own house, do you want to sell?")
            elif self.board[0][1] == 6:
                print("You are at a red house, time to pay")
                return 2
        elif placement == 2:
            print("You are at A3")
        elif placement == 3:
            print("You are at A4")
        elif placement == 4:
            print("You are at B4")
            if self.board[1][3] == 2:
                print("A purple house for sale\nPrice: 200$ Rent: 100$")
            elif self.board[1][3] == 5:
                print("You are on your own house, do you want to sell?")
            elif self.board[1][3] == 6:
                print("You are at a red house, time to pay")
                return 2
        elif placement == 5:
            print("You are at C4")
        elif placement == 6:
            print("You are at D4")
        elif placement == 7:
            print("You are at D3")
        elif placement == 8:
            print("You are at D2")
            if self.board[3][1] == 3:
                print("A green house for sale\nPrice: 300$ Rent: 150$")
            elif self.board[3][1] == 5:
                print("You are on your own house, do you want to sell?")
            elif self.board[3][1] == 6:
                print("You are at a red house, time to pay")
                return 2
        elif placement == 9:
            print("You are at D1")
        elif placement == 10:
            print("You are at C1")
        elif placement == 11:
            print("You are at B1")
            if self.board[1][0] == 4:
                print("A black house for sale\nPrice: 400$ Rent: 200$")
            elif self.board[1][0] == 5:
                print("You are on your own house, do you want to sell?")
            elif self.board[1][0] == 6:
                print("You are at a red house, time to pay")
                return 2

    def current_placement_red_player(self, placement):
        if placement == 0:
            print("You are at A1")
        elif placement == 1:
            print("You are at A2")
            if self.board[0][1] == 1:
                print("A yellow house for sale\nPrice: 100$ Rent: 50$")
            elif self.board[0][1] == 6:
                print("You are on your own house, do you want to sell?")
            elif self.board[0][1] == 5:
                print("You are at a blue house, time to pay")
                return 1
        elif placement == 2:
            print("You are at A3")
        elif placement == 3:
            print("You are at A4")
        elif placement == 4:
            print("You are at B4")
            if self.board[1][3] == 2:
                print("A purple house for sale\nPrice: 200$ Rent: 100$")
            elif self.board[1][3] == 6:
                print("You are on your own house, do you want to sell?")
            elif self.board[1][3] == 5:
                print("You are at a blue house, time to pay")
                return 1
        elif placement == 5:
            print("You are at C4")
        elif placement == 6:
            print("You are at D4")
        elif placement == 7:
            print("You are at D3")
        elif placement == 8:
            print("You are at D2")
            if self.board[3][1] == 3:
                print("A green house for sale\nPrice: 300$ Rent: 150$")
            elif self.board[3][1] == 6:
                print("You are on your own house, do you want to sell?")
            elif self.board[3][1] == 5:
                print("You are at a blue house, time to pay")
                return 1
        elif placement == 9:
            print("You are at D1")
        elif placement == 10:
            print("You are at C1")
        elif placement == 11:
            print("You are at B1")
            if self.board[1][0] == 4:
                print("A black house for sale\nPrice: 400$ Rent: 200$")
            elif self.board[1][0] == 6:
                print("You are on your own house, do you want to sell?")
            elif self.board[1][0] == 5:
                print("You are at a blue house, time to pay")
                return 1

    def check_owner_blue_player(self, position):
        if position == 1:
            if self.board[0][1] == 5:
                print("You already own this house")
            else:
                self.board[0][1] = 5
                return print("Congratulations you bought the yellow house")
        elif position == 4:
            if self.board[1][3] == 5:
                print("You already own this house")
            else:
                self.board[1][3] = 5
                return print("Congratulations you bought the purple house")
        elif position == 8:
            if self.board[3][1] == 5:
                print("You already own this house")
            else:
                self.board[3][1] = 5
                return print("Congratulations you bought the green house")
        elif position == 11:
            if self.board[1][0] == 5:
                print("You already own this house")
            else:
                self.board[1][0] = 5
                return print("Congratulations you bought the black house")
        elif position == 2 or 3 or 5 or 6 or 7 or 9 or 10:
            return print("No house to buy on this position")

    def check_owner_red_player(self, position):
        if position == 1:
            if self.board[0][1] == 6:
                print("You already own this house")
            else:
                self.board[0][1] = 6
                return print("Congratulations you bought the yellow house")
        elif position == 4:
            if self.board[1][3] == 6:
                print("You already own this house")
            else:
                self.board[1][3] = 6
                return print("Congratulations you bought the purple house")
        elif position == 8:
            if self.board[3][1] == 6:
                print("You already own this house")
            else:
                self.board[3][1] = 6
                return print("Congratulations you bought the green house")
        elif position == 11:
            if self.board[1][0] == 6:
                print("You already own this house")
            else:
                self.board[1][0] = 6
                return print("Congratulations you bought the black house")
        elif position == 2 or 3 or 5 or 6 or 7 or 9 or 10:
            return print("No house to buy on this position")

    def owner(self, position):
        if position == 1:
            if self.board[0][1] == 1:
                return "yes"
            elif self.board[0][1] == 5:
                return "blue"
            elif self.board[0][1] == 6:
                return "red"
        if position == 4:
            if self.board[1][3] == 2:
                return "yes"
            elif self.board[1][3] == 5:
                return "blue"
            elif self.board[1][3] == 6:
                return "red"
        elif position == 8:
            if self.board[3][1] == 3:
                return "yes"
            elif self.board[3][1] == 5:
                return "blue"
            elif self.board[3][1] == 6:
                return "red"
        elif position == 11:
            if self.board[1][0] == 4:
                return "yes"
            elif self.board[1][0] == 5:
                return "blue"
            elif self.board[1][0] == 6:
                return "red"
        else:
            return "yes"

    def sold_house(self, position):
        if position == 1:
            self.board[0][1] = 1
        elif position == 4:
            self.board[1][3] = 2
        elif position == 8:
            self.board[3][1] = 3
        elif position == 11:
            self.board[1][0] = 4
