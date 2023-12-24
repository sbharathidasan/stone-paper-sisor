import random
def start():
    user=int(input("choose \n1. for \"stone\" , \n2. for \"paper\" or \n3. for \"scissor\"\n "))
    user=user-1
    print("my decission is")
    game= ["scissor", "paper", "stone"]
    d=random.randint(0,2)
    print(game[d])
    spsci(game[d],game[user])
def spsci(m,i):
    if m==i:
        print("match draw")
        inisi()
    else:
        if m=="stone" and i=="paper":
            print("you won")
        elif m=="paper" and i=="scissor":
            print("you won")
        elif m=="scissor" and i=="stone":
            print("you won")
        else :
            print("better luck next time")
start()
