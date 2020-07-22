import random

try:
    import tkinter
except ImportError:                   #python 2
    import Tkinter as tkinter

print(tkinter.TkVersion)

def load_images(card_images):
    suits = ['heart', 'diamond', 'club', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    #for each suite retrieve the images for the cards
    for suit in suits:
        # 1-10
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

        # face cards
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


def initial_deal():
    deal_player()
    dealers_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealers_hand))
    deal_player()

def deal_card(frame): #returns a tuple
    # pop the next card off the top of the deck
    next_card = deck.pop(0)  #take the last entry from the list and return it
    deck.append(next_card) # put the card back to the bottom of the deck
    # add the image to a label and dislay the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # return the cards face value
    return next_card


def score_hand(hand):
    # calculate the full score of all scores in the list
    # only one ace can have the value 11 and this would reduce to 1 if the score would bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # if score is > 21 and there is an ace then subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealers_score = score_hand(dealers_hand)
    while 0 < dealers_score < 17:   #as long as the dealers score is less then 17 keep dealing cards
        dealers_hand.append(deal_card(dealer_card_frame))
        dealer_score_label.set(dealers_score)
        dealers_score = score_hand(dealers_hand)

    players_score = score_hand(players_hand)
    if players_score > 21:
        resultText.set('Dealer wins!')
    elif dealers_score > 21 or dealers_score < players_score:
        resultText.set('Player wins!')
    elif dealers_score > players_score:
        resultText.set('Dealer wins!')
    else:
        resultText.set('Draw!!!!')


def deal_player():   # ideally a function should be self-contained and so not change global variables
    players_hand.append(deal_card(player_card_frame))
    players_score = score_hand(players_hand)

    player_score_label.set(players_score)
    if players_score > 21:
        resultText.set('Dealer wins!')


def new_game():   # ideally a function should be self-contained and so not change global variables
    global player_card_frame
    global dealer_card_frame
    global dealers_hand
    global players_hand

    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background='green')
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    resultText.set('')

    #create both players hands
    dealers_hand = []
    players_hand = []

    initial_deal()

def shuffle():
    random.shuffle(deck)


def play():
    initial_deal()
    mainWindow.mainloop()


mainWindow = tkinter.Tk()
#setup the screen and frames for the player
mainWindow.title('Black Jack')
mainWindow.geometry('640x480')
mainWindow.configure(background='green')


resultText = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=resultText)
result.grid(row=0, column=0, columnspan=3)


dealer_score_label = tkinter.IntVar()
player_score_label = tkinter.IntVar()

card_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan='3', rowspan='2')
tkinter.Label(card_frame, text='Player', background='green', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)
tkinter.Label(card_frame, text='Dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)


#embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background='green')
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_card_frame = tkinter.Frame(card_frame, background='green')
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)



# button frame
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, sticky='w', columnspan='3')



# buttons
dealer_button = tkinter.Button(button_frame, text='Dealer', command=deal_dealer)
dealer_button.grid(row=0, column='0')

player_button = tkinter.Button(button_frame, text='Player', command=deal_player)
player_button.grid(row=0, column='1')

reset_button = tkinter.Button(button_frame, text='New Game', command=new_game)
reset_button.grid(row=0, column='2')

shuffle_button = tkinter.Button(button_frame, text='Shuffle Deck', command=shuffle)
shuffle_button.grid(row=0, column='3')

#load the cards
cards = []
load_images(cards)
print(cards)


#create a new deck of cards and shuffle
deck = list(cards)
shuffle()

#create both players hands
dealers_hand = []
players_hand = []


if __name__ == '__main__':
    play()