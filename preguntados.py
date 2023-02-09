
import random
score=0
name = input("Enter your name please")


print("Hello" + name +
"you are gonna play a quiz and you have a few topics and to win you have to answer the questions as fast as you can")

print("TOPICS")
print("___________________")
print("1-History")
print("2-Sport")
print("3-Entertainment")
print("4-Geography")
print("5-Art")
print("___________________")

def history():

    qhist=["¿Who discovered America?"," ¿In which year finished World War 2","¿In which country was born Hitler?" ]
    
    print(random.ramdrange(qhist) )
    eratzuna =input()
    a= random.randrange (0,3)
    print(qspor[a]) 
    if eratzuna== aspor[a]:
        print("the answer is Correct")
        score + 1
    else :
        print("the answer is incorrect")
def sport():
    qspor=["¿which country won the world cup in 2022? ","¿who is the the player who scored more points in the NBA?", "¿Who is the fastest athlete in the history?"]
    aspor=["Argentina","Lebron James","Usain Bolt"]
    
    eratzuna =input()
    a= random.randrange (0,3)
    print(qspor[a]) 
    if eratzuna== aspor[a]:
        print("the answer is Correct")
        score + 1
    else :
        print("the answer is incorrect")
        
        

        

def entertainment():
    qentertainment = ["Who is the main character in the pokémon series?",
                      "What is the most famous technique of goku from dragon ball?",
                      "What is the name of the film that toys have sense of life?"]
    print(random.ramdrange(qentertainment))

def geography():
    qgeo=["¿which is the country with the highest population?","¿which is the highest mountain in the world?","which is the capital of the USA "]
    print(random.ramdrange(qgeo))
def art():
    qart = ["Who painted the Mona Lisa?", "Who painted the last dinner?",
            "What city is depicted in Van Gogh's The Starry Night?"]
    print(random.ramdrange(qart))


num= int(input())
match num:
    case 1:
        history()

    case 2:
        sport()

    case 3:
        entertainment()

    case 4:
        geography()

    case 5:
        art()




