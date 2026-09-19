# Exercise 4 — Broadcasting
# Create:
# numbers = np.array([10, 20, 30, 40])
# Then:
# numbers + 5
# Print the result.
# Then create:
# data = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])
# and try:
# data + 5
# Observe the output.

import numpy as np

data = np.array([[10, 20, 30], [40, 50, 60]])
print("Original 2D array:", data)
print("Addition by 5", data + 5)
print("Shape of the array:", data.shape)
print("Number of dimensions:", data.ndim)
print("Size of the array:", data.size)
print("Data type of the array:", data.dtype)
print("Sum of all elements:", np.sum(data))
print("Mean of all elements:", np.mean(data))
print("Standard deviation of all elements:", np.std(data))
print("Minimum value in the array:", np.min(data))
print("Maximum value in the array:", np.max(data))
print("Transpose of the array:\n", np.transpose(data))
print("Reshaped array (3x2):\n", data.reshape(3, 2))
print("Flattened array:", data.flatten())
print("Unique elements in the array:", np.unique(data))
print("Cumulative sum of elements:", np.cumsum(data))
