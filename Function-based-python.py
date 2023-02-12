from random import randint
import os
import time


def tablero(a):#for printing the table
    print()
    print(str(a[0]) + " | " + str(a[1]) + " | " + str(a[2]))
    print("--------")
    print(str(a[3]) + " | " + str(a[4]) + " | " + str(a[5]))
    print("--------")
    print(str(a[6]) + " | " + str(a[7]) + " | " + str(a[8]))
    print()


def p1aldatu(a,name1):#for calling the table and asks a value to the user player 1

    print(str(name1) + "'s turn")
    print("Enter a number from 1 to 9")
    tablero(a)
    b = int(input())
    if a[b] == 0:
        a[b] = 'X'
    else:
        while b == a in range(0, 8):#repeats until valid input
            b = int(input("Select another number, the one you selected is already chosen:"))
        a[b]
    tablero(a)
    time.sleep(2)
    os.system("cls")#cleans console
    

def p2aldatu(a,name2):#for calling the table and asks a value to the user player 1
    
    print(str(name2) + "'s turn")
    print("Enter a number from 1 to 9")
    tablero(a)
    player= int(input())
    if a[player] == 0:
        a[player] = 'O'
    else:
        while b == a in range(0, 8):#repeats until valid input
            b = int(
                input("Select another number, the one you selected is already chosen:"))
        a[b]
    tablero(a)
    time.sleep(2)
    os.system("cls")#cleans console
    


def cpualdatu(a):#generates a pseudo random number and selects the cell
    print("cpu's Turn",end = "")
    b = 0
    while b <= 3:
        print(".",end="")
        time.sleep(1)
        b = b + 1
    cpu = randint(0, 8)#generate number
    while cpu == a in range(0, 8):#check if valid
        cpu = randint(0, 8)
    a[cpu] = 'O'#select the cell and change the value
    tablero(a)#prints the table

def TicTacToe():
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    b = 0
    c = 0
    print("What type of game do you want to play?")
    print("============================================================")
    print("1.-Single player")
    print("2.-Multiplayer")
    #asks if single player or multi, repeats until the user enters a valid value
    sing = int(input())
    if (sing != 1) and (sing != 2):
        while (sing != 1) and (sing != 2):
            sing = int(input("Not a valid input,Select a diferent option please")) 
    if sing == 1:#Single player mode
        z = 1
    elif sing == 2:#Multiplayer mode
        z = 2
    g = 1
    while g ==1:
        while c != 1:
            c = 2
            d = 1
            if sing == 1:#Executates this if the user chose Single player
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
            elif sing == 2:#Executates if user chose Multi player
                if z == 2:#asks for names
                    player1 = str(input("Enter player 1's name please:"))
                    player2 = str(input("Enter player 2's name please:"))
                    z = -1
                while d == 1:#funciton for table and selecting cell for the player 1
                    p1aldatu(a,player1)
                    d = 2
                    time.sleep(3)
                    os.system('cls')
                while d == 2:#funciton for table and selecting cell for the player 1
                    p2aldatu(a,player2)
                    d = 1
                    time.sleep(3)
                
                #checks if player 1 won
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
        #asks if the user wants to run the program again
        print("Do you want to repeat the program, YES/NO")
        l = str(input())
        l.lower()
        while l != "yes" or l != "no":
            l = str(input())
            l.lower()
        if l == "yes" :
            g = 1
        else :
            g = 0


a = 0
#Menu
print("MENU:")
print("=======================================")
print("1.-Rock,Paper,Scissors")
print("2.-Tic tac toe")
print("3.-Preguntados")

#asks for a value and selects the casters
a = int(input("Select an option please:"))

match a:
    case 2: TicTacToe()