def game(board):
    turn1 = 'X'
    turn2 = 'O'
    count = 0
    flag = True


    for i in range(10):
        printboard(board)
        print('Turn of player ' + str(count % 2))

        # Check for valid input
        while flag:
            temp = int(input('You choose: '))
            if temp not in board.keys():
                print('Invalid input, insert again')
            else:
                break

        # Sign on the table
        if (board[temp] == ' ') and (count % 2):
            board[temp] = turn1 # place: empty & == 0 -> turn1
        elif (board[temp] == ' ') and not (count % 2):
            board[temp] = turn2 # place: empty & == 1 -> turn2
        else:
            print('Marking in unavailable square\n')
            break


        # Win or lose condition
        if board[1] == board[2] == board[3] == turn1:
            print('Player 1 is win')
            printboard(board)
            break
        elif board[1] == board[2] == board[3] == turn2:
            print('Player 0 is win')
            printboard(board)
            break
        elif board[4] == board[5] == board[6] == turn1:
            print('Player 1 is win')
            printboard(board)
            break
        elif board[4] == board[5] == board[6] == turn2:
            print('Player 0 is win')
            printboard(board)
            break
        elif board[7] == board[8] == board[9] == turn1:
            print('Player 1 is win')
            printboard(board)
            break
        elif board[7] == board[8] == board[9] == turn2:
            print('Player 0 is win')
            printboard(board)
            break
        elif board[1] == board[4] == board[7] == turn1:
            print('Player 1 is win')
            printboard(board)
            break
        elif board[1] == board[4] == board[7] == turn2:
            print('Player 0 is win')
            printboard(board)
            break
        elif board[2] == board[5] == board[8] == turn1:
            print('Player 1 is win')
            printboard(board)
            break
        elif board[2] == board[5] == board[8] == turn2:
            print('Player 0 is win')
            printboard(board)
            break
        elif board[3] == board[6] == board[9] == turn1:
            print('Player 1 is win')
            printboard(board)
            break
        elif board[3] == board[6] == board[9] == turn2:
            print('Player 0 is win')
            printboard(board)
            break
        elif board[1] == board[5] == board[9] == turn1:
            print('Player 1 is win')
            printboard(board)
            break
        elif board[1] == board[5] == board[9] == turn2:
            print('Player 0 is win')
            printboard(board)
            break
        elif board[3] == board[5] == board[7] == turn1:
            print('Player 1 is win')
            printboard(board)
            break
        elif board[3] == board[5] == board[7] == turn2:
            print('Player 0 is win')
            printboard(board)
            break

        # The case when game is fair
        if count < 10:
            count += 1
        else:
            print('The game is fair')
            break


def printboard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
