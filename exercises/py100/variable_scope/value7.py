# running the program will print out 2
# we explicitly said inside the function variable a is global
# therefore, reassignment to the variable the integer value 2
# will change its value globally

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)