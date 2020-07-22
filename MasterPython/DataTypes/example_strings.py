#  =========================================================
#  Confirmations
#  A string in python is just an array of bytes
#  There is no character type in python, a character is simply a string with a length of 1
#  =========================================================



#  =========================================================
#  Escaping Strings
#  =========================================================
splitString='this string\nhas been\nsplit\nover several lines\nduuurrrrr'
print(splitString)
tabbedString='1\t2\t3\t4\t5\t'
print(tabbedString)
print('the pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
print("the pet shop owner said \"No, no, 'e's uh,...he's resting\".")
print("""the pet shop owner said "No, no, 'e's uh,...he's resting".""")
anotherSplitString = """
this
string
is
over
several
lines
"""
print(anotherSplitString)

anotherSplitStringWithoutNewLines = """
this \
string \
is \
over \
several \
lines
"""
print(anotherSplitStringWithoutNewLines)
print('Number1\tThe Larch\nNumber2\tThe Horse Chestnut')

print('c:\test\notes')
print('c:\\test\\notes')
print(r'c:\test\notes')

#  =========================================================
#  Joining strings
#  =========================================================
my_list = ['a', 'b', 'c', 'd']
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '123456789'

my_string = ', '.join(my_list)
my_string2 = ', '.join(letters)
my_string3 = ' mississipi '.join(numbers)

for c in my_list:
     my_string += c + ', ' #as strings are immutable, every time the code runs a new string is created

print(my_string)
print(my_string2)
print(my_string3)

#  =========================================================
#  Raw Strings
#  =========================================================

rawstring = r"this is\na string split\t\tand tabbed"
print(rawstring)

#  =========================================================
#  Removing non alphanumeric characters from a string
#  =========================================================
number = '100,464:773@242,666'
seperators = ''

for char in number:
    if not char.isnumeric():
        seperators = seperators + char


print(seperators)

print('*' * 80)

values = ''.join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

#  =========================================================
#  String Interpolation
#  =========================================================
age = 23
print('my age is ' + str(age) + ' years')
print('my age is {0} years'.format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}"
      .format(31, 'Jan', 'Mar', 'May', 'July', 'Aug', 'Oct', 'Dec'))
print("Jan:{0} Feb:{1} Mar:{0} April:{2}".format(31, 28, 30))
print("""
Jan:{0}
Feb:{1}
Mar:{0}
April:{2}""".format(31, 28, 30))

for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(
        i, i ** 2, i**3))
print('==============================')

for i in range(1, 13):
        print("No. {0:<2} squared is {1:<3} and cubed is {2:<4}".format(
            i, i ** 2, i**3))

print('==============================')

for i in range(1, 13):
    print("No. {0:^2} squared is {1:^3} and cubed is {2:^4}".format(
        i, i ** 2, i**3))

print('==============================')

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:40}".format(
        i, i ** 2, i**3))

print("Pi is approximatey {0:12}".format(22 / 7))
print("Pi is approximatey {0:12f}".format(22 / 7))
print("Pi is approximatey {0:12.50f}".format(22 / 7))
print("Pi is approximatey {0:52.50f}".format(22 / 7))
print("Pi is approximatey {0:62.50f}".format(22 / 7))
print("Pi is approximatey {0:<72.50f}".format(22 / 7))
print("Pi is approximatey {0:<72.54f}".format(22 / 7))

print('==============================')

#  Use the built-in function round():
print(round(1.2345,2))

#  Or built-in function format():
print(format(1.2345, '.3f'))

#  Or new style string formatting:
print("{:.2f}".format(1.2345))

#  Or old style string formatting:
print("%.2f" % (1.679))


#  =========================================================
#  Getting string (array) elements (characters from the string)
#  =========================================================

a = "Hello, World!"
print(a[1])
print(a[12])

#  =========================================================
#  Getting a slice of elements (characters from the string)
#  =========================================================

b = "Hello, this is My World!"
print(b[15:17])  # returns My
print(b[-6:-1])  # returns World

#  =========================================================
#  Getting the length of a string
#  =========================================================
c = "Hello, this is My World!"
d = "Harmy"
print(len(c))  # returns 24
print(len(d))  # returns 5

#  =========================================================
#  Stripping white space from the start and end of a string
#  =========================================================
e = "              Hello, this is My World!           "
print(e.strip())  # Hello, this is My World!

#  =========================================================
#  Converting a string to upper or lower case
#  =========================================================
e = "              Hello, this is My World!           "
print(e.lower())  # hello, this is my world!
print(e.upper())  # HELLO, THIS IS MY WORLD!

#  =========================================================
#  Replacing words in a string with other words
#  =========================================================
f = "Hello, this is My World!"
print(f.replace('H', 'J'))          # Jello, this is My World!
print(f.replace('Hello', 'Jowwy'))  # Jowwy, this is My World!

#  =========================================================
#  Splitting a string up (into a list of strings)
#  =========================================================
g = "Hello, this, is, My, World!, do, one!"
print(g.split(','))        # ['Hello', ' this', ' is', ' My', ' World!', ' do', ' one!']
print(type(g.split(',')))  # <class 'list'>

#  =========================================================
#  Checking if a string is or is not within another string (true or false)
#  =========================================================
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
y = "xlain" in txt
z = "ain" not in txt
a = "xlain" not in txt
print(x)  # True
print(y)  # False
print(z)  # False
print(a)  # True

#  =========================================================
#  Concatenating multiple strings
#  =========================================================
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#  =========================================================

#  =========================================================
#  Translate characters in a string to another character
#  =========================================================
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
str = "this is string example....wow!!!"
print (str.translate(trantab))

#  =========================================================


#  =========================================================
#  Search a string for an instance of a substring (full string)
#  =========================================================
quote = 'Let it be, let it be, let it be'

result = quote.rfind('let it')
print("Substring 'let it':", result)

result = quote.rfind('small')
print("Substring 'small ':", result)

result = quote.rfind('be,')


if (result != -1):
  print("Highest index where 'be,' occurs:", result)
else:
  print("Doesn't contain substring")

#  =========================================================

#  =========================================================
#  Search a string for an instance of a substring (with start and end index)
#  =========================================================
quote = 'Do small things with great love'

# Substring is searched in 'hings with great love'
print(quote.rfind('things', 10))

# Substring is searched in ' small things with great love'
print(quote.rfind('t', 2))

# Substring is searched in 'hings with great lov'
print(quote.rfind('o small ', 10, -1))

# Substring is searched in 'll things with'
print(quote.rfind('th', 6, 20))

#  =========================================================


#  =========================================================
#  The rindex() method returns the highest index of the substring inside the string (if found). If the substring is not found, it raises an exception.
#  =========================================================
quote = 'Let it be, let it be, let it be'

result = quote.rindex('let it')
print("Substring 'let it':", result)

# result = quote.rindex('small')
# print("Substring 'small ':", result)

#  =========================================================


#  =========================================================
#  Translate a string using a translation table
#  =========================================================

firstString = "abc"
secondString = "ghi"
thirdString = "ab"

string = "abcdef"
print("Original string:", string)

translation = string.maketrans(firstString, secondString, thirdString)

# translate string
print("Translated string:", string.translate(translation))
#  =========================================================


#  =========================================================
#  Print a range in reverse using a slice
#  =========================================================
backwards = 'relliM wehttaM'
print(backwards[::-1])
#  =========================================================



word_lower = 'harmony'
word_lower_1 = '          harmony'
word_lower_2 = '  harmony'
word_higher = 'HARMONY'
decimal_number = '576'
my_string = 'abcdefghijklmnopqrstuvwyz'


print(word_lower.capitalize())     # capitalize()	Converts the first character to upper case
print(word_higher.casefold())      # casefold()	Converts string into lower case
print(word_lower.center(20))       # center()	Returns a centered string surrounded by spaces
print(word_lower.center(20, 'x'))  # center()	Returns a centered string surrounded by configured character
print(word_lower.count('a'))       # count()	Returns the number of times a specified value occurs in a string
print(word_lower.encode())         # encode()	Returns an encoded version of the string
print(word_lower.endswith('b'))    # endswith()	Returns true if the string ends with the specified value
print(rawstring.expandtabs(2))     # expandtabs()	Sets the tab size of the string
print(word_lower.find('mo'))       # find()	Searches the string for a specified value and returns the position of where it was found
print(word_lower.index('y'))       # index()	Searches the string for a specified value and returns the position of where it was found
print(word_lower.isalnum())        # isalnum()	Returns True if all characters in the string are alphanumeric
print(word_lower.isalpha())        # isalpha()	Returns True if all characters in the string are in the alphabet
print(decimal_number.isdecimal())   # isdecimal()	Returns True if all characters in the string are decimals
print(decimal_number.isdigit())     # isdigit()	Returns True if all characters in the string are digits
print(word_lower.isidentifier())    # isidentifier()	Returns True if the string is an identifier
print(word_lower.islower())         # islower()	Returns True if all characters in the string are lower case
print(word_lower.isupper())         # Returns True if all characters in the string are upper case
print(decimal_number.isnumeric())   # isnumeric()	Returns True if all characters in the string are numeric
print(word_lower.isprintable())     # Returns True if all characters in the string are printable
print(word_lower.isspace())         # isspace()	Returns True if all characters in the string are whitespaces
print(word_lower.istitle())         # istitle()	Returns True if the string follows the rules of a title
print(word_lower_1.ljust(12))       # ljust()	Returns a left justified version of the string
print(word_lower_1.lstrip())        # lstrip()	Returns a left trim version of the string
print(word_lower.partition('a'))	# Returns a tuple where the string is parted into three parts
print(word_lower.rjust(12))	        # Returns a right justified version of the string
print(quote.rpartition(','))	    # The rpartition() splits the string at the last occurrence of the argument string and returns a tuple containing the part the before separator, argument string and the part after the separator.
print(word_lower.rsplit())	        # Splits the string at the specified separator, and returns a list
print(word_lower.rstrip())	        # Returns a right trim version of the string
print(word_lower.splitlines())      # Splits the string at line breaks and returns a list
print(word_lower.startswith('h'))	    # Returns true if the string starts with the specified value
print(word_lower.swapcase())	    # Swaps cases, lower case becomes upper case and vice versa
print(word_lower.title())	        # Converts the first character of each word to upper case
print(word_lower_1.zfill(3))	        # Fills the string with a specified number of 0 values at the beginning




