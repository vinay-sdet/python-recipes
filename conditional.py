print('Enter your text from below or your own')
print('Hello')
print('How are you?')
print('Bye')
print('-------------------')
user_input:str = input('Enter your choice: ')

if user_input == 'Hello':
    print('Bot: Hello!')
elif user_input == 'How are you?':
    print('Bot: I am fine, thank you!') 
elif user_input == 'Bye':
    print('Bot: Goodbye!')
else:
    print('Bot: I am sorry, I did not understand your request.')        

