numbers = [10, 5, 25, 8, 15]

largest = numbers[0]
for number in numbers:
    print(f"Current number: {number}, Largest so far: {largest}")
    if number > largest:
        largest = number
print(f"Largest number is: {largest}")
