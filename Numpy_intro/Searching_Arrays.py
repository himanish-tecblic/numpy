import numpy as np 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
  
x = np.where(arr == 4)

y = np.where(arr%2 == 1)

print(x)
print()
print(y)

a = np.array([7, 8, 9, 10])

x = np.searchsorted(a, 7)
x1 = np.searchsorted(a, 7, side='right')
print()
print(x)
print()
print(x1)
