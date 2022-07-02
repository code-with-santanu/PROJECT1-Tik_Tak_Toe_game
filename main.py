from Functions import *


def game_on(reset_list):
    count = 0
    turn = 2
    while count < 9:

        turn = player_turn(turn)
        user_choice = user_input()
        check = cheat_check(reset_list, user_choice)

        if check == True:
            reset_list = replace_choice(reset_list, user_choice, turn)
            count += 1
        else:
            print('Hello cheater:) \nThis block is not empty')
            # user_choice = user_input()
            turn = player_turn(turn)

        display_board(reset_list)
        if count >= 5:
            iswin = win_check(reset_list)
            if iswin > 0:
                player(reset_list, iswin)
                break
            else:
                if count == 9:
                    print('OH NO:( \nTHE  GAME IS OVER!!!!')
                    break
                else:
                    continue

    return reset_list


board_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# replace every element in the list with blank place
reset_list = display_board(board_list)

print("\nARE  YOU  READY  GUYS?\nLET'S  START  THE  GAME.......")
# showing empty board
clear_board(reset_list)


game_on(reset_list)
