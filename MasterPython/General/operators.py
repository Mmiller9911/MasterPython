a = 12
b = 3

print(a + b) #15
print(a - b ) #9
print(a * b) #36
print(a / b ) #4.0
print(a//b) #4
print(a%b) #0

print()
for i in range (1,4):
     print(i)


bun_price = 2.40
money = 15
print(money // bun_price) #this returns 6.0 instead of 6.25 so we will only sell full buns


# Operator precedence
# Refers to the order in which operators are evaluated eg.
#
# print (a + b / 3 - 4 * 12) = -35 NOT 12 which would need -  print ((((a + b) / 3) - 4) * 12)
# print (a + (b / 3) - (4 * 12))
# if operators have the same precendence then they are evaluated from left to right
#
# BODMAS - Brackets, Order, Division, Multiplication, Addition, Subtraction BODMAS - Brackets, Order, (Division, Multiplication), (Addition, Subtraction)

a = 12
b = 3
print(a / (b * a) / b)
# 12 / (36) / 3 (0.3333 / 3 = 0.1111)