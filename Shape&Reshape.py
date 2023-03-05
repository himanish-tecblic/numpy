# Array Shape

import numpy as np

# print the shape of 2-D array
arr = np.array([[1,2,3,4], [5,6,7,8]])

print(arr.shape)

# The example above returns (2, 4), 
# which means that the array has 2 dimensions, 
# where the first dimension has 2 elements and the second has 4.



a = np.array([1,2,3,4], ndmin=5)

print(a)
print("shape of array : ", a.shape)


# Reshaping arrays

# Reshape From 1-D to 2-D
# dimension will have 4 arrays, each with 3 elements:

b = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(b)
c = b.reshape(4, 3)
print(c)

# 1-D to 3-D
# dimension will have 2 arrays that contains 3 arrays, each with 2 elements:

d = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(d)
e = d.reshape(2, 3, 2)
print(e)



# Unknown Dimension
# Pass -1 as the value, and NumPy will calculate this number for you.

arr1 = np.array([1,2,3,4,5,6,7,8])

newarr = arr1.reshape(2,2,-1)
print(newarr)


# Flatteing the arrays whit the method reshape(-1)

p = np.array([[1,2,3], [4,5,6]])
print(p.ndim)

q = p.reshape(-1)
print(q)
print(q.ndim)
