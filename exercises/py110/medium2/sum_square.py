'''
Input:  A positive integer
Output: A number. difference between the square of the sum of the 
first count positive integers and the sum of the squares of the 
first count positive integers

Rules
Explicit

Implicit

Data Structures
- range 
Algorithms:
IDEA:
- Get the sum of individual numbers from 1 to input, square them
- Get the sum of square numbers from 1 to input
- Subtract second sum from the first sum and return 

Pseudocode:
- Two helper functions
- sum_square(num)
    - Add all numbers from 1 to input 
    - square the number and return
- square_sum(num)
    - total = 0 
    - for every number from 1 to input
    - square number and add to total
- return sum_square(num) - square_sum(num)
'''

def sum_square(num):
    total = sum(range(1, num + 1))
    return total**2

def square_sum(num):
    total = 0
    for current_num in range(1, num + 1):
        total += (current_num**2)
    return total

def sum_square_difference(num):
    return sum_square(num) - square_sum(num)

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True