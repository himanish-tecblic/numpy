import numpy as np

# We pass a sequence of arrays that we want to join to
# the concatenate() function, along with the axis.


a = np.array([1,2,3])
print(a)
print()
b = np.array([4,5,6])
print(b)

arr = np.concatenate((a, b))

print("--------->",arr)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

c = np.concatenate((arr1, arr2), axis=1)

print("--------->",c)



# sdfsdfdsfsdf
# sdfsfsdff