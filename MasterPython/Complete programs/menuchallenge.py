selection = '-'
while selection != '0':
    if selection in '12345':
        print('your selection was {} '.format(selection))
        #selection = int(input())
    else:
        print("""Please select an option from the menu!
        1. Chicken Tikka Madras
        2. Pepperoni
        3. Sweet and Sour chicken
        4. Cheese Burger
        5. Tomato pasta
        0. Exit""")

    selection = input()

# print a list of options
# allow the user to select an option
# should be at least 4 options
# loop will loop while the user has not selected option 0
# the number of the selection shoud be printed in a message to the user
# if a number which is not a selection is chosen, print the orginal menu again
# 0 - exit program
# 1 - curry
# 2 - pizza
# 3 - chinese
# 4 - burger
# 5 - pasta
# invalid

menu = """Please select an option from the menu!
        1. Chicken Tikka Madras
        2. Pepperoni
        3. Sweet and Sour chicken
        4. Cheese Burger
        5. Tomato pasta
        0. Exit"""

print(menu)
selection = int(input())
while True:
    if selection == 0:
        print('Exiting program')
        break
    if selection <= 5:
        print('your selection was {} '.format(selection))
        selection = int(input())
    else:
        print(menu)
        selection = int(input())