
'''
Does the solution meet the problem requirements?
Is the code readable and easy to understand?
Do variable and function names adhere to Python naming conventions?
Are the variable and function names meaningful and precise?
Is the code formatted correctly and free of syntax errors?
Is the solution repetitive or overly complex?
Would it make more sense to use different looping or conditional structures?
Would the solution benefit from helper functions?
Consider running the code through PyLint and discussing any issues raised.
'''
# Hi, Ursula. Your solution meets the problem's requirement of printing odd numbers from 1 to 99 (inclusive)
# Good job on that. 
# Instead of using vague number like i, try to use a more descriptive variable name. In this case, you can use
# number, for example. 
# Using a while loop for this problem is a good approach, but we could write a cleaner and concise version using 
# for loop and range(1, 100). That way, you don't have to update i (index or number) in your while loop
# for num in range(1, 100). Otherwise, good job. 
i = 1
while i < 99:
    if i % 2 == 1:
        print(i)

    i = i + 1