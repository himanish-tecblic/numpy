# if wnats to see only one result comment out other 
# some of values have same variable name 



import numpy as np 


# this will tall us the version of numpy
# print(np.__version__)


#this will create array 
# The array object in NumPy is called ndarray.
# We can create a NumPy ndarray object by using the array() function.

# arr = np.array([1,2,3])
# print(">>>>>>>>", arr)

# print(type(arr))



# Dimensions in Arrays


# (1) 0-D Arrays

# a = np.array(42)
# print("........zero D : ", a)

# # (2) 1-D arrays

# b = np.array([1,2,3,4,5])
# print("........one D : ", b)

# (3) 2-D arrays

# c = np.array([[1,2,3],[4,5,6]])
# print("........two D :",c)

# (4) 3-D arrays

# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print("........three d :",d)


#to chack the dimensions the arrays we have "ndim"

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# create an array with 5 dimensions 


# a = np.array([1,2,3], ndmin=5)

# print(a)
# print('number of dimensions : ', a.ndim)