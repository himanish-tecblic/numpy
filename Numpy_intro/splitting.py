# We use array_split() for splitting arrays,
# we pass it the array we want to split and the number of splits.
import numpy as np

arr = np.array([1,2,3,4,5,6])

newarr = np.array_split(arr, 3)

print(newarr)
print()
a = np.array_split(arr, 4)

print(a)
print()

b = np.array_split(arr, 3)

print(b[0])
print(b[1])
print(b[2])
print()



# Splitting 2-D Arrays

A = np.array([[1,2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 10]])

A1 = np.array_split(A, 3)
B = np.hsplit(A, 3)

print(B)
print(A1)