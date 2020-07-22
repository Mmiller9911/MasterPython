#  In computing, the modulo operation finds the remainder after division of one number by another (called the modulus of the operation).

# for i in range(0, 100, 7):
#     if i > 0 and i % 11 == 0: (i % 11 means i divided by 11 has no remainder, so it must be divisible)
#         break print(i)

# using continue this code excludes values which when divided by 3/5 produce a whole number
for x in range(21):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)
#  ============================================================================================

# without continue
for x in range(21):
    if x % 3 != 0 and x % 5 != 0:
        print(x)

