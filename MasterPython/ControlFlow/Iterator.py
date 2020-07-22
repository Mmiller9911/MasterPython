#  An iterator is used to iterate over a collection of items:

string = '0123456789'

# for i in char:
#     print(i)

for char in iter(string): #python adds the iter itself behind the scenes
     print(char)

#the code below does exactly what the for loop does implicitly

my_iterator = iter(string)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator)) #error - Traceback (most recent call last):

items = [1, 5, 9, 7, 4]
my_iterator = iter(items)
for i in iter(items):
    print(next(my_iterator))


# number = len(items)
# for number in items:
#     print(next(items))
