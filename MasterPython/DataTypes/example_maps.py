import timeit

text = 'what have the romans ever done for us?'


def comp_caps():
    capitals = [char.upper() for char in text]
    return(capitals)

# use map
# maps use a function to iterate over an iterable and build another iterable
def map_caps():
    map_capitals = list(map(str.upper, text))
    return(map_capitals)


def comp_words():
    words = [word.upper() for word in text.split(' ')]
    return(words)

# use map

def map_words():
    map_w = list(map(str.upper, text.split(' ')))
    return(map_w)


# for x in map(str.upper, text.split(' ')):
#     print(x)

if __name__ == '__main__':
    print(comp_caps())
    print(map_caps())
    print(comp_words())
    print(map_words())
    print(timeit.timeit(comp_caps, number=1000))
    print(timeit.timeit(map_caps, number=1000))
    print(timeit.timeit(comp_words, number=1000))
    print(timeit.timeit(map_words, number=1000))

# 1. wrap the methods in a function or in a string to use timeit
# 2. add a call to a REFERENCE for the function (not actually a function CALL, which would require brackets also)