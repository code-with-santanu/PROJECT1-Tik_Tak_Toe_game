# Display initial board
def display_board(board):

    # displaying the positions in the board
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-----')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-----')
    print(board[7] + '|' + board[8] + '|' + board[9])

    board = [' ']*10
    return board


# Clear the board
def clear_board(board):
    # replace the position no with blank space
    display_board(board)


# Take and verify users choice
def user_input():

    # Initial condition
    c = 'choice'
    check = True
    valid = range(1, 10)

    while c.isdigit() == False or check == True:
        c = input('Enter the position between(1-9): ')

        # digit checking
        if c.isdigit() == False:
            print("It's not an integer")
        elif c.isdigit() == True:

            # range checking
            if int(c) in valid:
                check = False
            else:
                print('You entered an invalid position')

    return int(c)


# Cheat Checking
def cheat_check(lst, user_choice):
    if lst[user_choice] == ' ':
        return True
    else:
        return False


# Place the marker
def replace_choice(lst, user_choice, player_no):
    if player_no == 1:
        lst[user_choice] = 'X'
    elif player_no == 2:
        lst[user_choice] = 'O'
    return lst


# winner check
def win_check(lst):
    if lst[1] == lst[2] == lst[3] and lst[1] != ' ':
        return 1
    elif lst[3] == lst[6] == lst[9] and lst[3] != ' ':
        return 3
    elif lst[7] == lst[8] == lst[9] and lst[7] != ' ':
        return 7
    elif lst[1] == lst[4] == lst[7] and lst[7] != ' ':
        return 4
    elif lst[1] == lst[5] == lst[9] and lst[1] != ' ':
        return 5
    elif lst[3] == lst[5] == lst[7] and lst[7] != ' ':
        return 5
    elif lst[4] == lst[5] == lst[6] and lst[4] != ' ':
        return 5
    elif lst[2] == lst[5] == lst[8] and lst[2] != ' ':
        return 2
    else:
        return 0


# Winner Player
def player(lst, win_index):
    if lst[win_index] == 'X':
        print('Player 1 win this game')
    elif lst[win_index] == 'O':
        print('Player 2 win this game')


def tie_game(win_index):
    if win_index == 0:
        print('The game is tied')


def player_turn(turn=2):
    if turn == 2:
        print("\nPlayer1's turn")
        turn = 1
    elif turn == 1:
        print("\nPlayer2's turn")
        turn = 2
    return turn
