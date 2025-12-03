'''
PEDAC

Input: A list of positive numbers
Output: A string. Multiply all of the integers from the input list, divide the result by the number of 
        elements in the input list, and return the result as a string with the value rounded to three
        decimal places.

Rules
Explicit:

Implicit: 

Questions: 
    - Can the input list be empty? 
        - Can't tell from examples, but will assume they will contain at least 1 number

Data Structures:
    - int : multiplying numbers 
    - float : when dividing the number
    - list : list iteration of the original input list 
    - string: formatted string to format output

Algorithms:
    - Initialize variable "multiple" as 1
    - Iterate through input list "nums", multiply each number to multiple
    - Divide "multiple" by the number of elements in the input list "nums". Store this result as "result" 
        variable
    - Format "result" variable using f-string f"{result:.3f}"
'''

def multiplicative_average(nums):
    multiple = 1

    for num in nums: 
        multiple *= num 

    result = multiple / len(nums)
      
    return f"{result:.3f}"

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")