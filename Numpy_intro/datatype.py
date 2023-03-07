# datatype in numpy

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )


import numpy as np

a = np.array([1,2,3,4])
b = np.array(['banana', 'apple'])

print(a.dtype)
print(b.dtype)


# Create an array with data type string:
c = np.array([1,2,3,4], dtype='S')
print(c.dtype)


# Create an array with data type 4 bytes integer:4

d = np.array([1,2,3,4], dtype='i4')

print(d)
print(d.dtype)

# Converting Data Type on Existing Arrays

# The best way to change the data type of an existing array,
# is to make a copy of the array with the astype() method.


# Change data type from float to integer by using 'i' as parameter value:

e = np.array([1.1,2.1,3.5,4.6])
print(e)
print(e.dtype)

newe = e.astype('i')

print(newe)
print(newe.dtype)