from Game import *


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
