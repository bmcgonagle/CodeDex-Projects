#Brady McGonagle
# 11 / 5 / 24
#Rock Paper Scissors Game

import random

def play():
    score_player = 0
    score_computer = 0
    while True:
        player = int(input("===================\nRock Paper Scissors\n=================== \n 1. Rock (✊) \n 2. Paper (✋) \n 3. Scissors (✌) \n"))
        computer = random.randint(1, 3)
        # Map numbers to symbols
        choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
        print("+++++++++++++++++++++++++++++++")
        print("The computer choose: " + choices[computer])

        if player == computer:
            print("You both threw " + choices[computer] + ". Please try again")
        elif player == 1 and computer == 2:
            score_computer += 1
            print("computer has won. The score is now - \n Player: " + str(score_player)  + "\n Computer: " + str(score_computer))
        elif player == 1 and computer == 3:
            score_player += 1
            print("player has won. The score is now - \n Player: " + str(score_player)  + "\n Computer: " + str(score_computer))
        elif player == 2 and computer == 1:
            score_player += 1
            print("player has won. The score is now - \n Player: " + str(score_player)  + "\n Computer: " + str(score_computer))
        elif player == 2 and computer == 3:
            score_computer += 1
            print("computer has won. The score is now - \n Player: " + str(score_player)  + "\n Computer: " + str(score_computer))
        elif player == 3 and computer == 1:
            score_computer += 1
            print("computer has won. The score is now - \n Player: " + str(score_player)  + "\n Computer: " + str(score_computer))
        elif player == 3 and computer == 2:
            score_player += 1
            print("player has won. The score is now - \n Player: " + str(score_player)  + "\n Computer: " + str(score_computer))

print(play())
