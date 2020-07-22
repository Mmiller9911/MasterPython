#  the computer should be able to guess any number within 1-1023 within 10 guesses

low = 1
high = 1000

#// does integer division (nearest whole number)
#/ does true division
#print(2 ** 10)
#print(2*2*2*2*2*2*2*2*2*2)

print('please think of a number between {} and {} '.format(low, high))
input('press ENTER to start ')
guesses = 1


while True:
    print('guessing in the range {} to {}'.format(low, high))
    guess = low + (high - low) // 2 # this formula calculates the midpoint between the high and low numbers to produce the next guess
    high_low = input('My guess is {}.  Should i guess higher or lower? '
                     'Enter h or l or c, if my guess was correct '
                     .format(guess).casefold())
    if high_low == 'h':
        low = guess + 1
        #Guess higher - the low end of the range becomes 1 higher than the guess
    elif high_low == 'l':
        high = guess - 1
        #Guess lower - the high end of the range becomes 1 lower than the guess
    elif high_low == 'c':
        print('correct in {} guesses'.format(guesses))
        break
    else:
        print('enter h/l/c')

    guesses += 1