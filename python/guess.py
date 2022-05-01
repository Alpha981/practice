import random

guess=random.randint(1,100)
#print(guess)
count=10
num=int(input("enter ur guess: "))
    
while (True and count>0):
    if (num==guess):
        print("YOU WON")
        print("you guessed in {} attempts".format(10-count))
        break
    elif (num<guess):
        print("bigger number please")
        count-=1
        #num=int(input("enter ur guess: "))
    elif (num>guess):
        print("lower number please")
        count-=1
    print("u have {} chances left".format(count))
    num=int(input("enter ur guess: "))
   
if (count==0):
    print("YOU LOSE")