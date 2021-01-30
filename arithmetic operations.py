
a = 12
b = 22.7


print(a * b)    # Mu ltiply
print(b/a)      # divid
print(b//a)     # divids but rounds and returns integer
print(a+b)      # addition
print(a-b)      #sunstract
print( a ** a)  # power.
print (b%a)     # Modulus, returns the reminder of the division

a += 2      # short form of  a = a + 2
print(a)
a -= 3      # short form of  a = a - 3
print(a)
a = 12
a *= 3      # short form of a = a * 3
print(a)

a = 12
a /= 3      # short form of a = a / 3
print(a)

# Order of operation is same as in general maths.
print(12 + 2 * 2)      # answer is 16 NOT 28
print( (1+3) - 10 + 22 - 6 * 4 / 2 ** 3) # first () then power (**) then / then * then - then +

#Math functions.

print(round(b))     #rounds from floating to integer
print(abs(-33.2))   # absolute (abs()) returns +ve value

import math

print(math.ceil(2.9))
print(math.floor(2.9))

