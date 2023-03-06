import numpy as np

# Iterating means going through elements one by one.
# As we deal with multi-dimensional arrays in numpy,
# we can do this using basic for loop of python.



# iterate on a 1-D array
a = np.array([1,2,3])

for x in a :
    print(x)

# iterate on a 2-D array

b = np.array([[1,2,3], [4,5,6]])

for y in b:
    print(y)

for x in b:
    for y in x:
        print(y)

# iterate on a 3-D array

c = np.array([[[1,2,3,4], [5,6,7,8], [9,10,11,12]]])

for x in c:
    print(x)

for x in c:
    for y in x:
        for z in y:
            pass
            # print(z)


# Iterating Arrays Using nditer()


arr = np.array([[[1,2], [3,4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    pass
    # print(x)



arr1 = np.array([[1,2,3,4], [5,6,7,8]])

for x in np.nditer(arr1[:, ::2]):
    print(x)