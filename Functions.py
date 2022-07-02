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
            print("\nIt's not an integer")
        elif c.isdigit() == True:

            # range checking
            if int(c) in valid:
                check = False
            else:
                print('\nYou entered an invalid position')

    return int(c)


# Empty Checking
def cheat_check(lst, user_choice):
    # checking if the position is empty or not
    if lst[user_choice] == ' ':
        return True
    else:
        return False


# Chcek Who's turn is it
def player_turn(player1, player2, turn=2):
    if turn == 2:
        print("\n{}'s turn...".format(player1))
        turn = 1
    elif turn == 1:
        print("\n{}'s turn...".format(player2))
        turn = 2
    return turn


# Place the marker
def replace_choice(lst, user_choice, player_no):
    if player_no == 1:
        lst[user_choice] = 'X'
    elif player_no == 2:
        lst[user_choice] = 'O'
    return lst


# check if anyone wins
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


# Find winner's name
def player(lst, win_index, player1, player2):
    if lst[win_index] == 'X':
        print(f'Congrats!! {player1} wins this game')
    elif lst[win_index] == 'O':
        print(f'Congrats!! {player2} wins this game')


# Replay the game
def replay():
    print('\nWanna play again??')
    c = True
    while c:
        select = input('\nChoose one[y / n]: ')

        if select == 'y':
            c = False
            return True
        elif select == 'n':
            c = False
            return False
        else:
            print("\nEnter correct option")
            c = True
