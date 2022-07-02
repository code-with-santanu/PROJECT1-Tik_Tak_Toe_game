from Functions import *


def board():
    board_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Display the position of each block
    reset_list = display_board(board_list)

    print("\nARE  YOU  READY  GUYS?\nLET'S  START  THE  GAME.......")
    # showing empty board
    display_board(reset_list)

    return reset_list


def game_on(reset_list):
    # Take players name
    player1 = input('\nEnter the name of first player: ')
    player2 = input('\nEnter the name of second player: ')

    count = 0
    turn = 2
    while count < 9:
        # Whose turn it is
        turn = player_turn(player1, player2, turn)
        # Ask user for a valid position
        user_choice = user_input()
        # Check if the position is empty
        check = cheat_check(reset_list, user_choice)

        if check == True:
            # Replace the blank place with user choice
            reset_list = replace_choice(reset_list, user_choice, turn)
            count += 1
        else:
            print('\nHello cheater:) \nThis block is not empty')
            # user_choice = user_input()
            turn = player_turn(player1, player2, turn)

        # Display updated board every time
        display_board(reset_list)
        if count >= 5:
            iswin = win_check(reset_list)
            if iswin > 0:
                player(reset_list, iswin, player1, player2)

                # Ask user to play again
                choice = replay()
                return choice
            else:
                if count == 9:
                    print('\nOH NO:( \nTHE  GAME IS OVER!!!!')

                    # Ask user to play again
                    choice = replay()
                else:
                    continue

    return choice


game = True
while game:
    # Play the game
    replay_choice = game_on(board())
    if replay_choice == True:
        # Replaying the game
        game_on(board())
    else:
        print('\nTHANKS FOR PLAYING :)')
        # Force the game not to replay
        game = False
