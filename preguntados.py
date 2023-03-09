import random




def history():
    qhist = ["¿Who discovered America?", " ¿In which year finished World War 2", "¿In which country was born Hitler?"]
    ahist = ["Cristobal Colon", "1945", "Austria"]

    a = random.randrange(0, 3)

    if a == 1:
        preg = "¿Who discovered America?"
        print(preg)
        erantzuna = input()

        if erantzuna.lower() == "cristobal colon":
            print("the answer is Correct")
            score + 1
        else:
            print("the answer is incorrect")

    if a == 2:
        preg = "¿In which year finished World War 2"
        print(preg)
        erantzuna = input()

        if erantzuna.lower() == "1945":
            print("the answer is Correct")
            score + 1
        else:
            print("the answer is incorrect")

    if a == 3:
        preg = "¿In which country was born Hitler?"
        print(preg)
        erantzuna = input()

        if erantzuna.lower() == "austria":
            print("the answer is Correct")
            score + 1
        else:
            print("the answer is incorrect")


def sport():
    qspor = ["¿which country won the world cup in 2022? ", "¿who is the the player who scored more points in the NBA?",
             "¿Who is the fastest athlete in the history?"]
    aspor = ["Argentina", "Lebron James", "Usain Bolt"]

    a = random.randrange(0, 3)
    if a == 1:
        preg = "¿which country won the world cup in 2022? "
        print(preg)
        erantzuna = input()

        if erantzuna.lower() == "argentina":
            print("the answer is Correct")
            score + 1
        else:
            print("the answer is incorrect")

    if a == 2:
        preg = "¿who is the the player who scored more points in the NBA?"
        print(preg)
        erantzuna = input()

        if erantzuna.lower() == "lebron james":
            print("the answer is Correct")
            score + 1
        else:
            print("the answer is incorrect")

    if a == 3:
        preg = "¿Who is the fastest athlete in the history?"
        print(preg)
        erantzuna = input()

        if erantzuna.lower() == "usain bolt":
            print("the answer is Correct")
            score + 1
        else:
            print("the answer is incorrect")


def entertainment():
    qentertainment = ["Who is the main character in the pokémon series?",
                      "What is the most famous technique of goku from dragon ball?",
                      "What is the name of the film that toys have sense of life?"]
    aentertainment = ["Ash Ketchum", "Kamehameha", "Toy Story"]

    a = random.randrange(0, 3)
    if a == 1:
        preg = "Who is the main character in the pokémon series?"
        print(preg)
        erantzuna = input()

        if erantzuna.lower()== "ash ketchum":
            print("the answer is Correct")
            score + 1
        else:
            print("the answer is incorrect")

    if a == 2:
        preg = "What is the most famous technique of goku from dragon ball?"
        print(preg)
        erantzuna = input()

        if erantzuna.lower() == "kamehameha":
            print("the answer is Correct")
            score + 1

        else:
            print("the answer is incorrect")

    if a == 3:
        preg = "What is the name of the film that toys have sense of life?"
        print(preg)
        erantzuna = input()

        if erantzuna.lower() == "toy story":
            print("the answer is Correct")
            score + 1
        else:
            print("the answer is incorrect")


def geography():
    qgeo = ["¿which is the country with the highest population?", "¿which is the highest mountain in the world?",
            "which is the capital of the USA "]
    ageo = ["China", "Everest", "Washington DC"]

    a = random.randrange(0, 3)
    if a == 1:
        preg = "¿which is the country with the highest population?"
        print(preg)
        erantzuna = input()

        if erantzuna.lower() == "china":
            print("the answer is Correct")
            score + 1
        else:
            print("the answer is incorrect")

    if a == 2:
        preg = "¿which is the highest mountain in the world?"
        print(preg)
        erantzuna = input()

        if erantzuna.lower() == "everest":
            print("the answer is Correct")
            score + 1
        else:
            print("the answer is incorrect")

    if a == 3:
        preg = "which is the capital of the USA "
        print(preg)
        erantzuna = input()

        if erantzuna.lower() == "washington dc":
            print("the answer is Correct")
            score + 1
        else:
            print("the answer is incorrect")


def art():
    qart = ["Who painted the Mona Lisa?", "Who painted the last dinner?",
            "What city is depicted in Van Gogh's The Starry Night?"]
    aart = ["Leonardo da Vinci", "Leonardo da Vinci", "Vincent van Gogh"]
    a = random.randrange(0, 3)

    if a == 1:
        preg = "Who painted the Mona Lisa?"
        print(preg)
        erantzuna = input()

        if erantzuna.lower() == "leonardo da vinci":
            print("the answer is Correct")
            score + 1
        else:
            print("the answer is incorrect")

    if a == 2:
        preg = "Who painted the last dinner?"
        print(preg)
        erantzuna = input()

        if erantzuna.lower() == "leonardo da vinci":
            print("the answer is Correct")
            score + 1
        else:
            print("the answer is incorrect")

    if a == 3:
        preg = "What city is depicted in Van Gogh's The Starry Night?"
        print(preg)
        erantzuna = input()

        if erantzuna.lower() == "new york":
            print("the answer is Correct")
            score + 1
        else:
            print("the answer is incorrect")

score = 0
name = input("Enter your name please ")
num=0

while num != 6:

    print("Hello " + name + " you are gonna play a quiz and you have a few topics and to win you have to answer the questions as fast as you can\n")

    print("TOPICS")
    print("___________________")
    print("1-History")
    print("2-Sport")
    print("3-Entertainment")
    print("4-Geography")
    print("5-Art")
    print("6-exit")
    print("___________________")
    num = int(input("what topic do you want \n"))

    if num == 1:
        history()

    elif num == 2:
        sport()

    elif num == 3:
        entertainment()

    elif num == 4:
        geography()

    elif num == 5:
        art()

    

print(score)

f=open("your score.txt","a+")#a append, r read, write
list=[]
s=input(" your name")
list.append(s)
s2=input("your score")
list.append(s2)

for element in list:
   f.write(element + "\n")
f.close()


