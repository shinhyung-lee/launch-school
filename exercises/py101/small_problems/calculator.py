

def prompt(message):
    print(f"==> {message}")
    
# Ask the user for the second number 
# Ask the user for an operator to perform
# Perform the operation on the two numbers
# Print the result to the terminal

prompt('Welcome to Calculator!')

# Ask the user for the first number.

prompt("What's the first number? ")
number1 = int(input())

prompt("What's the second number? ")
number2 = int(input())

operation = input('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide: ')

match operation:
    case '1':
        output = number1 + number2 
    case '2':
        output = number1 - number2 
    case '3':
        output = number1 * number2 
    case '4':
        output = number1 / number2 
        
    
print(f"The result is: {output}")







