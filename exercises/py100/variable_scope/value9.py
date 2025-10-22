

# program will print out 7. 
# b inside of my function is using assignment. Python regards this as new local variable inside of the function
# Therefore, b += 10 will not add 10 to the current value of 7

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)