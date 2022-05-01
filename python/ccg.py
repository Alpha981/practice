import random

print("enter the number between 1 to 5")
computer_score=0
player_score=0
answer='y'
while answer=='Y' or answer=='y':
    print("red-1 \t yellow-2\t orange-3\t green-4\t blue-5\nyour turn: ")
    player_choice=int(input("user turn"))

    while player_choice>5 and player_choice<1:
        player_choice= int(input("enter  valid number"))

    if player_choice==1 :
        choice_color ='red'
    elif player_choice==2:
        choice_color ='yellow'
    elif player_choice==3:
        choice_color ='orange'
    elif player_choice==4:
        choice_color ='green'
    else:
        choice_color ='blue'

    print("user color choice is: " +choice_color)
    print("now computer turn to choose color...")

    computer_choice=random.randint(1,5)

    if computer_choice == 1:
        com_choice_color ='red'
    elif computer_choice==2:
        com_choice_color ='yellow'
    elif computer_choice==3:
        com_choice_color ='orange'
    elif computer_choice==4:
        com_choice_color ='green'
    else:
        com_choice_color ='blue'
    print("computer color choice is: ",com_choice_color)

    #condition for winning
    if(choice_color==com_choice_color):
        player_score+= 1
        print("player_score: " + str(player_score))
        print("computer_score: " + str(computer_score))
    else:
        computer_score+=1
        print("player_score: " + str(player_score))
        print("computer_score: " + str(computer_score))
        
    answer=input("Do u want to play agin (Y/N): ")

    if answer =='n' or answer=='N':
        break
    elif answer=='Y' or answer=='y':
        pass
    else:
      answer=input("enter y or n: ")

if computer_score==player_score:
    print("<---Game tied--->")
elif computer_score<player_score:
    print("<---Player won--->")
elif computer_score>player_score:
    print("<---Computer won--->")
    
print("****Thanks For Playing***")