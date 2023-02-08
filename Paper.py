from random import randint
import os
import time



def RockPaperScissors():
    #create a list of play options
    t = ["Rock", "Paper", "Scissors"]
    score1=0
    score2=0
    #assign a random play to the computer
    computer = t[randint(0,2)]

    #set player to False
    player = False

    while player == False:
    #set player to True
        player = input("Rock, Paper, Scissors?")
        if player == computer:
            print("Tie!")
        elif player == "Rock":
            if computer == "Paper":
                score2+1
                print("You lose!", computer, "covers", player)
                print(score1,"-",score2)
            else:
                score1+1
                print("You win!", player, "smashes", computer)
                print(score1,"-",score2)
        elif player == "Paper":
            if computer == "Scissors":
                score2+1
                print("You lose!", computer, "cut", player)
                print(score1,"-",score2)
            else:
                score1+1
                print("You win!", player, "covers", computer)
                print(score1,"-",score2)
        elif player == "Scissors":
            if computer == "Rock":
                score2+1
                print("You lose...", computer, "smashes", player)
                print(score1,"-",score2)
            else:
                score1+1
                print("You win!", player, "cut", computer)
                print(score1,"-",score2)
        else:
            print("That's not a valid play. Check your spelling!")
        #player was set to True, but we want it to be False so the loop continues
        player = False
        computer = t[randint(0,2)]

def TicTacToe():
    cpu = 0
    player = 0
    a = [0,0,0,0,0,0,0,0,0]
    b = 0
    while c != 1:
        while d == 1:
            tablero(a)
            player = int(input("Enter a number from 1 to 9"))
            a[player] = 'X'
            d = 2
            os.system('cls')
        while d == 2:
            print("cpu's Turn")
            while b < 3:
                print(".")
                time.sleep(1)
                b + 1
            while cpu == a in range(0,8):
                cpu = randint(0,8)
                a[cpu] = 'O'
            tablero(a)
            d = 1
            os.system('cls')
        #check for player
        if a[0] == 'X' and  a[1] == 'X' and  a[2] == 'X':
            print("Player wins")
            c = 1
        elif a[0] == 'X' and  a[3] == 'X' and  a[6] == 'X':
            print("Player wins")
            c = 1
        elif a[0] == 'X' and  a[4] == 'X' and  a[8] == 'X':
            print("Player wins")
            c = 1
        elif a[6] == 'X' and  a[4] == 'X' and  a[2] == 'X':
            print("Player wins")
            c = 1
        elif a[3] == 'X' and  a[4] == 'X' and  a[5] == 'X':
            print("Player wins")
            c = 1
        elif a[6] == 'X' and  a[7] == 'X' and  a[8] == 'X':
            print("Player wins")
            c = 1
        elif a[7] == 'X' and  a[4] == 'X' and  a[1] == 'X':
            print("Player wins")
            c = 1
        elif a[8] == 'X' and  a[4] == 'X' and  a[2] == 'X':
            print("Player wins")
            c = 1


        #check for cpu
        if a[0] == 'O' and  a[1] == 'O' and  a[2] == 'O':
            print("cpu wins")
            c = 1
        elif a[0] == 'O' and  a[3] == 'O' and  a[6] == 'O':
            print("cpu wins")
            c = 1
        elif a[0] == 'O' and  a[4] == 'O' and  a[8] == 'O':
            print("cpu wins")
            c = 1
        elif a[6] == 'O' and  a[4] == 'O' and  a[2] == 'O':
            print("cpu wins")
            c = 1
        elif a[3] == 'O' and  a[4] == 'O' and  a[5] == 'O':
            print("cpu wins")
            c = 1
        elif a[6] == 'O' and  a[7] == 'O' and  a[8] == 'O':
            print("cpu wins")
            c = 1
        elif a[7] == 'O' and  a[4] == 'O' and  a[1] == 'O':
            print("cpu wins")
            c = 1
        elif a[8] == 'O' and  a[4] == 'O' and  a[2] == 'O':
            print("cpu wins")
            c = 1

def tablero(a):
    print(a[0] + " |")
    print(a[1] + "|")
    print(a[2])
    print("--------")
    print(a[3] + " |")
    print(a[4] + "|")
    print(a[5])
    print("--------")
    print(a[6] + " |")
    print(a[7] + "|")
    print(a[8])
    
a = 0   
print("MENU:")
print("=======================================")
print("1.-Rock,Paper,Scissors")
print("2.-Tic tac toe")
print("3.-Preguntados")

match a:
    case 1:RockPaperScissors()
    case 2:TicTacToe()