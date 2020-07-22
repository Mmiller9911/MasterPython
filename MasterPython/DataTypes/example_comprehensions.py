# python has comprehensions for:
#
# lists
# dicts
# sets
# list comp and set comp are exactly the same except one produces a list and one produces a set
# list comp produces a list but it doesnt have to be provided a list to iterate over
# it does so by evaluating each item in the iterable
# we can iterate over and evaluate any object which is iterable
# we should only use list comprehensions if we NEED to, if other code is simpler then use that
# comprehensions don't have the side-effects you can get with for loops

#  ============================================================================================================================================
#  List comprehensions
#  ============================================================================================================================================

text = 'what have the romans ever done for us?'

capitals = [char.upper() for char in text]
print(capitals)

words = [word.upper() for word in text.split(' ')]
print(words)

numbers = [1, 2, 3, 4, 5, 6]
squares = [number ** 2 for number in range(1, 7)]
squares1 = [number ** 2 for number in numbers]
# expression is (number ** 2) and iteration is (for number in range /number in range(1, 7))
print(squares)
print(squares1)


def centre_text(*args):

    text1 = "-".join([str(arg) for arg in args])  # this is a list comprehension
    text = "-".join(str(arg) for arg in args)  # this is a generator comprehension
    left_margin = (80 - len(text)) // 2
    left_margin1 = (80 - len(text)) // 2
    print(" " * left_margin, text)
    print(" " * left_margin1, text1)


# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam, spam and spam")
centre_text("first", "second", 3, 4, "spam") # you cannot add ints to strings but this list comprehension allows it

#  ============================================================================================================================================
#  convert a for loop into a list comprehension
#  ============================================================================================================================================

text = 'Harmony is cute oh yeah oh yeah aha'
output = []
for x in text.split():
    output.append(len(x))
print(output)

stringy = 'Harmony is cute oh yeah oh yeah aha'
result = [len(x) for x in stringy.split()]
print(result)

answer = [(x, len(x)) for x in stringy.split()]
print(answer)

inch_measurement = (3, 8, 20)
cm_measurement = [inch * 2.54 for inch in inch_measurement]
print(cm_measurement)


#  ============================================================================================================================================

# set comprehension is the same but doesnt contain duplicates
set_comp = {(x, len(x)) for x in stringy.split()}
print(set_comp)

#  ============================================================================================================================================

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

loc = 1
# forest = [locations[exit] for exit in exits if loc in exits[exit].values()]
# print(forest)

print('List comprehension inside a for loop:')
for loc in sorted(locations):
    exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
    print('Locations leading to {}'.format(loc), end='\t')
    print(exits_to_destination_2)

print('nested comprehension')
print('--------------------')

exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()] for loc in sorted(locations)]
print(exits_to_destination_3)

print()
for index, loc in enumerate(exits_to_destination_3):
    print('Locations leading to {}'.format(index), end='\t')
    print(loc)

#  ============================================================================================================================================

menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"],
    ["tree", "bark"]
]

print('-' * 50)

#  this is a conditional comprehension
#  as this is a FILTER we cannot have an else clause - a filter even allows something through or it doesn't
meals = [meal for meal in menu if 'spam' not in meal if 'chicken' not in meal]
meals1 = [meal for meal in menu if 'spam' not in meal and 'chicken' not in meal]
# expression = meal # iteration = for meal in menu # filter = if 'spam' not in meal
print(meals)
print(meals1)

#  with two filters
fussy_meals = [meal for meal in menu if 'spam' or 'eggs' in meal if not ('bacon' in meal and 'sausage' in meal)]
print(fussy_meals)

#  with one filter
fussy_meals = [meal for meal in menu if ('spam' or 'eggs' in meal) and not ('bacon' in meal and 'sausage' in meal)]
print(fussy_meals)


#  ============================================================================================================================================

#
# expression =   meal if 'spam' not in meal else 'skipped'
# iteration = for meal in menu
# filter = None
meals = [meal if 'spam' not in meal else 'skipped' for meal in menu]
print(meals)

#  ============================================================================================================================================

fizzbuzz = ['fizz buzz' if x % 15 == 0 else 'fizz' if x % 3 == 0 else 'buzz' if x % 5 == 0 else str(x)
            for x in range(1, 31)]

print(fizzbuzz)

# print a string of 12 chars with the results in the centre padded by '*' values
                                 # this only works because converting the x to a string

#  ============================================================================================================================================

