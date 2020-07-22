import random

standard_numbers_all = []
selected_numbers = []
star_numbers_all = []
lucky_stars = []

while len(standard_numbers_all) < 50:
    ball_number = random.randint(1,50)
    if ball_number not in standard_numbers_all:
        standard_numbers_all.insert(0, ball_number)
        if ball_number not in (selected_numbers) and len(selected_numbers) < 5:
            selected_numbers.insert(0, ball_number)

while len(star_numbers_all) < 12:
    star_number = random.randint(1,12)
    if star_number not in star_numbers_all:
        star_numbers_all.insert(0, star_number)               #insert the number to the list
        if star_number not in (lucky_stars) and len(lucky_stars) < 2:
             lucky_stars.insert(0, star_number)

standard_numbers_all.sort()
selected_numbers.sort()
star_numbers_all.sort()
print(standard_numbers_all)  #ensure all numbers are present
print(star_numbers_all)
print('-' * 80)
print('The main numbers to select are: {}'.format(selected_numbers))
print('-' * 80)
print('The lucky star numbers to select are: {}'.format(lucky_stars))
print('-' * 80)
