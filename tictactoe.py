board = [' ' for spaces in range(10)]

def printBoard(board):
    print("   |   |   ")
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] )
    print("   |   |   ")
    print("___________")
    print("   |   |   ")
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] )
    print("   |   |   ")
    print("___________")
    print("   |   |   ")
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] )
    print("   |   |   ")

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def isWinner(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or (b[4] == l and b[5] == l and b[6] == l) or
        (b[7] == l and b[8] == l and b[9] == l) or (b[1] == l and b[4] == l and b[7] == l) or
        (b[2] == l and b[5] == l and b[8] == l) or (b[3] == l and b[6] == l and b[9] == l) or
        (b[1] == l and b[5] == l and b[9] == l) or (b[3] == l and b[5] == l and b[7] == l))

def insertLetter(letter, pos):
    board[pos] = letter

def isFreeSpace(pos):
    return board[pos] == ' '

def firstPlayerMove():
    run = True
    while run:
        move = int(input("Enter player one position between 1 to 9 : "))
        if move > 0 and move < 10:
            if isFreeSpace(move):
                run = False
                insertLetter("X", move)
            else:
                print("Position already occupied, Please enter another position")
        else:
            print("Enter valid position")
    else:
        print("Enter only number between 0 to 9")

def secondPlayerMove():
    run = True
    while run:
        move = int(input("Enter player second position between 1 to 9 : "))
        if move > 0 and move < 10:
            if isFreeSpace(move):
                run = False
                insertLetter("0", move)
            else:
                print("Position already occupied, Please enter another position")
        else:
            print("Enter valid position")
    else:
        print("Enter only number between 0 to 9")

def main():
    print("Welcome to Tic Tac Toe Game")
    printBoard(board)

    if isBoardFull(board):
        print("Tie Game")

    while not(isBoardFull(board)):

        if not(isWinner(board, '0')):
            firstPlayerMove()
            printBoard(board)
        else:
            print("Player second wins the game")
            break

        if not(isWinner(board, 'X')):
            if isBoardFull(board):
                print("Tie Game")
                break
            else:
                secondPlayerMove()
                printBoard(board)
        else:
            print("Player first wins the game")
            break

while True:
    decision = input("Do want to play Tic Tac Toe, Press y for Yes or n for No : ")
    if decision.lower() == 'y':
        board = [' ' for spaces in range(10)]
        print("___________________________")
        main()
    else:
        break




