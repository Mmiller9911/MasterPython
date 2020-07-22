
#  ============================================================================================================================================
# Adding a TODO comment like the one below means that intelliJ will track the comment for you (in the todo section of the run window)
# raise AttributeError('testing attrubte error') # TODO remove before release
#  ============================================================================================================================================


#  ============================================================================================================================================
# Variables are within the scope of:
# * global namespace
# * class namespace
# * functions namespace

#  Variables - must begin with a letter or underscore
#  Are created when they are assigned a value
#  Are case-sensitive


# Python allows you to change the data type of variables on the fly unlike other languages such as java.
#
# greeting = 'greetings!'
# age = 17
#
# print (type(greeting))
# print (type(age))
#
# age = 'stringmcstringface'
# print (type(age))
#  ============================================================================================================================================

#  Docstrings can be added as below
# class Song:
#     """Class to represent a song
#
#     title(str) - title of the song
#     artist(Artist) - song creator
#     duration(int) - duration in seconds may be 0
#
#     """
#  ============================================================================================================================================

#  Garbage collection and circular references
# Circular references eg.
# an object references another object and the object in turn references it.
#
# These are to be avoided wherever possible, a process exists called garbage collection which will attempt to clear redundant data and this may cause issues.

#  ============================================================================================================================================

# Function annotations/ Type hints
# These are used so the calling method is aware of the type of param to pass and the return type
# The hints are not mandatory but it makes sense to include them for everything or nothing
#     def add_duck(self, duck: Duck) -> None:
#         self.flock.append(duck)

#  ============================================================================================================================================

# Python does not allow overloaded methods but it is possible to achieve the same results
# with methods which have named defaults (this will use the passed params and defaults if needed) ie.:
# class Troll:
#
#     def __init__(self, name='Enemy', hit_points=0, lives=1):
#         self.name = name
#         self.hit_points = hit_points
#         self.lives = lives
#
# ugly_troll = Troll()
# print('Ugly troll is {}'.format(ugly_troll))
#
# another_troll = Troll('another', 20, 30)
# print('Another troll is {}'.format(another_troll))
#
# brother_troll = Troll('BrotheyMcDo', 400)
# print('Brother Troll is {}'.format(brother_troll))
#  ============================================================================================================================================


# Python will automatically run any modules which it imports
#
# print(__name__) - this command prints the name of the executing class
#
# this test can be added and the code indented to prevent the code executing in another class if it only needs importing (within the class itself it will execute fine)
#
# if __name__ == '__main__':
#
# if the code in the called module is setup correctly then it can be modified so that it will only be executed when called:
#
# import BlackJack
#
# print(__name__)
#
# BlackJack.play()
#
# (see final version of blackjack class)

#  ============================================================================================================================================
#  The None keyword
#  ============================================================================================================================================
shopping_list = ["revels", "nibbles", "buttons", "buttons", "galaxy"]
item_to_find = 'galaxy'
found_at = None

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print('item found at position {}'.format(found_at))
else:
    print('{} is not found'.format(item_to_find))

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        print(index)
        break

#  ============================================================================================================================================
#  Print the current file path
print(__file__)
#  ============================================================================================================================================

