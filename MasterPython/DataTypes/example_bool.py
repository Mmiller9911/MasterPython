
#  ============================================================================================================================================
#  Boolean Values
#  In programming you often need to know if an expression is True or False.
#  You can evaluate any expression in Python, and get one of two answers, True or False.
#  When you compare two values, the expression is evaluated and Python returns the Boolean answer
#  Almost any value is evaluated to True if it has some sort of content.
#  Any string is True, except empty strings.
#  Any number is True, except 0.
#  Any list, tuple, set, and dictionary are True, except empty ones.
#  ============================================================================================================================================


print("Values interpreted as False in Python")
print("""False: {0}
None: {1}
0: {2}
0.0: {3}
empty list []: {4}
empty tuple (): {5}
empty string '': {6}
empty string "": {7}
empty mapping {{}}: {8}
""".format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))


#  ============================================================================================================================================

print("Values interpreted as True in Python")
print("""True: {0}
1 > 0: {1}
1: {2}
0.1: {3}
list with a value['a']: {4}
tuple with a value('a', 'b'): {5}
string with a value'yeah': {6}
""".format(True, 1 > 0, bool(1), bool(0.1), bool(['a']), bool(('a', 'b')), bool('yeah')))