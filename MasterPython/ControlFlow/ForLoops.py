#  ============================================================================================================================================
#  For Loops
#  ============================================================================================================================================
#  A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#  With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
#  a for loop is useful when you know in advance how many times the loop will execute
#  an else can be used in a for loop to execute ONLY when the entire loop has completed
#  continue makes the code skip the specified value in the for loop
#  break ends the loop when it is activated
#  for loop is zero-based by default

# There are two different uses for "ELSE" in python:
# 1.  In an IF statement it represents a statement which will execute if none of the other statements are True
# 2.  In FOR/WHILE/TRY loops it is executed if the previous code executed successfully

#  ============================================================================================================================================
#  Standard for loop
#  ============================================================================================================================================

for i in range(1, 20):  # last value is not included so its 1-19
    print("i is now {}".format(i))

for state in ['dead', 'alive', 'scaring Harmony']:
    print('the parrot is '+state)

for i in range(0, 100, 5):
    print(i)

summation = 0
for i in range(6):
    summation = summation + i
print(summation)

#  ============================================================================================================================================
#  Iterate over a string number and then output each character
#  ============================================================================================================================================

number = '100,464,773,242,666'
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i], end='')
print()
print(type(number))

#  ============================================================================================================================================
#  Iterate over a string number and add to a variable, then convert the variable to an integer and then output each value
#  ============================================================================================================================================

number = '100,464,773,242,666'
cleanedNumber = ''
for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print('The number is {}'.format(newNumber))
print(type(newNumber))
#  ============================================================================================================================================

#  ============================================================================================================================================
#  Iterate over two for loops (nested for loop)
#  ============================================================================================================================================


for i in range(1, 13):        # outer loop
    for j in range(1, 13):    # inner loop
        print('{0} times {1} is {2}'.format(j, i, i*j), end='\n')
    print('\n')

#  ============================================================================================================================================

#  ============================================================================================================================================
#  Iterate over a loop with a for and check values with an IF statement
#  ============================================================================================================================================

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print(char, end='')


#  ============================================================================================================================================


#  ============================================================================================================================================
#  Use a for loop to iteration of a sliced range of numbers
#  ============================================================================================================================================

print()
# Start at 50
# End at 80
# Step up in sevens

for i in range(101)[50:80:7]:
    print(i)

#  ============================================================================================================================================


#  ============================================================================================================================================
#  Use a for loop with an else
#  ============================================================================================================================================

numbers = [1, 31, 17, 8, 45, 23]

for number in numbers:
    if number % 8 == 0:
        print('a number is divisible by 8')
        break
else:
    print('none of the numbers is divisible by 8 so all good')
    print(numbers)

#  ============================================================================================================================================


#  ============================================================================================================================================
#  Use a for loop with continue
#  ============================================================================================================================================

shopping_list = ["revels", "nibbles", "mandms", "buttons", "galaxy"]
for item in shopping_list:
    if item == 'buttons':
        print('buttons is being skipped')
        continue
    print("buy "+item)
print()
#  ============================================================================================================================================

#  ============================================================================================================================================
#  Use a for loop with break
#  ============================================================================================================================================

shopping_list = ["revels", "nibbles", "mandms", "buttons", "galaxy"]
for item in shopping_list:
    if item == 'buttons':
        print('buttons is being skipped')
        break
    print("buy "+item)

#  If the number is more than zero and divisible by zero (a whole number) then print - loop ends at 77 as it breaks
for i in range(0, 200, 7):
    if i > 0 and i % 11 == 0:
        print(i)
        break

#  ============================================================================================================================================
#  Iterate over the length of a list to locate an item
#  ============================================================================================================================================

shopping_list = ["revels", "nibbles", "buttons", "buttons", "galaxy"]
item_to_find = 'galaxy'
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        print(index)
        break

#  ============================================================================================================================================
#  Side effects of a for loop
#  ============================================================================================================================================
# A common side effect of using for loops instead of list comprehensions can be seen below,
# basically the problem is that when the for loop terminates number = 6, this then overwrites the number input by the user
# so index_pos gets the numbers index of 6 which is 36
numbers = [1, 2, 3, 4, 5, 6]
squares = []
number = int(input('Please a enter a number, and I"ll tell you the square of it: '))


# for number in numbers:                # number = loop control variable
#     squares.append(number ** 2)       # when the for loop terminates the number value is 6 which means when the code below runs it always gets 36

# index_pos = numbers.index(number)     # get the number of the index position in the numbers list and then
# print(squares[index_pos])             # get the number in the squares list at the same position (the square)

squares = [number ** 2 for number in numbers]  # # with a list comprehension it doesnt matter if there is another variable with the same name
index_pos = numbers.index(number)     # get the number of the index position in the numbers list and then
print(squares[index_pos])             # get the number in the squares list at the same position (the square)


#  ============================================================================================================================================
#  Using 'not in'
#  ============================================================================================================================================
menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["chicken", "chips"]
]

for meal in menu:
    if "spam" not in meal:
        print(meal)

#  ============================================================================================================================================
    # text = ""
    # for arg in args:
    #     text += str(arg) + " "

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

print('Nested for loop')
print('----------------')
for loc in sorted(locations):               # iterate over the locations in key order ie 0-5
    exits_to_destination_1 = []             # create an empty list to hold the exits which are found in
    for xit in exits:                       # for each entry in the exits dictionary
        if loc in exits[xit].values():      # if the values for the entry in the dictionary contains the location id ie 0-5 as above
            exits_to_destination_1.append((xit, locations[xit])) # add a tuple of (entry id, location for that id in locations)
    print('Locations leading to {}'.format(loc), end='\t')  # print the locations for the current entry in the for loop and then restart the loop
    print(exits_to_destination_1)  # print the list for this entry


print('List comprehension inside a for loop:')
for loc in sorted(locations):
    exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
    print('Locations leading to {}'.format(loc), end='\t')
    print(exits_to_destination_2)

print()
#  ============================================================================================================================================

x = 12
expression = 'Twelve' if x == 12 else 'unknown'
print(expression)

for meal in menu:
    print(meal, 'contains sausage' if 'sausage' in meal else 'contains bacon' if 'bacon' in meal else 'default value')

print()

items = set()
for meal in menu:
    for item in meal:
        items.add(item)

print(items)

for meal in menu:
    for item in items:
        if item in meal:
            print('{} contains {}'.format(meal, item))
            break

for x in range(1, 31):
    fizzbuzz = 'fizz buzz' if x % 15 == 0 else 'fizz' if x % 3 == 0 else 'buzz' if x % 5 == 0 else str(x)
    print(fizzbuzz)

for buzz in fizzbuzz:
    print(buzz.center(12, '*'))
#  ============================================================================================================================================





