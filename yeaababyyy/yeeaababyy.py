print("Yo yo yo. I be the new ai chatbot for the future. Talk to me cuh..")
import random
rand = [1,2,3,4,5,6]
rand2 = [1,2,3]
while True:
    inp = input("Whatchu tryna say..").lower()
    words = inp.split()

    if "yo" in words or "hi" in words or "hello" in words or "helo" in words or "yoo" in words:
        print("Whaddup")
    elif "how" in words and "you" in words and not "old" in words:
        print("I'm good cuh..")
    elif "how" in words and "old" in words and "you" in words:
        print("I am currently like a few minutes old bruh..")
    elif "break" in words:
        print("K bai")
        break
    if "game" in words:
        game = input("K which one? I got rock paper scissors, and i got odd eve").lower()
        gamep = game.split()
        if "rock" in gamep and "paper" in gamep and not "odd" in gamep and not "eve" in gamep:
            print("K rock paper scissors it is")
            gem = 1
            opp = random.choice(rand2)
            you1 = input("enter").lower()
            you11 = you1.split()
            if opp == 1 and "rock" in you11 or "rocks" in you11 or "stone" in you11:
                print("i got rocks too, damn")
            elif opp == 2 and "rock" in you11 or "rocks" in you11 or "stone" in you11:
                print("Dang it , i had scissors")
            elif opp == 3 and "rock" in you11 or "rocks" in you11 or "stone" in you11:
                print("Get wrecked noob, i had paper")
            if opp == 1 and "paper" in you11 or "papers" in you11:
               print("Dang it, i had rock")
            elif opp == 2 and "paper" in you11 or "papers" in you11:
                print("Get wrecked noob, i had scissors")
            elif opp == 3 and "paper" in you11 or "papers" in you11:
                print("I got paper too, damn")
            if opp == 1 and "scissors" in you11 or "scissor" in you11 or "scisors" in you11:
                print("Get wrecked noob i had rock")
            elif opp == 2 and "scissors" in you11 or "scissor" in you11 or "scisors" in you11:
                print("I had scissors too, damn")
            elif opp == 3 and "scissors" in you11 or "scissor" in you11 or "scisors" in you11:
                print("Dang it, i had paper")
        elif "odd" in gamep and "eve" in gamep and not "rock" in gamep and not "paper" in gamep:
            print("i dont play that shit, rock paper scissors it is..")
            gem = 1

    else:
        print("Nahh i aint smart enough to understand that yet..")
