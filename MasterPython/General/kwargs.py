# def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
# **kwargs allows a method to pass through parameters without


# # def print_backwards(*args, end=' ', **kwargs): # define the function to accept kwargs
# def print_backwards(*args, **kwargs): # define the function to accept kwargs
#     print(type(kwargs)) # kwargs are added as a dictionary object
#     kwargs.pop('end', None)  # remove end from the dictionary first (before passing it through with kwargs)
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs) # pass kwargs onto the print function - the calling code can add as many onwards keywords/values
#                                     # we dont need to know what they are nor whats their defaults are


def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)

backwards_print('Harmony')


# def print_backwards(*args, **kwargs):
#     end_character = kwargs.pop('end', '\n')
#     sep_character = kwargs.pop('sep', ' ')
#     for word in args[:0:-1]:
#         print(word[::-1], end=sep_character, **kwargs)
#     print(args[0][::-1], end=end_character, **kwargs) # print the first word seperately
#
#
# with open('backwards.txt', 'w') as backwards:
#     print_backwards('hello', 'planet', 'earth', 'take', end='\n')
#     print('Another string')
#
# print()
# print('hello', 'planet', 'earth', 'take', end='', sep='\n**\n')
# print_backwards('hello', 'planet', 'earth', 'take', end='', sep='\n**\n')
# print('-' * 50)


# print('hello','world')
# def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
# *args means this method can take a variable number of arguments which will be scooped up into a tuple
# values passed to the method are then packed into a tuple and *args represents the unpacked values in that tuple
# the print function takes all the values from the passed tuple and then prints them


def average(*args):      #def average(args): # *args represents the unpacked tuple so - args represents the tuple
    print(type(args))                        # returns = <class 'tuple'>
    print('args is {}'.format(args))         # returns = args is (10, 10, 10, 10)
    print('*args is:',*args)                 # returns = *args is: 10 10 10 10
    mean = 0
    for arg in args:
        mean += arg
    return mean /len(args)


print(average(10,10,10,10)) # print(average((10,10,10,10))) if using the args param a tuple of arguments must be passed instead of just the arguments

print('-' * 50)


def build_tuple(*args):
    return args


message_tuple = build_tuple('hello','this','is','a','test')
number_tuple = build_tuple(1, 7, 8, 11, 56)

print(type(message_tuple))
print(message_tuple)

print(type(number_tuple))
print(number_tuple)


def return_smallest_number(*args):
    numbers = []
    print(*args)
    print(args)
    for arg in args:
        numbers.append(arg)
    numbers.sort()
    return numbers[0]


print('-' * 50)
print(return_smallest_number(4, 27, 3, 56, 167))

print('-' * 50)

words = ['one', 'two', 'seventy-four']
print(words)
print(*words)  #this has unpacked the list

