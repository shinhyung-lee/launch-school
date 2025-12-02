'''
PEDAC

Prompt:

Input:
Output:

Rules:
Explicit
    -Number string can start with + (positive), - (negative) signs. Or no sign (positive). 
Implicit

Questions

Data Structure

Algorithm

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

def string_to_signed_integer(string):
    match string[0]:
        case "+":
            return string_to_integer(string[1:])
        case "-":
            return -string_to_integer(string[1:])
        case _:
            return string_to_integer(string)

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True