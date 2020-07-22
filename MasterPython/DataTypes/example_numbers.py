
#  ============================================================================================================================================
#  Int
#  Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
#  ============================================================================================================================================

x = 1
y = 35656222554887711
z = -3255522

print(str(x) + ' is of type: {}'.format(type(x)))
print(str(y) + ' is of type: {}'.format(type(y)))
print(str(z) + ' is of type: {}'.format(type(z)))

#  ____________________________________________________________________________________________________________________________________________


#  ============================================================================================================================================
#  Float
#  Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
#  ============================================================================================================================================

x = 1.10
y = 1.0
z = -35.59

print(str(x) + ' is of type: {}'.format(type(x)))
print(str(y) + ' is of type: {}'.format(type(y)))
print(str(z) + ' is of type: {}'.format(type(z)))

#  Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100

print(str(x) + ' is of type: {}'.format(type(x)))
print(str(y) + ' is of type: {}'.format(type(y)))
print(str(z) + ' is of type: {}'.format(type(z)))

#  ____________________________________________________________________________________________________________________________________________

#  ============================================================================================================================================
#  Complex
#  Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
y = 5j
z = -5j

print(str(x) + ' is of type: {}'.format(type(x)))
print(str(y) + ' is of type: {}'.format(type(y)))
print(str(z) + ' is of type: {}'.format(type(z)))

#  ============================================================================================================================================

#  ============================================================================================================================================
#  Type Conversion
#  You can convert from one type to another with the int(), float(), and complex() methods:
#  ============================================================================================================================================

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#  convert from int to float:
a = float(x)

#  convert from float to int:
b = int(y)

#  convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(str(a) + ' is of type: {}'.format(type(a)))
print(str(b) + ' is of type: {}'.format(type(b)))
print(str(c) + ' is of type: {}'.format(type(c)))

#  ____________________________________________________________________________________________________________________________________________


#  ============================================================================================================================================
#  Generate a random number
#  ============================================================================================================================================
import random

print(random.randrange(1, 10))


#  ____________________________________________________________________________________________________________________________________________

