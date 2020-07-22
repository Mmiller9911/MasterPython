#  ============================================================================================================================================
#  Python range()
#  The range() type returns an immutable sequence of numbers between the given start integer to the stop integer.
#  Range() returns a generator-like object that only prints the output on demand. (which is why a for loop or list is often used to read them)
#  ============================================================================================================================================


#  ============================================================================================================================================
#  the range() constructor has two forms of definition:
#  range(stop)
#  range(start, stop[, step])
#  range() Parameters
#  range() takes mainly three arguments having the same use in both definitions:
#  start - integer starting from which the sequence of integers is to be returned
#  stop - integer before which the sequence of integers is to be returned.
#  The range of integers end at stop - 1.
#  step (Optional) - integer value which determines the increment between each integer in the sequence

#  ============================================================================================================================================
#  form 1: Only the stop value is specified
#  stop - integer before which the sequence of integers is to be returned.
#  The range of integers end at stop - 1.
range_with_just_stop_value = range(1000)
print(range_with_just_stop_value)  # description of the range
for i in range_with_just_stop_value:
    print(i)

print(range(100))
#  ============================================================================================================================================

#  ============================================================================================================================================
#  form 2: range(start, stop[, step])
#  start - integer starting from which the sequence of integers is to be returned
#  stop - integer before which the sequence of integers is to be returned.
#  The range of integers end at stop - 1.
#  step (Optional) - integer value which determines the increment between each integer in the sequence
range_with_start_stop_and_step = range(50, 100, 2)
print(range_with_start_stop_and_step)  # description of the range
for i in range_with_start_stop_and_step:
    print(i)

start = 2
stop = -14
step = -2

print(list(range(start, stop, step)))

#  ============================================================================================================================================

# empty range
print(list(range(0)))

# using range(stop)
print(list(range(10)))

# using range(start, stop)
print(list(range(1, 10)))

evens = list(range(0, 1000, 2))
odds = list(range(1, 1000, 2))
print(odds)
print(evens)

#  Note: We've converted the range to a Python list, as range() returns a generator-like object that only prints the output on demand.

#  ============================================================================================================================================


#  ============================================================================================================================================
#  Iterating over different types of RANGES using a FOR loop
#  ============================================================================================================================================

for i in range(0, 10):
    print(i)

r = range(0, 100)
for i in r[::-2]:
    print(i)

for i in range(5, 10):
    print(i)

for i in range(3):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(10, 0, -2):
    print(i)

for i in range(0, 101, 7):
    print(i)

for i in range(101)[::7]:
    print(i)

decimals = range(0, 100)
my_sliced_range = decimals[3:40:3]    #print all values between 3 and 39 which are divisible by 3
print(my_sliced_range)

for i in my_sliced_range:
    print(i)

for i in range(3, 40, 3):
    print(i)
#
#  ============================================================================================================================================
#  Getting a value from a range
#  ============================================================================================================================================

odd = range(1, 1000, 2)
print(odd[0])
print(odd[4])
print(odd[20])

ten = range(0, 10)
my_range = ten[::2]
for x in my_range:
    print('value in x is: ' + str(x))
print(my_range.index(6))  # returns 3 (position of 6 in the range)

#  ____________________________________________________________________________________________________________________________________________

#  ============================================================================================================================================
#  Comparing two range to each other
#  ============================================================================================================================================

#  These return true as the results of the ranges are the same
print(range(0, 5, 2) == range(0, 6, 2))
print(range(0, 100) [::-2] == range(99, 0, -2))

#  ____________________________________________________________________________________________________________________________________________
# sevens = range(7, 1000000, 7)
# x = int(input('please enter a number up to a million - '))
# if x in sevens:
#     print('{}, is divisible by 7'.format(x))




