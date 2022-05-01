def spaceisfree(pos):
    return board[pos]==' '

def insertletter(letter,pos):
    board[pos]=letter

def printboard(board):
    print("   |   |   ")
    print(" " + board[1] + ' | '  + board[2] + ' | ' + board[3])
    print("   |   |   ")
    print("----------------")
    print("   |   |   ")
    print(" " + board[4] + ' | '  + board[5] + ' | ' + board[6])
    print("   |   |   ")
    print("----------------")
    print("   |   |   ")
    print(" " + board[7] + ' | '  + board[8] + ' | ' + board[9])
    print("   |   |   ")
    print("----------------")

def isboardfull(board):
    if board.count(' ')>1:
        return False
    else:
        print("tie game")

def iswinner(b,l):
    return ((b[1]==l and b[2]==l and b[3]==l) or 
    (b[4]==l and b[5]==l and b[6]==l) or
    (b[7]==l and b[8]==l and b[9]==l) or
    (b[1]==l and b[4]==l and b[7]==l) or
    (b[2]==l and b[5]==l and b[8]==l) or
    (b[3]==l and b[6]==l and b[9]==l) or
    (b[1]==l and b[5]==l and b[9]==l) or
    (b[3]==l and b[5]==l and b[7]==l)) 

def playermove():
    run=True
    while run:
        move=input("please select a position to enter X between 1 to 9: ")
        try:
            move=int(move)
            if move>0 and move<10:
                if spaceisfree(move):
                    run=False
                    insertletter('X' , move)
                else:
                    printboard("sorry,this space is occupied")
            else:
                printboard("please type a number between 1 to 9")

        except:
            print("please type a number")

def computermove():
    possiblemoves=[x for x, letter in enumerate(board) if letter==' ' and x!=0 ]
    move =0

    for let in ["O" , "X"]:
        for i in possiblemoves:
            boardcopy=board[:]
            boardcopy[i]=let
            if iswinner(boardcopy,let):
                move=i
                return move
    
    corneropen =[]
    for i in possiblemoves:
        if i in [1,3,7,9]:
            corneropen.append(i)
    if len(corneropen)>0:
        move= selectrandom(corneropen)
        return move

    if 5 in possiblemoves:
        move=5
        return move

    edgeopen=[]
    for i in possiblemoves:
        if i in [2,4,6,8]:
            edgeopen.append(i)
    if len(edgeopen)>0:
        move=selectrandom(edgeopen)
        return move

def selectrandom(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]
    
def main():
    print("welcome to the game!!")
    printboard(board)

    if isboardfull(board):
        print("tie game")

    while not(isboardfull(board)):
        if not(iswinner(board,'O')):
            playermove()
            printboard(board)
        else:
            print("sorry u lose :(")
            break
             
        if not(iswinner(board,'X')):
            move =computermove()
            if move==0:
                print("sorry u lose :(")
            else:
                insertletter('O', move)
                print("computer placed an O on position",move,'!')
                printboard(board)
        else:
            print(" you win!! :)")
            break

while True:
    x=input("Do you want to play again? (y/n): ")
    if x.lower()== 'y':
        board=[' ' for x in range(10)]
        print("---------------------")
        main()
    else:
        break


