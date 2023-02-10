import random

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
    name = int(input("Enter your name please:"))
    score=0
    print("Hello" + name + "today you are gonna play a little quiz and you can't choose anything,you will only answer to five questions that are chosen randomly (the answers must be in lowercase)")
    print("Are you readyyyyyy?")
    count=0
    while count <=5:
        num = 3
        for i in range(1, num + 1):
            print(num - i, "es: ", num, "-", i)
        print("and the topic is...")
        for i in range(1, num + 1):
            print(num - i, "es: ", num, "-", i)
        print(random.randrange(topics))
        print("And the question is...")
        if topics== 1:
            print(random.randrange(qart))
            a= random.randint(0,3)
            print(qart[a])
            answer = int(input("Enter the answer:"))
            if answer == aart[a]:
                ++score
                ++count
            else:
                print("wrongggggg")
                ++count
        elif topics==2:
            print(random.randrange(qhistory))
            a = random.randint(0, 3)
            print(qhistory[a])
            answer = int(input("Enter the answer:"))
            if answer == ahistory[a]:
                ++score
                ++count
            else:
                print("wrongggggg")
                ++count
        elif topics==3:
            print(random.randrange(qsport))
            a = random.randint(0, 3)
            print(qsport[a])
            answer = int(input("Enter the answer:"))
            if answer == asport[a]:
                ++score
                ++count
            else:
                print("wrongggggg")
                ++count
        elif topics==4:
            print(random.randrange(qentertainment))
            a = random.randint(0, 3)
            print(qentertainment[a])
            answer = int(input("Enter the answer:"))
            if answer == aentertainment[a]:
                ++score
                ++count
            else:
                print("wrongggggg")
                ++count
        elif topics==5:
            print(random.randrange(qgeography))
            a = random.randint(0, 3)
            print(qgeography[a])
            answer = int(input("Enter the answer:"))
            if answer == ageography[a]:
                ++score
                ++count
            else:
                print("wrongggggg")
                ++count
    print("You answered" + score + "correctly")
