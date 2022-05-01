import random

def hangman():
    word=random.choice(["laptop" , "java", "python","numpy","keras","seaborn","pandas"])
    validletters='abcdefghijklmnopqrstuvwxyz'
    turns=10
    guessmadee=''

    while len(word)>0:
        main=""
      #  missed=0
        for letter in word:
            if letter in guessmadee:
                main= main +letter
            else:
                main=main+"_"+""

        if main == word:
            print(main)
            print("you win") 
            break
        print("Guess the word:",main)
        guess=input()

        if guess in validletters:
            guessmadee=guessmadee+guess
        else:
            print("enter a valid character")
            guess=input()
        if guess not in word:
            turns-=1
            if turns==9:
                print("9 turns left")
                print("============")
            if turns==8:
                print("8 turns left")
                print("============")
                print("      0     ")
            if turns==7:
                print("7 turns left")
                print("============")
                print("      0     ")
                print("      |     ")
            if turns==6:
                print(" 6turns left")
                print("============")
                print("      0     ")
                print("      |     ")
                print("     /      ")
            if turns==5:
                print("5 turns left")
                print("============")
                print("      0     ")
                print("      |     ")
                print("     / \    ")
            if turns==4:
                print("4 turns left")
                print("============")
                print("    \ 0     ")
                print("      |     ")
                print("     / \    ")
            if turns==3:
                print("3 turns left")
                print("============")
                print("    \ 0 /   ")
                print("      |     ")
                print("     / \    ")
            if turns==2:
                print("2 turns left")
                print("============")
                print("    \ 0 / | ")
                print("      |     ")
                print("     / \    ")
            if turns==1:
                print("1 turns left")
                print("============")
                print("    \ 0_|/  ")
                print("      |     ")
                print("     / \    ")
            if turns==0:
                print("YOU LOSE")
                print("man is hanged")
                print("      0_|   ")
                print("     /|\    ")
                print("     / \    ")
                print("the answer is ",word)
                break


name= input("enter your name: ")
print("welcome" ,name)
print("=======================")
print("Try to guess the word in less than 10 attempts")
hangman()