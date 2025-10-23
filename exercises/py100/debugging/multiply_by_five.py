# the reason why we don't get the expected result in print is, because with input function
# default value for user input is string. Therefore, we have to type cast user input
# from string to int

def multiply_by_five(n):
    return n * 5

number = int(input("Hello! Which number would you like to multiply by 5? "))

print(f"The result is {multiply_by_five(number)}!")