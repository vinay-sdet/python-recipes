names: list[str] = ['Vinay','Vijay','Vivek','Varun']

for name in names:
    print (f'Hello {name}! ')

print('-------------------')

index:int = 0
while index < len(names):
    name = names[index]
    print (f'Hello {name}! ')
    index += 1  