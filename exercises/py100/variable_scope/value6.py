# the program will print 1. reassignment in the function scope does not change the value of the variable
# in the global scope.

a = 1

def my_function():
    a = 2

my_function()
print(a)