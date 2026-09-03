#This code will raise a TypeError because you cannot add an integer and a string together.
# a=10, b='asdf'
# print(a + b)  

a, b = 10, 'asdf'
try:
 print(a + b)
except Exception as e:
    print(f'Error: {e}')

print('I am continuing my code execution after handling the exception')       