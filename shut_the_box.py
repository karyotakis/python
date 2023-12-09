import random
from itertools import combinations
import os
import time

# globals
start_board = {1, 2, 3, 4, 5, 6, 7, 8, 9}
choices = set()


# functions
def roll_dice():
    res1 = random.randrange(1, 7)
    res2 = random.randrange(1, 7)
    return res1, res2


def sum_exists(L, number):
    for i in range(1, len(L) + 1):
        answer = number in (map(sum, combinations(L, i)))
        if answer:
            return answer
    return False


def input_choice():
    while True:
        data = input(" enter number value or (d) delete chosen numbers: ").strip()
        if data.isdigit() or data == "d":
            
            return data
        else:
            print(" Only digits or (d) please. ")


def main():
    play = True
    while play:
        rounds = 1
        board = start_board.copy()
        while True:
            clear = lambda: os.system('cls') # on windows
            # clear = lambda: os.system('clear') # on linux
            clear()
            time.sleep(1)

            # view board
            print("\n" + "  " * 15 + " ROUND: " + str(rounds) )
            print( "  " * 15 +   "~~~~~~~~~~" )
            print(f" BOARD:  {sorted(list(board))}")

            # check if only one dice
            dice1, dice2 = roll_dice()
            if len(board) == 1 and sum(board) <= 6:  # play with one dice
                dice_sum = dice1
                print(f" roll dice = {dice_sum}")
            else:
                dice_sum = dice1 + dice2
                print(f" roll dice = {dice1} + {dice2} ")

            # check if roll dice sum exists in board
            if not sum_exists(list(board), dice_sum):
                # check win
                if sum(board) == 0:
                    print(" - SHUT THE BOX -!!!", end=" ")
                else:
                    print(" You lost !!! " + "SCORE=" + str(sum(board)))
                print(" GAME OVER !!!")
                print("*" * 30)
                break
            print("-" * 67)

            while sum(choices) != dice_sum:
                print(f" CHOICE: {list(choices)} sum choices: {str(sum(choices))}")

                choice = input_choice()

                if choice == "d":
                    print("-" * 67)
                    choices.clear()
                    continue

                choices.add(int(choice))

                # check all ok
                if sum(choices) == dice_sum:
                    # delete from board the chosen numbers
                    board = board - choices
                    choices.clear()
                    break

            rounds += 1
        again = str(input(" Type 'no' to quit : "))
        if again == "no":
            play = False


main()
