import numpy as np 

# to access array elements 

arr = np.array([1,3,4,5])

print("first element", arr[0]) # for first element

print("third element", arr[2]) # for third element


# we can also perform addition and all...

a = np.array([1,2,3,4])

print("som of third and first element : ", a[2] + a[0]) 

# Access elements from twp 2D array

b = np.array([[1,2,3,4], [5,6,7,8]])
print("---------->>>", b.ndim)

print("this is 2nd element on 1st row : ", b[0, 1])


# Access elements from twp 3D array

c = np.array([[[1,2,3,4], [5,6,7,8]], [[9,10,11,12], [13,14,15,16]]])
print("---------->>>", c.ndim)

print("third element of second array of first array" ,c[0, 1, 2])


