import random


"""
A simple multiplayer Tic Tac Toe game,
using Python.
This software is available under GPL license.
Author: Shahibur Rahaman
Year: 2020
Month: November
License: GNU GENERAL PUBLIC LICENSE (GPL v3.0)
"""

version = "2.6.10.20"

print("|---------------|")
print("|----Welcome----|")
print("|-------to------|")
print("|--Tic-Tac-Toe--|")
print("|_______________|\n")
print("Developed by -> Shahibur Rahaman")
print('')
print("Version", version)
print('')


def matrix():  # Declaring a function as the map of the game.
    print("---------\n"
          '|', cells[0], cells[1], cells[2], '|\n' +
          '|', cells[3], cells[4], cells[5], '|\n' +
          '|', cells[6], cells[7], cells[8], '|\n' +
          "---------\n")


while True:
    x_score = 0
    o_score = 0

    while True:
        try:
            rounds = int(input("How many rounds you want to play?: "))
            break
        except ValueError:
            print("\nPlease enter only numerical values!\n")
            continue
    
    choice = ["O", "X"]
    turn = random.choice(choice)

    for i in range(rounds):
        print("")
        print("{-> Round", i + 1, "<-}")
        print("")

        print("Current Map:")  # Setting up the default blank map.
        cells = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

        matrix()

        for k in range(9):  # Running the loop for maximum possibilities
            empty_count = 0
            x_wins = False
            o_wins = False

            # Switching the turn of the players.
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            print("|->", turn + "'s", "turn <-|")

            # Taking the position input from the user with error handling.
            while True:
                try:
                    usr = int(input("Enter the position (1-9): "))
                    if usr > 9:
                        print("")
                        print("Please enter values between 1-9!\n")
                        continue
                    elif cells[usr - 1] != '_':
                        print("")
                        print("|-> This position is already occupied! <-|\n")
                        continue
                except ValueError:
                    print("")
                    print("Please enter only numerical values!\n")
                else:
                    break

            cells[usr - 1] = turn

            for cell in cells:
                if cell == "_":
                    empty_count += 1

            #Setting up all of the winning situations.

            hor1 = cells[0] + cells[1] + cells[2]
            hor2 = cells[3] + cells[4] + cells[5]
            hor3 = cells[6] + cells[7] + cells[8]

            ver1 = cells[0] + cells[3] + cells[6]
            ver2 = cells[1] + cells[4] + cells[7]
            ver3 = cells[2] + cells[5] + cells[8]

            dia1 = cells[0] + cells[4] + cells[8]
            dia2 = cells[2] + cells[4] + cells[6]

            wins = [hor1, hor2, hor3, ver1, ver2, ver3, dia1, dia2]

            matrix()  # Calling out the map function.

            if "XXX" in wins:
                x_wins = True
            if "OOO" in wins:
                o_wins = True

            if x_wins:
                x_score += 1
                print("|-> X is the winner of Round", str(i + 1) + "! <-|\n")
                break

            elif o_wins:
                o_score += 1
                print("|-> O is the winner of Round", str(i + 1) + "! <-|\n")
                break

            elif empty_count == 0:
                print("|-> Draw! <-|\n")

        print("----------X" * 4)
        print("")
    print("____________________________________________")
    print("                FINAL SCORES")
    print("____________________________________________")
    print("      Player X       |      Player O")
    print("|>       ", x_score, "         |        ", o_score, "         <|")
    print("--------------------------------------------\n")

    if o_score > x_score:
        print("|============= O Won the match ============|\n")
    elif x_score > o_score:
        print("|============= X Won the match ============|\n")
    else:
        print("|=============== Draw match ===============|\n")

    NG = input("\nDo you want to play another match [y/n]: ")
    print("")
    if NG == "y" or NG == "Y":
        pass
    else:
        print("Exiting now...")
        break
