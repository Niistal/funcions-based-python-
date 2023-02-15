from random import randint
import os
import time
import random


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


def RockPaperScissors():

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


def Preguntadosbutrandomized():
    topics =["Art", "History", "Sports", "Entertainment", "Geography"]
    qart= ["Who painted the Mona Lisa?", "Who painted the last dinner?", "What city is depicted in Van Gogh's The Starry Night?"]
    aart=["da vinci","da vinci", "saint-remy"]
    qentertainment= ["Who is the main character in the pokemon series?", "What is the most famous technique of goku from dragon ball?","What is the name of the film that toys have sense of life?"]
    aentertainment=["ash", "kamehameha", "toy story"]
    qhistory = ["¿Who discovered America?", " ¿In which year finished World War 2", "¿In which country was born Hitler?"]
    ahistory =["cristobal colon", "1945", "austria"]
    qsport = ["¿which country won the world cup in 2022? ", "¿who is the the player who scored more points in the NBA?", "¿Who is the fastest athlete in the history?"]
    asport= ["argentina", "lebron james", "usain bolt"]
    qgeography = ["¿which is the country with the highest population?", "¿which is the highest mountain in the world?", "which is the capital of the USA "]
    ageography = ["tokio","everest","washington"]
    name = str(input("Enter your name please:"))
    score=0
    print("Hello" + name + "today you are gonna play a little quiz and you can't choose anything,you will only answer to five questions that are chosen randomly (the answers must be in lowercase)")
    print("Are you readyyyyyy?")
    count=0
    while count <=5:
        num = 3
        if count == 0:
            print("and the topic is",end="")
            for i in range(1, num + 1):
                print("." ,end="")
        a = int(randint(0,5))
        print(topics[a])
        print("And the question is...",end="")
        if a == 1:
            a = random.randint(0,3)
            print(qart[a])
            answer = str(input("Enter the answer:"))
            answer.lower()
            if answer == aart[a].lower():
                print("You are right")
                score+1
                count+1
            else:
                print("wrongggggg")
                count+1
        elif a ==2:
            a = random.randint(0, 3)
            print(qhistory[a])
            answer = str(input("Enter the answer:"))
            answer.lower()
            if answer == ahistory[a].lower():
                print("You are right")
                score+1
                count+1
            else:
                print("wrongggggg")
                count+1
        elif a ==3:
            a = random.randint(0, 3)
            print(qsport[a])
            answer = str(input("Enter the answer:"))
            answer.lower()
            if answer == asport[a].lower():
                print("You are right")
                score + 1
                count + 1
            else:
                print("wrongggggg")
                count + 1
        elif a == 4:
            a = random.randint(0, 3)
            print(qentertainment[a])
            answer = str(input("Enter the answer:"))
            answer.lower()
            if answer == aentertainment[a].lower():
                print("You are right")
                score + 1
                count + 1
            else:
                print("wrongggggg")
                count + 1
        elif a == 5:
            a = random.randint(0, 3)
            print(qgeography[a])
            answer = str(input("Enter the answer:"))
            answer.lower()
            if answer == ageography[a].lower():
                print("You are right")
                score + 1
                count + 1
            else:
                print("wrongggggg")
                count + 1
    print("You answered" + score + "correctly")

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
    case 1: RockPaperScissors()
    case 2: TicTacToe()
    case 3: 
        q = int(input("Do you want randomized questions or normal cuestions"))
        if q == 1:
            Preguntadosbutrandomized()
        elif q == 2:
            #normalpreguntados()
            pass
        else:
            print("Not a valid number")
        


