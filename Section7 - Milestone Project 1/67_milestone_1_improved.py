# Condense check_game_over by wrapping entire check in parenthesis (completed)
# Use tuple unpacking where it makes sense (completed)

def game_menu():
    has_select_game_piece = False
    is_ready_to_play = False

    print("Welcome to Tic Tac Toe!")

    while not has_select_game_piece:
        p1_game_piece = input("Player 1: Do you want to be X or O: ")
        p1_game_piece = p1_game_piece.upper()

        if p1_game_piece in ['X', 'O']:
            has_select_game_piece = True

        # determine p2's game piece
        if p1_game_piece == 'X':
            p2_game_piece = 'O'
        else:
            p2_game_piece = 'X'

    print("Player 1 will go first")

    while not is_ready_to_play:
        ready = input("Are you ready to play? (Y/N): ")

        if ready.upper() == "Y":
            is_ready_to_play = True

    return (p1_game_piece, p2_game_piece)


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
    position = 999

    while not valid_position:
        position = input("Choose your next position (1-9): ")

        if not position.isdigit():
            print("Enter a numerical value")
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
    # 6|7|8
    # 3|4|5
    # 0|1|2
    return ((bd[6] == bd[3] == bd[0] == game_piece) or
            (bd[7] == bd[4] == bd[1] == game_piece) or
            (bd[8] == bd[5] == bd[2] == game_piece) or
            (bd[6] == bd[7] == bd[8] == game_piece) or
            (bd[3] == bd[4] == bd[5] == game_piece) or
            (bd[0] == bd[1] == bd[2] == game_piece) or
            (bd[0] == bd[4] == bd[8] == game_piece) or
            (bd[6] == bd[4] == bd[2] == game_piece))


def game_over_menu(the_winner):
    user_input = ""
    valid_response = False

    print(f"Congratulations! {the_winner} won the game!")
    while not valid_response:
        user_input = input("Do you want to play again? (Y/N): ")
        user_input = user_input.lower()

        if user_input in ['y', 'n']:
            valid_response = True

    return user_input == 'n'


# ================
# Game Logic (main)
# ================
stop_playing = False

while not stop_playing:
    board_state = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    game_over = False
    p1_game_piece = '@'
    p2_game_piece = '@'
    winner = "No one"
    turnNum = 0

    p1_game_piece, p2_game_piece = game_menu()

    # draw initial board
    draw_board(board_state)

    while not game_over:
        # player 1 choose
        p1_choice = get_position(board_state)
        board_state = update_board_state(board_state, p1_game_piece, p1_choice)
        draw_board(board_state)
        turnNum += 1

        # check if player 1 has won
        if check_game_over(board_state, p1_game_piece):
            game_over = True
            winner = "Player 1"
            break

        # check if board is full
        if turnNum >= 9:
            break

        # player 2 choose
        p2_choice = get_position(board_state)
        board_state = update_board_state(board_state, p2_game_piece, p2_choice)
        draw_board(board_state)
        turnNum += 1

        # check if player 2 has won
        if check_game_over(board_state, p2_game_piece):
            game_over = True
            winner = "Player 2"
            break

        # check if board is full
        if turnNum >= 9:
            break

    # display winner and check if players want to play again
    stop_playing = game_over_menu(winner)

print("Thanks for playing!")
