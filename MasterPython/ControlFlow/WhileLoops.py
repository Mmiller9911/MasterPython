#  ============================================================================================================================================
#  While Loops
#  ============================================================================================================================================
#  while is used to check a condition is true or not
#  whiles are useful when you have no idea how many times the loop will execute and it might not at all
#  whiles are especially useful for reading data from a file as you probably wont know how much data is in it beforehand
#  i must be initialised before the loop runs

# There are two different uses for "ELSE" in python:
# 1.  In an IF statement it represents a statement which will execute if none of the other statements are True
# 2.  In FOR/WHILE/TRY loops it is executed if the previous code executed successfully

#  ============================================================================================================================================
#  Standard while loop
#  ============================================================================================================================================

i = 0
while i < 10:
    print('i is now {}'.format(i))
    i += 1

i = 0
while i < 15:
    i += 1
    print(i)

print()
i = 5
while i > 1:
    if i == 2:
        break
    print(i)

    i -= 1

print()

#  ============================================================================================================================================
#  Another standard while loop
#  ============================================================================================================================================


available_exits = ['north', 'south', 'east', 'west']
chosen_exit = ''

while chosen_exit not in available_exits:
    chosen_exit = input('please choose a direction ')
    if chosen_exit.casefold() == 'quit':
        print('Game Over')
        break
else:
    print("aren\'t you glad you are out!")

#  ============================================================================================================================================
#  Another standard while loop
#  ============================================================================================================================================

value = 10

while value > 1:
    if value == 9:
        value = value - 1
        continue  # only skips the specific iteration of the loop
    if value == 3:
        break     # exit the loop entirely
    print(value)

    value = value - 1

#  ============================================================================================================================================