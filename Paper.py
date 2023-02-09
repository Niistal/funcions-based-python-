from random import randint
import os
import time


def tablero(a):
    print()
    print(str(a[0]) + " | " + str(a[1]) + " | " + str(a[2]))
    print("--------")
    print(str(a[3]) + " | " + str(a[4]) + " | " + str(a[5]))
    print("--------")
    print(str(a[6]) + " | " + str(a[7]) + " | " + str(a[8]))
    print()


def p1aldatu(a,name1):

    print(str(name1) + "'s turn")
    print("Enter a number from 1 to 9")
    tablero(a)
    b = int(input())
    if a[b] == 0:
        a[b] = 'X'
    else:
        while b == a in range(0, 8):
            b = int(input("Select another number, the one you selected is already chosen:"))
        a[b]
    tablero(a)
    time.sleep(2)
    os.system("cls")
    

def p2aldatu(a,name2):
    
    print(str(name2) + "'s turn")
    print("Enter a number from 1 to 9")
    tablero(a)
    player= int(input())
    if a[player] == 0:
        a[player] = 'O'
    else:
        while b == a in range(0, 8):
            b = int(
                input("Select another number, the one you selected is already chosen:"))
        a[b]
    tablero(a)
    time.sleep(2)
    os.system("cls")


def cpualdatu(a):
    print("cpu's Turn",end = "")
    b = 0
    while b <= 3:
        print(".",end="")
        time.sleep(1)
        b = b + 1
    cpu = randint(0, 8)
    while cpu == a in range(0, 8):
        cpu = randint(0, 8)
    a[cpu] = 'O'
    tablero(a)


def RockPaperScissors():
     from random import randint

t = ["Rock", "Paper", "Scissors", "Exit"]
score1 = 0
score2 = 0

computer = t[randint(0, 2)]

# set player to False
player = False

while not player:

    # set player to True
    player = input("Rock, Paper, Scissors, Exit?")
    if player == computer:
        print("Tie!")
        print(score1, "-", score2)
    elif player == "Rock":
        if computer == "Paper":
            score2 += 1
            print("You lose!", computer, "covers", player)
            print(score1, "-", score2)
        else:
            score1 += 1
            print("You win!", player, "smashes", computer)
            print(score1, "-", score2)
    elif player == "Paper":
        if computer == "Scissors":
            score2 += 1
            print("You lose!", computer, "cut", player)
            print(score1, "-", score2)
        else:
            score1 += 1
            print("You win!", player, "covers", computer)
            print(score1, "-", score2)
    elif player == "Scissors":
        if computer == "Rock":
            score2 += 1
            print("You lose...", computer, "smashes", player)
            print(score1, "-", score2)
        else:
            score1 += 1
            print("You win!", player, "cut", computer)
            print(score1, "-", score2)
    elif player == "Exit":
        print("The final score is", score1, "-", score2)
        if score1 > score2:
            print("You win")
        elif score1 == score2:
            print("There is a tie")
        elif score2 > score1:
            print("Sorry...You lost")
        player = True
        exit()

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
    sing = int(input())
    if (sing != 1) and (sing != 2):
        while (sing != 1) and (sing != 2):
            sing = int(input("Not a valid input,Select a diferent option please")) 
    if sing == 1:
        z = 1
    elif sing == 2:
        z = 2

    while c != 1:
        d = 1
        if sing == 1:
            if z == 1:
                player1 = str(input("Enter your name please:"))
                z = -1
            while d == 1:
                p1aldatu(a,player1)
                d = 2
                time.sleep(1)
            while d == 2:
                cpualdatu(a)
                d = 1
            # check for player

            if a[0] == 'X' and a[1] == 'X' and a[2] == 'X':
                print(player1 + " wins")
                c = 1
            elif a[0] == 'X' and a[3] == 'X' and a[6] == 'X':
                print(player1 + " wins")
                c = 1
            elif a[0] == 'X' and a[4] == 'X' and a[8] == 'X':
                print(player1 + " wins")
                c = 1
            elif a[6] == 'X' and a[4] == 'X' and a[2] == 'X':
                print(player1 + " wins")
                c = 1
            elif a[3] == 'X' and a[4] == 'X' and a[5] == 'X':
                print(player1 + " wins")
                c = 1
            elif a[6] == 'X' and a[7] == 'X' and a[8] == 'X':
                print(player1 + " wins")
                c = 1
            elif a[7] == 'X' and a[4] == 'X' and a[1] == 'X':
                print(player1 + " wins")
                c = 1
            elif a[8] == 'X' and a[4] == 'X' and a[2] == 'X':
                print(player1 + " wins")
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
            if z == 2:
                player1 = str(input("Enter player 1's name please:"))
                player2 = str(input("Enter player 2's name please:"))
                z = -1
            while d == 1:
                p1aldatu(a,player1)
                d = 2
                time.sleep(3)
                os.system('cls')
            while d == 2:
                p2aldatu(a,player2)
                d = 1
                time.sleep(3)
            
            if a[0] == 'X' and a[1] == 'X' and a[2] == 'X':
                print(player1 + " wins")
                c = 1
            elif a[0] == 'X' and a[3] == 'X' and a[6] == 'X':
                print(player1 + " wins")
                c = 1
            elif a[0] == 'X' and a[4] == 'X' and a[8] == 'X':
                print(player1 + " wins")
                c = 1
            elif a[6] == 'X' and a[4] == 'X' and a[2] == 'X':
                print(player1 + " wins")
                c = 1
            elif a[3] == 'X' and a[4] == 'X' and a[5] == 'X':
                print(player1 + " wins")
                c = 1
            elif a[6] == 'X' and a[7] == 'X' and a[8] == 'X':
                print(player1 + " wins")
                c = 1
            elif a[7] == 'X' and a[4] == 'X' and a[1] == 'X':
                print(player1 + " wins")
                c = 1
            elif a[8] == 'X' and a[4] == 'X' and a[2] == 'X':
                print(player1 + " wins")
                c = 1

                # check for player 2
            if a[0] == 'O' and a[1] == 'O' and a[2] == 'O':
                print(player2 + " wins")
                c = 1
            elif a[0] == 'O' and a[3] == 'O' and a[6] == 'O':
                print(player2 + " wins")
                c = 1
            elif a[0] == 'O' and a[4] == 'O' and a[8] == 'O':
                print(player2 + " wins")
                c = 1
            elif a[6] == 'O' and a[4] == 'O' and a[2] == 'O':
                print(player2 + " wins")
                c = 1
            elif a[3] == 'O' and a[4] == 'O' and a[5] == 'O':
                print(player2 + " wins")
                c = 1
            elif a[6] == 'O' and a[7] == 'O' and a[8] == 'O':
                print(player2 + " wins")
                c = 1
            elif a[7] == 'O' and a[4] == 'O' and a[1] == 'O':
                print(player2 + " wins")
                c = 1
            elif a[8] == 'O' and a[4] == 'O' and a[2] == 'O':
                print(player2 + " wins")
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
