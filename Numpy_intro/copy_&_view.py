import numpy as np

# copy is new array copy of orignal
# view is just a view of orignal array

# COPY
a = np.array([1,2,3,4])
a1 = a.copy()

a[0] = 40

print(a)

print(a1)

# VIEW
b = np.array([4,3,5,6])

b1 = b.view()

b[0] = 0


print(b)
print(b1)


arr = np.array([1,2,3,4])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)