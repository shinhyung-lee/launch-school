'''
PEDAC

Input:  A list of integers
Output: Average of all the integers in the list, rounded down to the integer component of the average

Rules
Explicit:
    - The list will never be empty
    - Numbers will always be positive integers
Implicit:

Questions

Data Structures:

Algorithms:
    - sum all numbers from the list and store in a variable "sum_numbers"
    - divide the sum by the length of numbers in the list and store in a variable "average"
    - return the integer version of "average"

'''

def average(numbers):
    total = sum(numbers)
    return total // len(numbers)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True