#  ============================================================================================================================================
#  Tuple
#  A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
#  A list and tuple are basically the same, the difference is that a list is mutable and a tuple is immutable (and the brackets)
#  Tuples are immuteable (the tuple object cannot be changed after creation) - this doesnt mean that the variable cannot be assigned a new object of the same type
#  Tuples DON'T require brackets but it is good practice
#  Tuples are not homogenous meaning they can contain items of different types
#  Make sense for storing things which are never going to change as items in a tuple are not meant to change and that gives extra protections.
#  ============================================================================================================================================

#  ============================================================================================================================================
#  Negative Indexing
#  ============================================================================================================================================
#  Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.

#  Example
#  Print the last item of the tuple:


thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
print(thistuple[-2])

#  _________________________________________________________________________________


#  ============================================================================================================================================
#  Range of Indexes
#  ============================================================================================================================================
#  You can specify a range of indexes by specifying where to start and where to end the range.
#
#   When specifying a range, the return value will be a new tuple with the specified items.

#  Example
#  Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#  ____________________________________________________________________________________________________________________________________________


#  ============================================================================================================================================
#   Updating a tuple
#   Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#
#   But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
#  ============================================================================================================================================

#  Example
#  Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#  ____________________________________________________________________________________________________________________________________________


#  ============================================================================================================================================
#   Check if Item Exists
#   To determine if a specified item is present in a tuple use the in keyword:
#  ============================================================================================================================================
#  Example
#  Check if "apple" is present in the tuple:

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
#  ____________________________________________________________________________________________________________________________________________


#  ============================================================================================================================================
#   Check length of tuple
#  ============================================================================================================================================
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#  ____________________________________________________________________________________________________________________________________________

#  ============================================================================================================================================
#   Create Tuple With zero items
#   To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

#  ============================================================================================================================================

thistuple = ()
print(type(thistuple))
#  ____________________________________________________________________________________________________________________________________________


#  ============================================================================================================================================
#   Create Tuple With One Item
#   To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

#  ============================================================================================================================================
#  One item tuple, remember the commma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#  ____________________________________________________________________________________________________________________________________________


#  ============================================================================================================================================
#   Remove Items
#   Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:

#  ============================================================================================================================================
thistuple = ("apple", "banana", "cherry")
del thistuple
#  print(thistuple) #this will raise an error because the tuple no longer exists
#  ____________________________________________________________________________________________________________________________________________


#  ============================================================================================================================================
#   Join Two Tuples together
#  ============================================================================================================================================
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#  ____________________________________________________________________________________________________________________________________________


#  ============================================================================================================================================
#   Use the tuple() constructor to make a tuple.
#  ============================================================================================================================================
thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)
#  ____________________________________________________________________________________________________________________________________________

#  ============================================================================================================================================
#   Use the tuple() count to return the number of occurrences in a tuple
#  ============================================================================================================================================
thistuple = tuple(("apple", "banana", "cherry", "apple"))  # note the double round-brackets
print(thistuple.count('apple'))
#  ____________________________________________________________________________________________________________________________________________

#  ============================================================================================================================================
#   Use the tuple() index to return the first occurrence of a value in a tuple
#  ============================================================================================================================================
thistuple = tuple(("apple", "banana", "cherry", "apple"))  # note the double round-brackets
print(thistuple.index('cherry'))
#  ____________________________________________________________________________________________________________________________________________

#  ============================================================================================================================================
#   Named tuples
#   Named tuples provide all the usual tuple functionality plus additional ones: *
#   _replace allows a field to be replaced and a new tuple created
#   You can use dot notation
#   The idea is that it is the same as a normal tuple but much more readable because of the dot notation
#   A named tuple is intended to be a compromise between a standard tuple and a dictionary
#  ============================================================================================================================================
from DataTypes.example_named_tuples import plants_list, basic_plants_list

# Plant = namedtuple('Plant', ['name', 'scientific_name', 'lifecycle', 'plant_type'])
# Variable =          Tuple name [fields]

# PlantDetails = namedtuple('PlantDetails', ['scientific_name', 'lifecycle', 'plant_type'])

# basic_plants_list = [
#     ("Andromeda", "Pieris japonica", "Evergreen", "Shrub"),
#     ("Bellflower", "Campanula", "perennial", "Flower"),
#     ("China Pink", "Dianthus", "Perennial", "Flower"),
# ]
#
# plants_list = [
#     Plant("Andromeda", "Pieris japonica", "Evergreen", "Shrub"),
#     Plant("Bellflower", "Campanula", "perennial", "Flower"),
# ]
#
# plants_dict = {
#     "Andromeda": PlantDetails("Pieris japonica", "Evergreen", "Shrub"),
#     "Bellflower": PlantDetails("Campanula", "Annual, biennial, perennial", "Flower"),
# }

print('*' * 40)
print(plants_list[0])  # prints the name of the tuple, plus the tuple fields and values
print(plants_list[1])
print('*' * 40)
for plant in plants_list:
    print(plant.name, plant.scientific_name, plant.plant_type, plant.lifecycle)
    print(plant[0], plant[1], plant[3], plant[2])
    if plant.name == 'Bellflower':
        break

print('*' * 40)

for plant in basic_plants_list:
    print('the values for each basic entry are {} {} {} {}'.format(plant[0], plant[1], plant[2], plant[3]))
print('*' * 40)

example = plants_list[0]
example = example._replace(name='Matt the Hat',scientific_name='Hat', lifecycle='MyReplacementText', plant_type='Cool')
print(example)
print(type(example))
print('*' * 40)

print(example.name)

print('*' * 40)

#  ____________________________________________________________________________________________________________________________________________

#  ============================================================================================================================================
#  Unpacking a tuple
#  ============================================================================================================================================

welcome = 'Welcome to my nightmare', 'Alice Cooper', 1975
bad = 'Bad Company', 'Bad Company', 1974
budgie = 'nightflight', 'budgie', 1981
oasis = 'live forever', 'definately maybe', 1994
blur = 'song 2', 'blur', 1993

#  unpacking the tuple
song, album, year = blur
print(song)
print(album)
print(year)
#  ____________________________________________________________________________________________________________________________________________
#  unpacking the tuple which contains another tuple
take_that = 'take', 'that', 1990, ((1, 'back for good'), (2, 'another'),(3, 'dancer'))
first, second, year, songs = take_that
print(take_that)
print(songs)
#  ____________________________________________________________________________________________________________________________________________
#  unpacking the tuple which contains another tuple and then unpacking that
take_that_songs = 'take', 'that', 1990, (1, 'back for good'), (2, 'another'), (3, 'dancer')
first1, second1, year1, song1, song2, song3 = take_that_songs
print(first1, second1, year1, song1, song2, song3)
print(song3)
#  ____________________________________________________________________________________________________________________________________________
#  unpacking the tuple which contains another tuple of tuples and then unpacking that
imelda = 'More Mayhem', 'Imelda May', 2011, ((1, 'pulling the rug'), (2, 'pyscho'), (3, 'mayhem'), (4, 'kentish town waltz'))

album, artist, year, songs = imelda
print('the album {} by {} was released in {}'.format(album, artist, year))
for song in songs:
    track, song = song
    print('\ttrack number {} is {}'.format(track, song))
#  ____________________________________________________________________________________________________________________________________________
#  adding values to a tuple (containing a list with tuples inside)
#  the tuples themselves are not updated as they are immutable but the lists are not

imelda = 'More Mayhem', 'Imelda May', 2011, ([(1, 'pulling the rug'), (2, 'pyscho'),(3, 'mayhem'),(4, 'kentish town waltz')])
print(imelda)

imelda[3].append([5, 'extra'])  # Add a song to the imelda tuple

album, artist, year, songs = imelda
songs.append((6, 'eternity'))    # Add a song to the unpacked songs tuple from the imelda tuple
for song in songs:
    track, title = song
    print('\ttrack number {} is {}'.format(track, title))
#  ____________________________________________________________________________________________________________________________________________

# convert a list comprehension into a tuple
inch_measurement = (3, 8, 20)
cm_measurement = tuple([inch * 2.54 for inch in inch_measurement])
print(cm_measurement)

#  ____________________________________________________________________________________________________________________________________________











