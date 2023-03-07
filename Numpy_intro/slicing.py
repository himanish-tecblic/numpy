# slice the array with index number

import numpy as np

a = np.array([1,2,3,4,5,6])

print("befor slice ", a)
print("after slice", a[1:5])
# this will slice array form index 1 to 5 

print("from start to index 4", a[:4])

print(a[1:5:2])
print(a[::2])


# slicing 2-D arrays

b = np.array([[1,2,3,4], [5,6,7,8]])

print("second array 2nd element to 4th index", b[1, 1:4])

print("print 2nd index ele. from both", b[:2, 2])

print(b[0:2, 1:4])