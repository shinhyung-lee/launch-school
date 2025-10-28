

# Ask the user for the second number 
# Ask the user for an operator to perform
# Perform the operation on the two numbers
# Print the result to the terminal

print('Welcome to Calculator!')

# Ask the user for the first number.

number1 = int(input("What's the first number? "))

number2 = int(input("What's the second number? "))

print(f'{number1} {number2}')

operation = input('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide ')

if operation == '1':
    output = number1 + number2 
elif operation == '2':
    output = number1 - number2 
elif operation == '3':
    output = number1 * number2 
elif operation == '4':
    output = number1 / number2 
    
print(f"The result is: {output}")







