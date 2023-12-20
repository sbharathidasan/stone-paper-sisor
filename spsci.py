import time  
import random
def inisi():
    i=input("choose \"stone\" , \"paper\" or \"scissor\" ")
    print("my decission is")
    des = ["scissor", "paper", "stone"]
    d=random.randint(0,2)
    if(d==0):
        m=des[d]
        print(m)
    elif(d==1):
        m=des[d]
        print(m)
    else:
        m=des[d]
        print(m)
    spsci(m,i)
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
def timfu():
    c=2
    while c:
        m, s = divmod(c, 60)
        timer = '{:02d}:{:02d}'.format(m, s)
        time.sleep(1)
        c -= 1
inisi()
timfu()
