# underscores indicate that the intention is that the method is not intended to be used from outside its containing module
#
# double underscored methods should NEVER be changed
#
# an underscore can be used as a variable name ie. _ = 6
# this (or __) is called a throwaway variable name (when it is only going to be used for one thing quickly and nothing else

# def _deal_card(frame):
#
# when the underscore is added, python will generate a WARNING but will still allow it to be used
#
# using import blackjack will INCLUDE underscored methods but, if importing using * then anything with an underscore will not be imported:
#
# from BlackJack import *
#
# g = sorted(globals())
# for x in g:
#     print(x)
#
# _deal_card(dealer_card_frame) - this now returns an error as it is not found by the import


# __annotations__
# __builtins__
# __cached__
# __doc__
# __file__
# __loader__
# __name__
# __package__
# __spec__
# button_frame
# card_frame
# cards
# deal_dealer
# deal_player
# dealer_button
# dealer_card_frame
# dealer_score_label
# dealers_hand
# deck
# initial_deal
# load_images
# mainWindow
# new_game
# play
# player_button
# player_card_frame
# player_score_label
# players_hand
# random
# reset_button
# result
# resultText
# score_hand
# shuffle
# shuffle_button
# tkinter
# __main__