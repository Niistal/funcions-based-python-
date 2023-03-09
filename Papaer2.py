from random import randint


t = ["Rock", "Paper", "Scissors", "Exit"]
score1 = 0
score2 = 0

computer = t[randint(0, 2)]

# set player to False
player = False
jugador = input(str("What is your name?"))
while not player:

    # set player to True
    #f = open("testua.txt", "w+")

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
            print("The winner is",jugador)
            #f.write("The winner is",jugador)
            #f.write("\n")
        elif score1 == score2:
            print("There is a tie")
            print("There is a tie between",jugador,"and the rival")
        elif score2 > score1:
            print("Sorry...",jugador,"has lost")
        player = True
        exit()
        #f.close()
    else:
        print("That's not a valid play. Check your spelling!")
    # player was set to True, but we want it to be False so the loop continues

    player = False
    computer = t[randint(0, 2)]