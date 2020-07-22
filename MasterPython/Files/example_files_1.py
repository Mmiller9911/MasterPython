

# Access Modes	Description
# r	Opens a file for reading only.
# rb	Opens a file for reading only in binary format.
# r+	Opens a file for both reading and writing.
# rb+	Opens a file for both reading and writing in binary format.
# w	Opens a file for writing only.
# wb	Opens a file for writing only in binary format.
# w+	Opens a file for both writing and reading.
# wb+	Opens a file for both writing and reading in binary format.
# a	Opens a file for appending.
# ab	Opens a file for appending in binary format.
# a+	Opens a file for both appending and reading.
# ab+	Opens a file for both appending and reading in binary format.

#  ============================================================================================================
#  Reading a file
#  ============================================================================================================

file = open('sample.txt', 'r')
for line in file:
    if 'jabberwock' in line.lower():
        print(line, end='')  # end='' prevents print from printing a new line character after each row of the results
file.close()

#  ============================================================================================================

#  ============================================================================================================
#  Reading a file and make it close when finished (using with keyword)
#  ============================================================================================================
print('*' * 40)
with open('sample.txt', 'r') as jabber:
    for line in jabber:
        if 'jabberwock' in line.lower():
          print('test ' + line, end='')


#  ============================================================================================================

#  ============================================================================================================
#  Read a file and make print a line
#  ============================================================================================================
print()
print('*' * 40)
with open('sample.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()

#  ============================================================================================================
#  Read a file and make print all lines (including newlines)
#  ============================================================================================================
print()
with open('sample.txt', 'r') as jabber:
    lines = jabber.readlines()
print(lines)

# for line in lines:
#     print(line, end='')

#  ============================================================================================================
#  Amend a file and then print all lines
#  ============================================================================================================

with open('samples.txt', 'a') as tables:
    for i in range(2, 13):
        for j in range(1, 13):
            print('{1} times {0} is {2}'.format(i, j, i*j), file=tables)
        print('-' * 20, file=tables)
print()
with open('samples.txt', 'r') as tables:
    line = tables.readline()
    while line:
        print(line, end='')
        line = tables.readline()
#  ============================================================================================================
#  Read and write a binary file
#  ============================================================================================================


with open('binary', 'bw') as bin_file: #binary/write
    for i in range(17):
        bin_file.write(bytes([i])) #convert to bytes before writing to the file

with open('binary', 'br') as bin_file_2:
    for b in bin_file_2:
        print(b)

#  ============================================================================================================


a = 65534 #ff fe
b = 65535 #ff ff
c = 65536 #00 01 00 00
x = 2998302 #02 2D c0 ie

with open('binary3', 'bw') as bin_file_3:
    bin_file_3.write(a.to_bytes(2, 'big'))
    bin_file_3.write(b.to_bytes(2, 'big'))
    bin_file_3.write(c.to_bytes(4, 'big'))
    bin_file_3.write(x.to_bytes(4, 'big'))
    bin_file_3.write(x.to_bytes(4, 'little'))

with open('binary3', 'br') as bin_file_3:
    f = int.from_bytes(bin_file_3.read(2), 'big')
    print(f)
    g = int.from_bytes(bin_file_3.read(2), 'big')
    print(g)
    h = int.from_bytes(bin_file_3.read(4), 'big')
    print(h)
    i = int.from_bytes(bin_file_3.read(4), 'big')
    print(i)
    j = int.from_bytes(bin_file_3.read(4), 'big')
    print(j)

#  ============================================================================================================
#  Write to a text file and then read it
#  ============================================================================================================
cities = ['london', 'newcastle', 'leeds', 'coventry', 'york']

with open('cities.txt', 'w') as city_file:
    for city in cities:
        print(city, file=city_file)

cities = []
with open('cities.txt', 'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))

print(cities)
for city in cities:
    print(city)

#  ============================================================================================================

imelda = 'more mayhem', 'imelda may', '2011', (
    (1, 'pulling the rug'), (2, 'psycho'), (3, 'mayhem'), (4, 'kentish town nwaltz'))

with open('imelda3.txt', 'w') as imelda_file:
    print(imelda, file=imelda_file)

with open('imelda3.txt', 'r') as imelda_file:
    contents = imelda_file.readline()
    print(contents, end='')

imelda = eval(contents)
print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)

#  ============================================================================================================

file = open('test.txt')

line = file.readline()
while line != '':  # exit when no more lines
    print(line)
    line = file.readline()

for line in file.readlines():  # this converts all the lines into a list and then iterates over them
    print(line)
file.close()

#  ============================================================================================================
print()
with open('test.txt', 'r') as new_reader:
    file_content = new_reader.readlines()
    with open('test.txt', 'w') as new_writer:
        for line in reversed(file_content):
            new_writer.write(line)

#  ============================================================================================================
