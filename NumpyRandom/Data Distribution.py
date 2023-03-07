# Random Distribution

# A random distribution is a set of random numbers that follow a certain probability density function.
import numpy as np
from numpy import random

x = random.choice([3, 5, 7, 9], p = [0.1, 0.3, 0.6, 0], size = (4))


# Random Permutations

# Shuffling Arrays

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print("------------->>>",arr)

# Permutation of Arrays
a = [1, 2, 3, 4, 5]
print("--------------->>>", random.permutation(a))