from terminal_color import color_print
import random
from settings import in_game_settings


rules = " This is the board\n" \
        "      A2  A3\n" \
        "A1 ⬜  ⬜  ⬜  ⬜ A4\n" \
        "B1 ⬜  ⬜  ⬜  ⬜ B4\n" \
        "C1 ⬜  ⬜  ⬜  ⬜ C4\n" \
        "D1 ⬜  ⬜  ⬜  ⬜ D4\n" \
        "      D2  D3\n"


def visual_map(board):
    for row in board:
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


def player_1(player1, running, player1_place, money1):
    choice = input(f"{player1} what do you want to do? ")
    if choice.lower() == "quit":
        return "quit"
    elif choice.lower() == "rules":
        print(rules)
    elif choice.lower() == "money":
        print(money1)
    elif choice.lower() == "roll":
        dice = random.choice([1, 2, 3, 4, 5, 6])
        print(f"You rolled a {dice}")
        if player1_place + dice >= 12:
            money1 += 200
        in_game_settings(dice + player1_place)
        return dice
    elif choice.lower() != "quit" or "rules" or "roll":
        print("Cant do that")


def player_2(player2, running, player2_place, money2):
    choice = input(f"{player2} what do you want to do? ")
    if choice.lower() == "quit":
        return "quit"
    elif choice.lower() == "rules":
        print(rules)
    elif choice.lower() == "money":
        print(money2)
    elif choice.lower() == "roll":
        dice = random.choice([1, 2, 3, 4, 5, 6])
        print(f"You rolled a {dice}")
        if player2_place + dice >= 12:
            money2 += 200
        in_game_settings(dice + player2_place)
        return dice
    elif choice.lower() != "quit" or "rules" or "roll":
        print("Cant do that")


def main():
    board = [
        [0, 1, 0, 0],
        [4, 5, 5, 2],
        [0, 5, 5, 0],
        [0, 3, 0, 0]
    ]

    player1_place = 0
    player2_place = 0
    money1 = 400
    money2 = 400
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
        visual_map(board)
        if player_in_turn == 1:
            moving1 = player_1(player1, running, player1_place, money1)
            if type(moving1) == int:
                player1_place += moving1
                player_in_turn = 2
            elif type(moving1) == str:
                running = False
            else:
                player_in_turn = 1

        elif player_in_turn == 2:
            moving2 = player_2(player2, running, player2_place, money2)
            if type(moving2) == int:
                player2_place += moving2
                player_in_turn = 1
            elif type(moving2) == str:
                running = False
            else:
                player_in_turn = 2


if __name__ == '__main__':
    main()
