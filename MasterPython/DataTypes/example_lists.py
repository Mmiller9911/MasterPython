#  ============================================================================================================================================
#  LISTS
#  A list is a sequence of things
#  A list could be a string, int, class or even another list
#  If two lists are ordered differently then they are NOT equal
#  A list object is mutable - can be updated after creation
#  Lists are homogenous meaning they contain items of the same type

#  ============================================================================================================================================


#  animals = ['cat', 'bear', 'frog', 'mouse', 'dear']
animals = ['cat', 'bear', 'frog', 'mouse', 'dear', 'tony']
for animal in animals:
    print('it is a ' + animal)

even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7]
numbers = odd + even
# numbers.sort()
print(numbers)
sorted_numbers = sorted(numbers)

if numbers == sorted_numbers:
    print('they are the same')
if numbers != sorted_numbers:
    print('they are the not same because they are ordered differently')

#  ____________________________________________________________________________________________________________________________________________

list_1 = []
list_2 = list()
print(list('list the lists are equal'))

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
# another_even = even               # if the construcutor is NOT used as here the lists will be equal
another_even = list(even)          # if the construcutor is used as here a new list is created
print(another_even is even)        # are the lists the same object?
print(another_even == even)        # do the contents match
another_even.sort(reverse=True)
print(even)
all_numbers = [odd, even]  #list of lists
print(all_numbers)

for number_set in all_numbers:
    print(number_set)

    for number in number_set:
        print(number)

#  ____________________________________________________________________________________________________________________________________________

menu = []
menu.append(['egg', 'bacon', 'sausage'])
menu.append(['egg', 'bacon', 'spam'])
menu.append(['egg', 'bacon', 'tomato'])
menu.append(['spam', 'bacon', 'tomato'])
menu.append(['egg', 'bacon', 'tomato', 'spam'])
menu.append(['egg', 'bacon', 'tomato', 'spam', 'sausage'])
menu.append(['egg', 'spam', 'tomato', 'spam', 'sausage', 'spam'])

print(menu)
print('-' * 40)
for meal in menu:
    if not 'spam' in meal:
        print(meal)
        print('-' * 40)
        for ingrediant in meal:
          print(ingrediant)

#  ____________________________________________________________________________________________________________________________________________
#  Get last value in the list
#  ____________________________________________________________________________________________________________________________________________
print_last_entry = [2, 4, '5']
print(print_last_entry[-1])

#  ____________________________________________________________________________________________________________________________________________
#  Get a slice of the list
#  ____________________________________________________________________________________________________________________________________________

print_last_entry = [2, 4, '5', 8, 'f']
print(print_last_entry[1:3])  # exclusive

#  ____________________________________________________________________________________________________________________________________________
#  Insert an entry at a point in the list
#  ____________________________________________________________________________________________________________________________________________

print_last_entry = [2, 4, '5', 8, 'f']
print_last_entry.insert(2, 'Miller')
print(print_last_entry[0:len(print_last_entry)])

#  ____________________________________________________________________________________________________________________________________________
#  Insert an entry to the end of the list
#  ____________________________________________________________________________________________________________________________________________

print_last_entry = [2, 4, '5', 8, 'f']
print_last_entry.append('Endy')
print(print_last_entry[0:len(print_last_entry)])

#  ____________________________________________________________________________________________________________________________________________
#  Update an entry in the list
#  ____________________________________________________________________________________________________________________________________________

print_last_entry[1] = 100
print(print_last_entry[0:len(print_last_entry)])
#  ____________________________________________________________________________________________________________________________________________
#  Delete an entry in the list
#  ____________________________________________________________________________________________________________________________________________

del print_last_entry[1]
print(print_last_entry[0:len(print_last_entry)])
#  ____________________________________________________________________________________________________________________________________________

