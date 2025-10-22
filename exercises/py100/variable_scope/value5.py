# calling my_function will result in UnboundLocalError. local variable a cannot be accessed since it does 
# not have a value associated with it.

a = 1

def my_function():
    print(a)
    a = 2

my_function()