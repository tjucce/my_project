from terminal_color import color_print
import random

rules = " This is the map\n" \
        "      A2  A3\n" \
        "A1 ⬜  ⬜  ⬜  ⬜ A4\n" \
        "B1 ⬜  ⬜  ⬜  ⬜ B4\n" \
        "C1 ⬜  ⬜  ⬜  ⬜ C4\n" \
        "D1 ⬜  ⬜  ⬜  ⬜ D4\n" \
        "      D2  D3\n"


def main():
    the_map = [
        [0, 0, 1, 0],
        [1, 3, 3, 0],
        [2, 3, 3, 1],
        [0, 0, 2, 0]
    ]
    player_in_turn = 1
    print(rules)
    game = input("Do you want to play monopoly? ")

    if game.lower() == "no":
        running = False
    else:
        running = True
        player1 = input("Player1 what is your name? ")
        player2 = input("Player2 what is your name? ")
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

            if player_in_turn == 1:
                choice = input(f"{player1} what do you want to do? ")
                if choice.lower() == "quit":
                    running = False
                elif choice.lower() == "rules":
                    print(rules)
                else:
                    player_in_turn = 2

            elif player_in_turn == 2:
                choice = input(f"{player2} what do you want to do? ")
                if choice.lower() == "quit":
                    running = False
                elif choice.lower() == "rules":
                    print(rules)
                else:
                    player_in_turn = 1



if __name__ == '__main__':
    main()
