

#  ============================================================================================
# +=
number = "767, 754, 234, 755, 933, 123"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]

newNumber = int(cleanedNumber)
print('the number is {0} '.format(newNumber))


greeting = 'good '
greeting += 'morning '
print(greeting)


number = 5
multiplier = 8
answer = 0
for i in range(0, multiplier):
    answer += number

print(answer)
#  ============================================================================================
#  -=
x = 24
x -= 4
print(x)
#  ============================================================================================


#  ============================================================================================
#  *=
x *= 4
print(x)

greeting *= 7
print(greeting)
#  ============================================================================================


#  ============================================================================================
#  /=
x /= 7
print(x)
#  ============================================================================================


#  ============================================================================================
#  **=
x **=5
print(x)
#  ============================================================================================


#  ============================================================================================
#  %=
x %= 60
print(x)
#  ============================================================================================








