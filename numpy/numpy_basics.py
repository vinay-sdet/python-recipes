# NumPy vectorized operations let us perform arithmetic on every element in an array without writing loops.
# This example shows how multiplication, subtraction, addition, and division work element-wise on a NumPy array.

import numpy as np

numbers = [10, 20, 30, 40, 50]
arr = np.array(numbers)
print("Original array:", arr)
result = arr * 2
print("Result after multiplying by 2:", result)

result = arr - 5
print("Result after subtracting 5:", result)
result = arr + 5
print("Result after adding 5:", result)
result = arr / 2
print("Result after dividing by 2:", result)
