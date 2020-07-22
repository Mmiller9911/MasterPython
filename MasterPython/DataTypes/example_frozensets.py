
#  ============================================================================================================================================
#  The frozenset() is an inbuilt function is Python which takes an iterable object as input and makes them immutable. Simply it freezes the iterable objects and makes them unchangeable.
#  In Python, frozenset is same as set except its elements are immutable. This function takes input as any iterable object and converts them into immutable object. The order of element is not guaranteed to be preserved.
#  Since frozenset object are immutable they are mainly used as keys in a dictionary or elements of other sets
#  ============================================================================================================================================


#
immute_set = frozenset(range(0, 50, 5))
print(immute_set)

# tuple of numbers
nu = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# converting tuple to frozenset
fnum = frozenset(nu)

# printing details
print("frozenset Object is : ", fnum)



# creating a dictionary
Student = {"name": "Ankit", "age": 21, "sex": "Male",
           "college": "MNNIT Allahabad", "address": "Allahabad"}

# making keys of dictionary as frozenset
key = frozenset(Student)

# printing keys details
print('The frozen set is:', key)

