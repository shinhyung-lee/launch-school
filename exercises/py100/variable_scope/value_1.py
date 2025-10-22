
# from the global scope, the program cannot see my_value variable
# my_value variable is inside the if statement scope.
# When the program is run, it will print out None

if True:
    my_value = 20

print(my_value)