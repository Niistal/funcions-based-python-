from random import randint
import os
import time


def tablero(a):
    print(str(a[0]) + " |" + str(a[1]) + "|" + str(a[2]))
    print("--------")
    print(str(a[3]) + " |" + str(a[4]) + "|" + str(a[5]))
    print("--------")
    print(str(a[6]) + " |" + str(a[7]) + "|" + str(a[8]))


def p1aldatu(a):
    tablero(a)
    player = int(input("Enter a number from 1 to 9"))
    if a[player] == 0:
        a[player] = 'X'
    else:
        while b == a in range(0, 8):
            b = int(
                input("Select another number, the one you selected is already chosen:"))
        a[b]

def p2aldatu(a):
    tablero(a)
    player = int(input("Enter a number from 1 to 9"))
    if a[player] == 0:
        a[player] = 'O'
    else:
        while b == a in range(0, 8):
            b = int(
                input("Select another number, the one you selected is already chosen:"))
        a[b]


def cpualdatu(a):
    print("cpu's Turn")
    while b < 3:
        print(".")
        time.sleep(1)
        b = + 1
    while cpu != a in range(0, 8):
        cpu = randint(0, 8)
    a[cpu] = 'O'
    tablero(a)


def RockPaperScissors():
    # create a list of play options
    t = ["Rock", "Paper", "Scissors"]
    score1 = 0
    score2 = 0
    # assign a random play to the computer
    computer = t[randint(0, 2)]

    # set player to False
    player = False

    while player == False:
        # set player to True
        player = input("Rock, Paper, Scissors?")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                score2+1
                print("You lose!", computer, "covers", player)
                print(score1, "-", score2)
            else:
                score1+1
                print("You win!", player, "smashes", computer)
                print(score1, "-", score2)
        elif player == "Paper":
            if computer == "Scissors":
                score2+1
                print("You lose!", computer, "cut", player)
                print(score1, "-", score2)
            else:
                score1+1
                print("You win!", player, "covers", computer)
                print(score1, "-", score2)
        elif player == "Scissors":
            if computer == "Rock":
                score2+1
                print("You lose...", computer, "smashes", player)
                print(score1, "-", score2)
            else:
                score1+1
                print("You win!", player, "cut", computer)
                print(score1, "-", score2)
        else:
            print("That's not a valid play. Check your spelling!")
        # player was set to True, but we want it to be False so the loop continues
        player = False
        computer = t[randint(0, 2)]


def TicTacToe():
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    b = 0
    c = 0
    print("What type of game do you want to play?")
    print("============================================================")
    print("1.-Single player")
    print("2.-Multiplayer")

    while sing != 1 or sing != 2:
        sing = int(input())

    while c != 1:
        d = 1
        if sing == 1:
            player1 = str(input("Enter your name please:"))
            while d == 1:
                p1aldatu(a)
                d = 2
                time.sleep(3)
                os.system('cls')
            while d == 2:
                cpualdatu(a)
                d = 1
            os.system('cls')
            # check for player

            if a[0] == 'X' and a[1] == 'X' and a[2] == 'X':
                print(player1 + "wins")
                c = 1
            elif a[0] == 'X' and a[3] == 'X' and a[6] == 'X':
                print(player1 + "wins")
                c = 1
            elif a[0] == 'X' and a[4] == 'X' and a[8] == 'X':
                print(player1 + "wins")
                c = 1
            elif a[6] == 'X' and a[4] == 'X' and a[2] == 'X':
                print(player1 + "wins")
                c = 1
            elif a[3] == 'X' and a[4] == 'X' and a[5] == 'X':
                print(player1 + "wins")
                c = 1
            elif a[6] == 'X' and a[7] == 'X' and a[8] == 'X':
                print(player1 + "wins")
                c = 1
            elif a[7] == 'X' and a[4] == 'X' and a[1] == 'X':
                print(player1 + "wins")
                c = 1
            elif a[8] == 'X' and a[4] == 'X' and a[2] == 'X':
                print(player1 + "wins")
                c = 1

                # check for cpu
            if a[0] == 'O' and a[1] == 'O' and a[2] == 'O':
                print("cpu wins")
                c = 1
            elif a[0] == 'O' and a[3] == 'O' and a[6] == 'O':
                print("cpu wins")
                c = 1
            elif a[0] == 'O' and a[4] == 'O' and a[8] == 'O':
                print("cpu wins")
                c = 1
            elif a[6] == 'O' and a[4] == 'O' and a[2] == 'O':
                print("cpu wins")
                c = 1
            elif a[3] == 'O' and a[4] == 'O' and a[5] == 'O':
                print("cpu wins")
                c = 1
            elif a[6] == 'O' and a[7] == 'O' and a[8] == 'O':
                print("cpu wins")
                c = 1
            elif a[7] == 'O' and a[4] == 'O' and a[1] == 'O':
                print("cpu wins")
                c = 1
            elif a[8] == 'O' and a[4] == 'O' and a[2] == 'O':
                print("cpu wins")
                c = 1
        elif sing == 2:
            player1 = str(input("Enter player 1's name please:"))
            player2 = str(input("Enter player 2's name please:"))
            while d == 1:
                p1aldatu(a)
                d = 2
                time.sleep(3)
                os.system('cls')
            while d == 2:
                p2aldatu(a)
                d = 1
                time.sleep(3)
            
            if a[0] == 'X' and a[1] == 'X' and a[2] == 'X':
                print(player1 + "wins")
                c = 1
            elif a[0] == 'X' and a[3] == 'X' and a[6] == 'X':
                print(player1 + "wins")
                c = 1
            elif a[0] == 'X' and a[4] == 'X' and a[8] == 'X':
                print(player1 + "wins")
                c = 1
            elif a[6] == 'X' and a[4] == 'X' and a[2] == 'X':
                print(player1 + "wins")
                c = 1
            elif a[3] == 'X' and a[4] == 'X' and a[5] == 'X':
                print(player1 + "wins")
                c = 1
            elif a[6] == 'X' and a[7] == 'X' and a[8] == 'X':
                print(player1 + "wins")
                c = 1
            elif a[7] == 'X' and a[4] == 'X' and a[1] == 'X':
                print(player1 + "wins")
                c = 1
            elif a[8] == 'X' and a[4] == 'X' and a[2] == 'X':
                print(player1 + "wins")
                c = 1

                # check for player 2
            if a[0] == 'O' and a[1] == 'O' and a[2] == 'O':
                print(player2 + "wins")
                c = 1
            elif a[0] == 'O' and a[3] == 'O' and a[6] == 'O':
                print(player2 + "wins")
                c = 1
            elif a[0] == 'O' and a[4] == 'O' and a[8] == 'O':
                print(player2 + "wins")
                c = 1
            elif a[6] == 'O' and a[4] == 'O' and a[2] == 'O':
                print(player2 + "wins")
                c = 1
            elif a[3] == 'O' and a[4] == 'O' and a[5] == 'O':
                print(player2 + "wins")
                c = 1
            elif a[6] == 'O' and a[7] == 'O' and a[8] == 'O':
                print(player2 + "wins")
                c = 1
            elif a[7] == 'O' and a[4] == 'O' and a[1] == 'O':
                print(player2 + "wins")
                c = 1
            elif a[8] == 'O' and a[4] == 'O' and a[2] == 'O':
                print(player2 + "wins")
                c = 1


a = 0
print("MENU:")
print("=======================================")
print("1.-Rock,Paper,Scissors")
print("2.-Tic tac toe")
print("3.-Preguntados")

a = int(input("Select an option please:"))

match a:
    case 1: RockPaperScissors()
    case 2: TicTacToe()
    #case 3: Preguntados()
