# You can roughly think of any and all as series of logical or and and operators, respectively.
#
# any - will return True when at least one of the elements is Truthy.
# all - will return True only when all the elements are Truthy.

# Truth table
#
# +-----------------------------------------+---------+---------+
# |                                         |   any   |   all   |
# +-----------------------------------------+---------+---------+
# | All Truthy values                       |  True   |  True   |
# +-----------------------------------------+---------+---------+
# | All Falsy values                        |  False  |  False  |
# +-----------------------------------------+---------+---------+
# | One Truthy value (all others are Falsy) |  True   |  False  |
# +-----------------------------------------+---------+---------+
# | One Falsy value (all others are Truthy) |  True   |  False  |
# +-----------------------------------------+---------+---------+
# | Empty Iterable                          |  False  |  True   |
# +-----------------------------------------+---------+---------+

# There can be a gotcha with "all" if the list is empty, this would still equate to true
#
# this can be avoided with:

entries = [1, 2, 3, 4, 5]  # = True
# entries = [1, 2, 3, 4, 0]  # = False as a false value is included (0) - see example_bool for more truthy examples

if entries:  # entries are present so entries cannot be an empty iterable
    print('if statement all: {}'.format(all(entries)))
else:
    print('if statement any: {}'.format(any(entries)))


