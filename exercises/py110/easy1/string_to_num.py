'''
Your function should calculate the result by using the characters in the string.
- Assume all characters are numeric.
- Do not use built-in int() function to convert

PEDAC
Input:  string
Output: integer version of input string

Rules:
Explicit:
    - Do not use built-in int() function
Implicit:

Q's

Data Structure:
-list: add each number from original string into this list 
-dictionary: match char to number (ex: '8' to 8)
-int: needed for result integer

Algorithm:
    - get the corresponding int "current_digit" from char
    - add "current_digit" to int "result" * 10

'''

def string_to_integer(string):
    DIGITS = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "0": 0,
    }

    result = 0
    for char in string:
        result = (10 * result) + DIGITS[char]
    return result

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
print(string_to_integer("692025") == 692025)    # True
print(string_to_integer("0") == 0)    # True
print(string_to_integer("10") == 10)    # True