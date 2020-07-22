# Overflow exceptions are almost impossible
# The easiest way to check the exception to handle is to cause the expected problem and see what type of error is returned
# finally is always executed even if the program is exited
# else is only executed in this context if the program completes correctly
# It is possible to catch all exceptions using "except Exemption:" but it is better to use a specific error so it can be handled exclusively
# the ordering of exceptions is important as some of them are related (may be sub/super classes of each other)
# if an exception is not handled it will be passed up the stack until it reaches the top of the stack, or the runtime
# Two types: Syntax error Runtime Exceptions


def factorial(n):
    # n! = n * (n-1)!
    if n <= 1:
        return 1
    else:
        print(n/0)
        return n * factorial(n-1)

try:
    print(factorial(1000))
except (RecursionError, ZeroDivisionError):
    print('the factorial provided is too large!')
# except ZeroDivisionError:
#     print('cannot divide by zero!')

print('program complete!')

#  ============================================================================================================================================


import sys


def getint(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print('Invalid number ')
        except EOFError:
            sys.exit(1)
        finally:
            print('the finally clause always executes')


# x = int(input('Enter a number - '))
first_number = getint('please enter a number ')
second_number = getint('please enter another number ')

try:
    print('{} divided by {} is {}'.format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print('cannot divide by zero ')
    sys.exit(2)
else:
    print('Division performed successfully')

# TYPE of exception	       extra details provided
# ZeroDivisionError	       division by zero
# RecursionError	       maximum recursion depth exceeded in comparison
# ValueError	           invalid literal for int() with base 10: 'g'
# EOFError	               EOF when reading a line (control-d on windows ends the stream)
# AttributeError	      'Penguin' object has no attribute 'fly'
# TypeError	               raise TypeError('cannot add duck, are you sure it is not a ' + str(type(duck).name))

# Raise keyword
#
# this is used in one of two ways:
#
# 1. to re-raise the error further up in the call-stack (see below)
# 2. or to specifically raise a type of exception ie - raise AttributeError


def migrate(self):
    problem = None
    for duck in self.flock:
        try:
            duck.fly()
        except AttributeError as e:
            print('One duck down')
            # raise
            problem = e
    if problem:
        raise problem

#OR


raise AttributeError('testing attribute error')  # TODO remove before release