# a generator will continue from where it left off after yielding the last value
# a generator can be very useful to create something when the end is not known, such as indexing all the webpages in the world for google
# because only one thing is done at a time (as opposed to a list) the memory usage is very low - a list would be stored in memory

# What are generators in Python?
# There is a lot of overhead in building an iterator in Python;
# we have to implement a class with __iter__() and __next__() method, keep track of internal states, raise StopIteration when there was no values to be returned etc.
#
# This is both lengthy and counter intuitive. Generator comes into rescue in such situations.
# Python generators are a simple way of creating iterators. All the overhead we mentioned above are automatically handled by generators in Python.
# Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

#  Each tuple is created and then control is yielded to create the next tuple

import os

root = "music"

# this gnerator recursively visit every folder from the root and for every one returns a tuple
for path, directories, files in os.walk(root, topdown=True):
    # for f in files:
    #     print("\t{}".format(f))

    # print(path)
    # print(directories)
    # print(files)
    # input()

    if files:
        print(path)
        first_split = os.path.split(path)
        print(first_split)
        second_split = os.path.split(first_split[0])
        print(second_split)
        for f in files:
            song_details = f[:-5].split(' - ')  # strip last 5 chars and remove the hyphen from the filename
            print(song_details)
        print('*' * 40)

        print('*' * 40)

import os
import fnmatch
import id3reader_p3 as id3reader


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)     #create an absolute path
            yield os.path.join(absolute_path, file)


error_list = []
for f in find_music(r'C:\Users\Matt\Downloads\flyandbecalm\flyandbecalm', 'mp3'):
#  for f in find_music('music', 'emp3'):
    try:
        id3r = id3reader.Reader(f)
        print('Artist: {}, Album: {}, Track: {}, Song: {}'.format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title')))
    except:
        error_list.append(f)

for error_file in error_list:
    print(error_list)
