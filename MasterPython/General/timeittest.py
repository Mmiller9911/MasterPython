# can be run via command line
# import the module and then either use the function or create an instance of the timer class
# the idea is to compare how long different code take in comparison to each other NOT to see how long it takes per se.
# other things which are running on your machine will also affect the results so this should be considered
# things to be timed can be either passed as a string or enclosed as a function
# you cannot use to check functions which require arguments passing in to them

# import timeit
#
# setup = """\
# gc.enable()
# locations = {0: "You are sitting in front of a computer learning Python",
#              1: "You are standing at the end of a road before a small brick building",
#              2: "You are at the top of a hill",
#              3: "You are inside a building, a well house for a small stream",
#              4: "You are in a valley beside a stream",
#              5: "You are in the forest"}
#
# exits = {0: {"Q": 0},
#          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          2: {"N": 5, "Q": 0},
#          3: {"W": 1, "Q": 0},
#          4: {"N": 1, "W": 2, "Q": 0},
#          5: {"W": 2, "S": 1, "Q": 0}}
# """
#
# nested_loop = """\
# for loc in sorted(locations):
#     exits_to_destination_1 = []
#     for xit in exits:
#         if loc in exits[xit].values():
#             exits_to_destination_1.append((xit, locations[xit]))
#     print("Locations leading to {}".format(loc), end='\t')
#     print(exits_to_destination_1)
# """
#
# loop_comp = """\
# for loc in sorted(locations):
#     exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
#     print("Locations leading to {}".format(loc), end='\t')
#     print(exits_to_destination_2)
# """
#
# nested_comp = """\
# exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
#                           for loc in sorted(locations)]
# for index, loc in enumerate(exits_to_destination_3):
#     print("Locations leading to {}".format(index), end='\t')
#     print(loc)
# """
#
# result_1 = timeit.timeit(nested_loop, setup, number=100)
# result_2 = timeit.timeit(loop_comp, setup, number=100)
# result_3 = timeit.timeit(nested_comp, setup, number=100)
# print("Nested loop:\t{}".format(result_1))
# print("Loop and comp:\t{}".format(result_2))
# print("Nested comp:\t{}".format(result_3))

#  ============================================================================================================================================

# import timeit
#
# locations = {0: "You are sitting in front of a computer learning Python",
#              1: "You are standing at the end of a road before a small brick building",
#              2: "You are at the top of a hill",
#              3: "You are inside a building, a well house for a small stream",
#              4: "You are in a valley beside a stream",
#              5: "You are in the forest"}
#
# exits = {0: {"Q": 0},
#          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          2: {"N": 5, "Q": 0},
#          3: {"W": 1, "Q": 0},
#          4: {"N": 1, "W": 2, "Q": 0},
#          5: {"W": 2, "S": 1, "Q": 0}}
#
#
# def nested_loop():
#     result = []
#     for loc in sorted(locations):
#         exits_to_destination_1 = []
#         for xit in exits:
#             if loc in exits[xit].values():
#                 exits_to_destination_1.append((xit, locations[xit]))
#         result.append(exits_to_destination_1)
#         # print the result before returning
#     for x in result:
#         pass
#     return result
#
#
# def loop_comp():
#     result = []
#     for loc in sorted(locations):
#         exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
#         result.append(exits_to_destination_2)
#     for x in result:
#         pass
#     return result
#
#
# def nested_comp():
#     exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
#                               for loc in sorted(locations)]
#
#     for x in exits_to_destination_3:
#         pass
#     return exits_to_destination_3
#
#
# def nested_gen():
#     exits_to_destination_4 = ([[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
#                               for loc in sorted(locations)])
#
#     for x in exits_to_destination_4:
#         pass
#     return exits_to_destination_4
#
#
# print(nested_loop())
# print(loop_comp())
# print(nested_comp())
# print(nested_gen())
#
# result_1 = timeit.timeit(nested_loop, globals=globals(), number=1000)
# result_2 = timeit.timeit(loop_comp, globals=globals(), number=1000)
# result_3 = timeit.timeit(nested_comp, globals=globals(), number=1000)
# result_4 = timeit.timeit(nested_comp, globals=globals(), number=1000)
# print("Nested loop:\t{}".format(result_1))
# print("Loop and comp:\t{}".format(result_2))
# print("Nested comp:\t{}".format(result_3))
# print("Nested gen:\t{}".format(result_4))

#  ============================================================================================================================================

import timeit

# locations = {0: "You are sitting in front of a computer learning Python",
#              1: "You are standing at the end of a road before a small brick building",
#              2: "You are at the top of a hill",
#              3: "You are inside a building, a well house for a small stream",
#              4: "You are in a valley beside a stream",
#              5: "You are in the forest"}
#
# exits = {0: {"Q": 0},
#          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          2: {"N": 5, "Q": 0},
#          3: {"W": 1, "Q": 0},
#          4: {"N": 1, "W": 2, "Q": 0},
#          5: {"W": 2, "S": 1, "Q": 0}}
#
#
# def nested_loop():
#     result = []
#     for loc in sorted(locations):
#         exits_to_destination_1 = []
#         for xit in exits:
#             if loc in exits[xit].values():
#                 exits_to_destination_1.append((xit, locations[xit]))
#         result.append(exits_to_destination_1)
#         # print the result before returning
#     for x in result:
#         pass
#     return result
#
#
# def loop_comp():
#     result = []
#     for loc in sorted(locations):
#         exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
#         result.append(exits_to_destination_2)
#     for x in result:
#         pass
#     return result
#
#
# def nested_comp():
#     exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
#                               for loc in sorted(locations)]
#
#     for x in exits_to_destination_3:
#         pass
#     return exits_to_destination_3
#
#
# def nested_gen():
#     exits_to_destination_4 = ([[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
#                               for loc in sorted(locations)])
#
#     for x in exits_to_destination_4:
#         pass
#     return exits_to_destination_4
#
#
# print(nested_loop())
# print(loop_comp())
# print(nested_comp())
# print(nested_gen())
#
# result_1 = timeit.timeit(nested_loop, globals=globals(), number=1000)
# result_2 = timeit.timeit(loop_comp, globals=globals(), number=1000)
# result_3 = timeit.timeit(nested_comp, globals=globals(), number=1000)
# result_4 = timeit.timeit(nested_comp, globals=globals(), number=1000)
# print("Nested loop:\t{}".format(result_1))
# print("Loop and comp:\t{}".format(result_2))
# print("Nested comp:\t{}".format(result_3))
# print("Nested gen:\t{}".format(result_4))

# fact_test = """\
# def fact(n=1):
#     result = 1
#     if n > 1:
#         for f in range(2, n + 1):
#             result *= f
#     return result
#
# x = fact(130)
# """
#
# factorial_test = """\
# def factorial(n=1):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# y = factorial(130)
#
# """


def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    print(timeit.timeit('x = fact(130)', setup="from __main__ import fact", number=1000))
    print(timeit.timeit('x = factorial(130)', setup="from __main__ import factorial", number=1000))

#  ============================================================================================================================================

from statistics import mean, stdev


def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == '__main__':
    print(timeit.repeat('x = fact(130)', setup="from __main__ import fact", number=1000, repeat=10))
    print(timeit.repeat('x = factorial(130)', setup="from __main__ import factorial", number=1000, repeat=10))
    list_1 = timeit.repeat('x = fact(130)', setup="from __main__ import fact", number=1000, repeat=10)
    list_2 = timeit.repeat('x = factorial(130)', setup="from __main__ import factorial", number=1000, repeat=10)

    print(sum(list_1) / 10)
    print(sum(list_2) / 10)
    print(mean(list_1), stdev(list_1))
    print(mean(list_2), stdev(list_2))

