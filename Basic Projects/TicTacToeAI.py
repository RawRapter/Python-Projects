"""
This Project is Tic Tac Toe Game, with the algorithm designed to make Computer Win.
"""

#For inserting the symbol to specified position
def insertLetter(letter,pos):
    board[pos] = letter

#Checks if space is free
def spaceIsFree(pos):
    return board[pos] == ' '

#Prints the board
def printBoard(board):
    print('   |   |   ')
    #Upper three Boxes
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    #center 3 Boxes
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    #Lower 3 Boxes
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

#Checks if the board is full
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

#Creating Winning positions
def IsWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

#Player movement Interface
def playerMove():
    run = True
    while run:
        move = input("Please Select a position for X i.e (1-9)")
        try:
            move = int(move)
            #Making Players move when selected from 1-9
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X' , move)
                #If something else provided i.e other than 1-9
                else:
                    print('Sorry, This Space is Occupied')
            else:
                print('Please type a number between 1 and 9')
        #If wrong input provided
        except:
            print('Please type a Number 1-9')

#Computer Movement Interface
def computerMove():
    #Making List of possible moves for the computer
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    #Creating loop to position the computer's Move
    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move

    #Creating list for empty corner positions
    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)
    #Randomly Selecting the corner
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    #Checks if center is available
    if 5 in possibleMoves:
        move = 5
        return move

    #Creating list for empty non corner positions
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    #randomly selecting the non corners
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

#To Randomly select some position
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

#Main Function for the game
def main():
    print("Welcome to the Game!")
    printBoard(board)

    #Loop until the board is not full
    while not(isBoardFull(board)):
        #When computer is made move and it is participant's turn
        if not(IsWinner(board , 'O')):
            playerMove()
            printBoard(board)
        #If computer wins
        else:
            print("Sorry You Loose!")
            break
        
        #When participant has made move and it is computer's turn
        if not(IsWinner(board , 'X')) or isBoardFull(board):
            move = computerMove()
            #If no move left
            if move == None:
                print(" ")
            #If there is a move
            else:
                insertLetter('O' , move)
                print('Computer placed an o on position ' , move , ':')
                printBoard(board)
        else:
            print("*----You Win!----*")
            break

    if isBoardFull(board):
        print("----Tie Game----")


#Starting part of the project
if __name__== "__main__" :
    #Loop to start play again when a game is finished
    while True:
        try:
            x = input("Do you want to play (y/n)? ")
            if x.lower() == 'y':
                board = [' ' for x in range(10)]
                print('---------------------------')
                main()
            #When invalid choice provided i.e. other than Y/N
            else:
                break
        except:
            print("You have provided the invalid choice, exiting!!")
            break