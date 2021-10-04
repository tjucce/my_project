from terminal_color import color_print
import random

rules = "   A1 A2 A3  A4\n   ⬜  ⬜  ⬜  ⬜\nB1 ⬜  ⬜  ⬜  ⬜ B4\nC1 ⬜  ⬜  ⬜  ⬜ C4\n   ⬜  ⬜  ⬜  ⬜\n   D1 D2 D3  D4"


def main():
    the_map = [
        [0, 0, 1, 0],
        [1, 3, 3, 0],
        [2, 3, 3, 1],
        [0, 0, 2, 0]
    ]
    print(rules)
    running = True
    while running:
        for row in the_map:
            for cell in row:
                color = "white"
                if cell == 1:
                    color = "red"
                elif cell == 2:
                    color = "blue"
                elif cell == 3:
                    color = "black"
                color_print(color, "⬜", end=" ")
            print()
        print(random.choice([1, 2, 3, 4, 5, 6]))
        move = input()


if __name__ == '__main__':
    main()
