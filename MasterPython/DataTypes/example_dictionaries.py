#  ============================================================================================================================================
#  are unordered
#  contain key-value pairs
#  values accessed by keys
#  values/keys do not have to be the same format
#  if you add two keys with the same key the last one will be used
#  if iterating over the key/values it is always more efficient to use the keys than the values
#  # #print(dictionary_of_players['graham']) #returns a key error as key not in dictionary
#  ============================================================================================================================================


dictionary_of_players = {'casilla': 'keeper',
                         'cooper': 'defender',
                         'phillips': 'midfielder',
                         'bamford': 'striker',
                         'bielsa': 'genius',
                         'batty': 'four'
}
diff_valued_dict = {1: 'keeper',
                    'defender': 6,
                    4: 6,
                    'key': 'secret'}
print(diff_valued_dict)
print(diff_valued_dict['key'])
print(diff_valued_dict[1])

#  ============================================================================================================================================
#  Display The full Dictionary
#  ============================================================================================================================================
print(dictionary_of_players)
#  ============================================================================================================================================


#  ============================================================================================================================================
#  Display The Dictionary value for a key
#  ============================================================================================================================================
print(dictionary_of_players['cooper'])
#  ============================================================================================================================================


#  ============================================================================================================================================
#  Add an entry to the dictionary
#  ============================================================================================================================================
dictionary_of_players['key'] = 'value'
#  ============================================================================================================================================


#  ============================================================================================================================================
#  Delete an entry from the dictionary
#  ============================================================================================================================================
#del dictionary_of_players['casilla']
#  ============================================================================================================================================


#  ============================================================================================================================================
#  Delete all entries from the dictionary
#  ============================================================================================================================================
#dictionary_of_players.clear()  #empty
#del dictionary_of_players  #delete
#  ============================================================================================================================================

#  ============================================================================================================================================
#  Display all entries from the dictionary
#  ============================================================================================================================================
for player in dictionary_of_players:
    print(player)

for player in dictionary_of_players:
    print([player])
#  ============================================================================================================================================


#  ============================================================================================================================================
#  Print all keys or values
#  ============================================================================================================================================
for val in dictionary_of_players.values():
    print(val)

for val in dictionary_of_players.keys():
    print(val)

#  ============================================================================================================================================
#  Print all items in the dictionary
#  ============================================================================================================================================
print(dictionary_of_players.items())


#  ============================================================================================================================================
#  Update and copy a dictionary
#  ============================================================================================================================================


fruit = {'orange': 'a, sweet, orange, citrus fruit',
         'apple': 'good for making cider'}

veg = {'cabbage': 'every child\'s favourite',
       'sprouts': 'mmmm, lovely'}


veg.update(fruit)  #  copy the fruit dictionary into the veg dictionary
fruit.update(veg)
print(veg)
print(fruit)
nice = fruit.copy()
print(nice)

#  ============================================================================================================================================

#  ============================================================================================================================================
#  Convert a dictionary into a list and then back so the values can be ordered
#  ============================================================================================================================================
order_dict = list(dictionary_of_players.keys())
order_dict.sort()
print(order_dict)

ordered_keys = sorted(list(dictionary_of_players.keys()))

for player in ordered_keys:
    print(player + ' - ' + dictionary_of_players[player])
#  ============================================================================================================================================

#  ============================================================================================================================================
#  Convert a dictionary into a tuple and then back
#  ============================================================================================================================================
print(dictionary_of_players.items())
p_tuple = tuple(dictionary_of_players.items())
print(p_tuple)
print(dict(p_tuple))
#  ============================================================================================================================================


#  ============================================================================================================================================
#  Get a value from the dictionary - using dictionary.get
#  ============================================================================================================================================

while True:
    dict_key = input('please enter a key ')
    if dict_key == 'quit':
        break
    #description = dictionary_of_players['p']
    description = dictionary_of_players.get(dict_key, 'the value passed in was ' + '\"' + dict_key + '\"' + ' which is not present in the dictionary')
    # dictionary_of_players.get returns none if value is not present unlike dictionary[key] which returns  - # KeyError: 'p'
    print(description)
#  ============================================================================================================================================

#  ============================================================================================================================================
#  The game
#  ============================================================================================================================================

# locations = {0: {"desc": "You are sitting in front of a computer learning Python",
#                  "exits": {},  #each location with the dictionary has three sub-dictionaries
#                  "namedExits": {}},
#              1: {"desc": "You are standing at the end of a road before a small brick building",
#                  "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#                  "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
#              2: {"desc": "You are at the top of a hill",
#                  "exits": {"N": 5, "Q": 0},
#                  "namedExits": {"5": 5}},
#              3: {"desc": "You are inside a building, a well house for a small stream",
#                  "exits": {"W": 1, "Q": 0},
#                  "namedExits": {"1": 1}},
#              4: {"desc": "You are in a valley beside a stream",
#                  "exits": {"N": 1, "W": 2, "Q": 0},
#                  "namedExits": {"1": 1, "2": 2}},
#              5: {"desc": "You are in the forest",
#                  "exits": {"W": 2, "S": 1, "Q": 0},
#                  "namedExits": {"2": 2, "1": 1}}
#              }
#
# vocabulary = {"QUIT": "Q",
#               "NORTH": "N",
#               "SOUTH": "S",
#               "EAST": "E",
#               "WEST": "W",
#               "ROAD": "1",
#               "HILL": "2",
#               "BUILDING": "3",
#               "VALLEY": "4",
#               "FOREST": "5"}
#
# loc = 1
# while True:
#     availableExits = ", ".join(locations[loc]["exits"].keys())
#
#     print(locations[loc]["desc"]) #print the sub-dictionary desc of the selected location
#
#     if loc == 0:
#         break
#     else:
#         allExits = locations[loc]["exits"].copy()
#         allExits.update(locations[loc]["namedExits"])
#
#     direction = input("Available exits are " + availableExits).upper()
#     print()
#
#     # Parse the user input, using our vocabulary dictionary if necessary
#     if len(direction) > 1:  # more than 1 letter, so check vocab
#         words = direction.split()
#         for word in words:
#             if word in vocabulary:   # does it contain a word we know?
#                 direction = vocabulary[word]
#                 break
#
#     if direction in allExits:
#         loc = allExits[direction]
#     else:
#         print("You cannot go in that direction")

#  ============================================================================================================================================