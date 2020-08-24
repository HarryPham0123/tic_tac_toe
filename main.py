import function1

#board = {7:' ', 8:' ', 9:' ', 4:' ', 5:' ', 6:' ', 1:' ', 2:' ', 3:' '}
#function.printboard(board)
#function.game(board)

while True:
    theBoard = [' '] * 10
    print('Welcome to Tic Tac Toe')
    playerLetter, computerLetter = function1.inputPlayer()
    turn = function1.whoGoesFirst()
    print('The'+turn+'will go first')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'human':
            # player's turn
            function1.drawBoard(theBoard)
            move = function1.getPlayerMove(theBoard)
            function1.makeMove(theBoard, playerLetter, move)

            if function1.isWinner(theBoard, playerLetter):
                print('Yayy you are win Human')
                function1.drawBoard(theBoard)
                gameIsPlaying = False
            else:
                if function1.isBoardFull(theBoard):
                    print('The game is tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn
            function1.drawBoard(theBoard)
            move = function1.getComputerMove(theBoard, computerLetter)
            function1.makeMove(theBoard, computerLetter, move)

            if function1.isWinner(theBoard, computerLetter):
                print('Unfortunately, the human is being beaten by computer')
                function1.drawBoard(theBoard)
                gameIsPlaying = False
            else:
                if function1.isBoardFull(theBoard):
                    function1.drawBoard(theBoard)
                    print('The game is tie!')
                    break
                else:
                    turn = 'human'

    if not function1.playAgain():
        break


