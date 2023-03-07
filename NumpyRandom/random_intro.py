import numpy

from numpy import random

# NumPy offers the random module to work with random numbers.


# Generate a random integer from 0 to 100:
x = random.randint(10)
print("---->>>",x)

# rand() method returns a random float between 0 and 1.

x1 = random.rand()
print("---->>>", x1)

# Random Array

a = random.randint(100, size=4)

print("---->>>", a )

b = random.rand(5)
c = random.rand(3, 5)

print("---->>>", b)
print("---->>>", c)


# Generate Random Number From Array

# The choice() method takes an array as a parameter
# and randomly returns one of the values.

ab = random.choice([4,5,6,7,8,10])
print("------->>>>>",ab)

abc = random.choice([4,5,6,7,8,10], size=(3, 5))
print("----->>>", abc)


