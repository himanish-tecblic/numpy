import numpy as np


arr = np.array([3, 4, 6, 0, 1])

print("--------->", np.sort(arr))


a = np.array(['banana', 'cherry', 'apple'])

print("--------->", np.sort(a))


b = np.array([[6, 3, 7], [0, 4, 1]])

print("---------->", np.sort(b))




# Filtering Arrays

# ----   Getting some elements
# ---- out of an existing array and creating a new array out of them is called filtering.

x = np.array([41, 40, 46, 1])

y = [True, True, True, False]

x1 = x[y]

print("---------->", x1)
