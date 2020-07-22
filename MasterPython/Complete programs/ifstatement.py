# print('Please enter a number between 1 and 30')
# guess = int(input())  #guess number one is captured
#
# if guess != 5:   #it cant be equal to 5 or would go down the else strand
#     if guess < 5:
#         print('guess a higher number')
#     else:
#         print('guess a lower number')
#
#     guess = int(input()) #guess number two is captured
#
#     if guess == 5:
#         print('bingo! it is five!')
#     else:
#         print('wrong, sorry you only get 2 guesses')
# else:
#     print('you guessed correctly on the first guess!')
# name = input('Please enter your name: ')
# age = int(input('Hi {0} how old are you?'.format(name)))
# print(age)
#
# if age >= 18:
#     print('you are old enough to vote')
#     print('duhh')
# else:
#     print('please come back in {0} years'.format(18 - age))
# age = int(input('How old are you?'))
#
# #if (age >=16) and (age <=65):  #brackets for clarity only
# #if 16<= age <=65:
# #if 15 < age < 66:
#
#
# name = input('please enter your name ')
# age = int(input('hi {0} please enter your age '.format(name)))
# if 18 <= age <31:
# #if age > 17 and age < 31:
#     print ("Welcome to club 18-30!")
# else:
#     if age <=17:
#         print ("Always next time!!!")
#     elif age >= 31:
#         print ("Sorry too old!")




print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")

if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")

