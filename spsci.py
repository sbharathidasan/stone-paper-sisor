import time  
import random
def countdown(c):      
    while c:  
        m, s = divmod(c, 60)  
        timer = '{:02d}:{:02d}'.format(m, s)  
        print(timer, end="\r")  
        time.sleep(1)  
        c -= 1       
def spsci():
    d=random.randint(1,3)
    if d==1:
        print("stone")
    elif d==2:
        print("paper")
    else:
        print("scissor")
def timfu():
    print("choose \"stone\" , \"paper\" or \"scissor\" in mind")
    c=2
    while c:
        m, s = divmod(c, 60)
        timer = '{:02d}:{:02d}'.format(m, s)
        time.sleep(1)
        c -= 1
timfu()
countdown(5)
print("my decission is")
spsci()  