from terminal_color import color_print


class Board:
    def __init__(self):
        self.board = [
                [0, 1, 0, 0],
                [4, 0, 0, 2],
                [0, 0, 0, 0],
                [0, 3, 0, 0]
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
                color_print(color, "⬜", end=" ")
            print()
