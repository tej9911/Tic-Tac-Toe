def printBoard(xstate, zstate):
    board = []
    for i in range(9):
        if xstate[i]:
            board.append('X')
        elif zstate[i]:
            board.append('O')
        else:
            board.append(str(i + 1))  # Show numbers for empty spots

    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    
if __name__ == "__main__":
    xstate = [0] * 9  # List of 9 elements
    zstate = [0] * 9  
    turn = 1  # 1 for X, 0 for O

    print("Welcome to Tic-Tac-Toe!")

    while True:
        printBoard(xstate, zstate)
        if turn == 1:
            print("X's Turn")
            value = int(input("Enter a position (1-9): ")) - 1
            if xstate[value] == 0 and zstate[value] == 0:  # Ensure valid move
                xstate[value] = 1
                turn = 0  # Switch turn
            else:
                print("Invalid move, try again!")
        else:
            print("O's Turn")
            value = int(input("Enter a position (1-9): ")) - 1
            if xstate[value] == 0 and zstate[value] == 0:
                zstate[value] = 1
                turn = 1  # Switch turn
            else:
                print("Invalid move, try again!")
