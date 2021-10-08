from terminal_color import color_print
import random
from settings import in_game_settings


rules = " This is the map\n" \
        "      A2  A3\n" \
        "A1 ⬜  ⬜  ⬜  ⬜ A4\n" \
        "B1 ⬜  ⬜  ⬜  ⬜ B4\n" \
        "C1 ⬜  ⬜  ⬜  ⬜ C4\n" \
        "D1 ⬜  ⬜  ⬜  ⬜ D4\n" \
        "      D2  D3\n"


def player_1(player1, running, player1_place):
    choice = input(f"{player1} what do you want to do? ")
    if choice.lower() == "quit":
        running = False
    elif choice.lower() == "rules":
        print(rules)
    elif choice.lower() == "roll":
        dice = random.choice([1, 2, 3, 4, 5, 6])
        print(f"You rolled a {dice}")
        move1 = in_game_settings(dice + player1_place)
        return dice


def player_2(player2, running, player2_place):
    choice = input(f"{player2} what do you want to do? ")
    if choice.lower() == "quit":
        running = False
    elif choice.lower() == "rules":
        print(rules)
    elif choice.lower() == "roll":
        dice = random.choice([1, 2, 3, 4, 5, 6])
        print(f"You rolled a {dice}")
        move2 = in_game_settings(dice + player2_place)
        return dice


def main():
    the_map = [
        [0, 1, 0, 0],
        [4, 5, 5, 2],
        [0, 5, 5, 0],
        [0, 3, 0, 0]
    ]

    player1_place = 0
    player2_place = 0
    player_in_turn = 1
    running = True
    print(rules)
    game = input("Do you want to play monopoly? ")

    if game.lower() == "no":
        running = False
    else:
        player1 = input("Player1 what is your name? ")
        player2 = input("Player2 what is your name? ")
        while running:
            for row in the_map:
                for cell in row:
                    color = "white"
                    if cell == 1:
                        color = "yellow"
                    elif cell == 2:
                        color = "red"
                    elif cell == 3:
                        color = "green"
                    elif cell == 4:
                        color = "blue"
                    elif cell == 5:
                        color = "black"
                    color_print(color, "⬜", end=" ")
                print()

            if player_in_turn == 1:
                moving1 = player_1(player1, running, player1_place)
                player1_place += moving1
                player_in_turn = 2

            elif player_in_turn == 2:
                moving2 = player_2(player2, running, player2_place)
                player2_place += moving2
                player_in_turn = 1


if __name__ == '__main__':
    main()
