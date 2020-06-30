# Project Milestone 1: Tic Tac Toe game for 2 human players
#
# Requirements
#   * 2 players should be able to play the game on the same computer
#   * the board should be printed out everytime a player makes a move
#   * you should be able to accept input of the player position and then place a symbol on the board
#
# Tic Tac Toe Board
# 7|8|9
# 4|5|6
# 1|2|3
#
# Game flow
# * "Welcome to Tic Tac Toe!"
# * "Player 1: Do you want to be X or O?"
# * "Player 1 will go first""
# * "Are you ready to play? Enter Yes or No."
# * -display board (empty)-
# * "Choose your next position: (1-9)"
# * -display board w/ (X)-
# * "Choose your next position: (1-9)"
# * -display board w/ (O)-
# * "..."
# * "Congratulations! You won the game!"
# * "Do you want to play again? Enter Yes or No: "


def game_menu():
    has_select_game_piece = False
    is_ready_to_play = False

    print("Welcome to Tic Tac Toe!")

    while not has_select_game_piece:
        p1_game_piece = input("Player 1: Do you want to be X or O: ")
        p1_game_piece = p1_game_piece.upper()

        if p1_game_piece in ['X', 'O']:
            has_select_game_piece = True

    print("Player 1 will go first")

    while not is_ready_to_play:
        ready = input("Are you ready to play? (Y/N): ")

        if ready.upper() == "Y":
            is_ready_to_play = True

    return p1_game_piece


def draw_board(board):
    rowLn = "-----------"
    row1 = " {0} | {1} | {2} ".format(board[6], board[7], board[8])
    row2 = " {0} | {1} | {2} ".format(board[3], board[4], board[5])
    row3 = " {0} | {1} | {2} ".format(board[0], board[1], board[2])
    print()
    print(row1)
    print(rowLn)
    print(row2)
    print(rowLn)
    print(row3)
    print()


def get_position(brd_state):
    valid_position = False

    while not valid_position:
        position = input("Choose your next position (1-9): ")

        if not position.isdigit():
            print("Enter a numberical value")
        else:
            # convert into integer
            position = int(position)

            # check number is 1-9
            if not (1 <= position <= 9):
                print("Enter a value between 1 and 9")
            # check if position is taken
            elif brd_state[position - 1] in ['X', 'O']:
                print("This spot has already been taken. Please select another location")
            else:
                valid_position = True

    return position


def update_board_state(brd_state, game_piece, position):
    brd_state[position - 1] = game_piece
    return brd_state


def check_game_over(bd, game_piece):
    there_is_a_winner = False

    # incomplete
    if (bd[6] == bd[3] == bd[0] == game_piece):
        there_is_a_winner = True

    return there_is_a_winner


# ================
# Game Logic (main)
# ================
stop_playing = False

while not stop_playing:
    board_state = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    game_over = False
    p1_game_piece = '@'
    p2_game_piece = '@'
    winner = "no one"

    # p1_game_piece = game_menu()

    # # determine p2's game piece
    # if p1_game_piece == 'X':
    #     p2_game_piece = 'O'
    # else:
    #     p2_game_piece = 'X'

    # test
    # p1_game_piece = 'X'
    # p2_game_piece = 'O'

    while not game_over:
        # draw initial board
        board_state[6] = 'X'
        board_state[3] = 'X'
        draw_board(board_state)
        
        # player 1 choose
        p1_choice = get_position(board_state)
        board_state = update_board_state(board_state, p1_game_piece, p1_choice)
        draw_board(board_state)

        # check if player 1 has won
        if check_game_over(board_state, p1_game_piece):
            game_over = True
            break
        
        # player 2 choose
        p2_choice = get_position(board_state)
        board_state = update_board_state(board_state, p2_game_piece, p2_choice)
        draw_board(board_state)

        # check if player 2 has won
        if check_game_over(board_state, p1_game_piece):
            game_over = True
            break

        game_over = True #temporary

    print("Congratulations! You won the game!")
    print("Do you want to play again?")
    stop_playing = True
