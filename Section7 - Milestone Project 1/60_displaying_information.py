# def display(row1, row2, row3):
#     print(row1)
#     print(row2)
#     print(row3)
# row1 = [' ', ' ', ' ']
# row2 = [' ', ' ', ' ']
# row3 = [' ', ' ', '']
# row2[1] = 'X'
# display(row1, row2, row3)

# prototype tic-tact-toe board
def DrawBoard(board):
    row0 = "-----------"
    row1 = " {0} | {1} | {2} ".format(board[0], board[1], board[2])
    row2 = " {0} | {1} | {2} ".format(board[3], board[4], board[5])
    row3 = " {0} | {1} | {2} ".format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row0)
    print(row2)
    print(row0)
    print(row3)
    print()


boardState = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
boardState[2] = "x"
boardState[5] = "x"
boardState[8] = "x"
DrawBoard(boardState)
