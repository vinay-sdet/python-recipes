# Exercise 1 — Create an array
# Create a NumPy array containing:
# 10, 20, 30, 40, 50
# Print:
# the array
# its type
# its shape

import numpy as np

data = np.array([10, 20, 30, 40, 50])
print(data)
print(type(data))
print(data.dtype)
print(data.shape)

# Exercise 2 — Vectorized operations
# Using the same array, calculate:
# each number × 2
# each number + 10
# each number − 5

print(data * 2)
print(data + 10)
print(data - 5)
