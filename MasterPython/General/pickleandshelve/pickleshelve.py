# for saving or pickling an object or object
# objects must be loaded back in the same order they are added
# pickle loads should be able to detect the correct protocol to decode objects
# DONT use pickle files from untrusted sources
# shelves are persisted in .db files
# are unsorted entries like a dictionary
# shelve keys MUST be a string (unlike dictionary’s)
# files are pickled when saving and unpickled when loading again, can have performance issues
# basically stores some data that the program needs to run without having SQL db
# can have issues with concurrent writing

# The shelve module implements persistent storage for arbitrary Python objects which can be pickled,
# using a dictionary-like API. The shelve module can be used as a simple persistent storage option
# for Python objects when a relational database is overkill. The shelf is accessed by keys, just as with a dictionary.


#  ============================================================================================================================================
#  Write a tuple in binary to a file named imelda.pickle then read the file and unpack the tuple again
#  ============================================================================================================================================

import pickle
import shelve
#
# imelda = ('More Mayhem',
#            'Imelda May',
#            '2011',
#            ((1, 'song 1'),
#             (2, 'song 2'),
#             (3, 'song 3'),
#             (4, 'song 4')))
#
# print(type(imelda))
#
# with open('imelda.pickle', 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file)
#
# with open('imelda.pickle', 'rb') as pickled_file:
#     imelda2 = pickle.load(pickled_file)
#
# print(imelda2)
#
# album, artist, year, songs = imelda2
#
# print(album + ' ' + artist + ' ' + year)
#
# for track in songs:
#     track_number, track_name = track
#     print(track_number, track_name)

#  ============================================================================================================================================
#  Write two lists and an integer to a pickle file in binary and then decode the values again
#  ============================================================================================================================================

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open('oddsnevens.pickle', 'wb') as pickle_file:
    pickle.dump(even, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(53573333, pickle_file, protocol=0)

with open('oddsnevens.pickle', 'rb') as pickled_file:
    evens = pickle.load(pickled_file)
    odds = pickle.load(pickled_file)
    x = pickle.load(pickled_file)

for i in evens:
    print(i)

print('-' * 40)

for i in odds:
    print(i)

print('-' * 40)

print(x)

#  ============================================================================================================================================

# the with statement will always close the file when the run has finished.
# shelve.close() (only required if not using a with statement to close the shelf)

print()

with shelve.open('shelvetestfile') as fruit:
    fruit['orange'] = 'orange fruit'
    fruit['banana'] = 'yellow fruit'
    fruit['apple'] = 'greenyred fruit'
    fruit['grape'] = 'wine yeah fruit'
    fruit['pineapple'] = 'yummy fruit'

    print(fruit['orange'])
    print(fruit['apple'])

    ordered_keys = list(fruit.keys())
    ordered_keys.sort()

    for f in ordered_keys:
        print(f + '---' + fruit[f])
    for v in fruit.values():
        print(v)

    print(fruit.values())

    for v in fruit.items():
        print(v)

    print(fruit.items())

print()
print(fruit)        # displays the shelf object memory location
print(type(fruit))  # displays the shelf object type
print()

#  ============================================================================================================================================

with shelve.open('abike') as bike:
    bike_keys = []
    bike['make'] = 'harley'
    bike['model'] = 'fast'
    bike['colour'] = 'black'
    bike['engine_size'] = 2.4
    for key in bike:
        print(key)
        bike_keys.append(key)

    for bike_key in bike_keys:
        print(bike[bike_key])

#  ============================================================================================================================================


