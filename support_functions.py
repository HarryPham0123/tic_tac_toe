import random

def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('================')


def inputPlayer():
    # Input whatever letter
    # Output list in which the player's letter as the 1st item, the computer's letter as the second

    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    #0: human first, 1: computer first
    if random.randint(0, 1) == 0:
        return 'human'
    else:
        return 'computer'

def playAgain():
    # This func return True if user want to play again, otherwise False
    print('Human, do you want to play again??(yes or no)\n')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[int(move)] = letter

def isWinner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # Use bo instead of board and le instead of letter
    return (bo[7] == bo[8] == bo[9] == le or bo[4] == bo[5] == bo[6] == le or
            bo[1] == bo[2] == bo[3] == le or bo[7] == bo[4] == bo[1] == le or
            bo[8] == bo[5] == bo[2] == le or bo[9] == bo[6] == bo[3] == le or
            bo[7] == bo[5] == bo[3] == le or bo[1] == bo[5] == bo[9] == le)

def getBoardCopy(board):
    # Make a duplicate of board list and return it the duplicate
    dupBoard = []
    for k in board:
        dupBoard.append(k)
    return dupBoard

def isSpaceFree(board, move):
    # Return True is the pass move is free, otherwise is False
    return board[int(move)] == ' '

def getPlayerMove(board):
    # Let the player type on their move, return an int number
    move = ' '
    # (smart) if wanna a list of string number 1-9
    while not (move in '1 2 3 4 5 6 7 8 9'.split() and isSpaceFree(board, move)):
        print('Choose your move 1-9')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, moveList):
    # Return valid move from the passed list on the passed board
    # Return None if there is no valid move
    posMove = list()

    #Dealing with space free
    for k in moveList:
        if isSpaceFree(board, k):
            posMove.append(k)

    if len(posMove) == 0:
        return None
    else:
        return random.choice(posMove)


def getComputerMove(board, computerLetter): #board: list
    # Given a board and computer's letter, determine where to move and return that move
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    ## Here is our algorithm for our Tic Tac Toe AI
    # First check if we can win in the next move
    for t in range(1,10):
        copy1 = getBoardCopy(board)
        if isSpaceFree(copy1, t):
            makeMove(copy1, computerLetter, t)
            if isWinner(copy1, computerLetter):
                return t

    # Check if human can win in the next move, and block them
    for k in range(1,10):
        copy2 = getBoardCopy(board)
        if isSpaceFree(copy2, k):
            makeMove(copy2, playerLetter, k) # Visualize the human move
            if isWinner(copy2, playerLetter):
                return k
            
    # Try to take one of the corners if they are free
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center when it's free
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # Return True if every space on the board has been taken, otherwise return False
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
        else:
            continue
    return True
