# Create a generator function that yields user input strings until the word "stop" is entered.

def user_input_generator():    
    while True:
        user_input = input('Enter value: ')
        if user_input == 'stop':
            break 
        yield user_input 

user_input = user_input_generator()
for val in user_input:
    print(val)