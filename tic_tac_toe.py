board = [' ' for spaces in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def isFreeSpace(pos):
    return board[pos] == ' '

def isBoradFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def isWinner(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or (b[4] == l and b[5] == l and b[6] == l) or
           (b[7] == l and b[8] == l and b[9] == l) or (b[1] == l and b[4] == l and b[7] == l) or
           (b[2] == l and b[5] == l and b[8] == l) or (b[3] == l and b[6] == l and b[9] == l) or
           (b[1] == l and b[5] == l and b[9] == l) or (b[3] == l and b[5] == l and b[7] == l))

def printBorad(board):
    print("   |    |   ")
    print(' ' + board[1] + ' | ' + ' ' + board[2] + ' | ' + board[3])
    print("   |    |   ")
    print("-----------")
    print("   |    |   ")
    print(' ' + board[4] + ' | ' + ' ' + board[5] + ' | ' + board[6])
    print("   |    |   ")
    print("-----------")
    print("   |    |   ")
    print(' ' + board[7] + ' | ' + ' ' + board[8] + ' | ' + board[9])
    print("   |    |   ")

def playerMove():
    run = True
    while run:
        move = int(input("Please select a position to enter X between 0 to 9 : "))
        try:
            if move > 0 and move < 10:
                if isFreeSpace(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print("Sapce Already Occupied, Enter another position")
            else:
                print("Please Type a Number between 1 and 9")
        except:
            print("Please type a number")

def computerMoves():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['X', 'O']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(board, let):
                move = 1
                return move

    cornerOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornerOpen.append(i)

    if len(cornerOpen) > 0:
        move = selectRandom(cornerOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def main():
    print("Welcome to Tic Tac Toe Game")
    printBorad(board)

    if isBoradFull(board):
        print("Tie Game")

    while not(isBoradFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBorad(board)
        else:
            print("Sorry you loss the game")
            break

        if not(isWinner(board, 'X')):
            move = computerMoves()
            if move == 0:
                print("Tie Game")
            else:
                insertLetter('O', move)
                print("Computer places an O on position", move)
                printBorad(board)
        else:
            print("You Won the Game")
            break

while True:
    x = input("Do you want to play again press Yes for y and No for n : ")
    if x.lower() == 'y':
        board = [' ' for spaces in range(10)]
        print("___________________________")
        main()
    else:
        break








