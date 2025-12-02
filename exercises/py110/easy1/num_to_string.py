'''
converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) 
to the string representation of that integer

PEDAC
Input: non-negative integer
Output: string representation of the input integer

Rules
Explicit:
-May not use built-in functions such as str

Implicit:

Questions

Data Structures:
    - dictionary 
    - string (string concatenation)
    - list (gather digits first then join)

Algorithm:
    - initialize stringified_num to empty string "" 
    - divide each digit by 10 until modulo == 0 and division is 0. 
    - collect modulo into "digits_lst"
    - join digits_lst and reverse. Name this string "stringified_num"
    - return "stringified_num"
'''

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def integer_to_string(integer):
    stringified_num = ""

    while integer > 0:
        integer, remainder = divmod(integer, 10)
        stringified_num = DIGITS[remainder] + stringified_num
    
    return stringified_num or "0"

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True