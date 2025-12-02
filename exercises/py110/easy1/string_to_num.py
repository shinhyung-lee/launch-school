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
- initialize a dictionary "char_to_num_dict" with string version of number as the key, int version of number as the value
- initialize a int "result_int" and assign it 0
- initialize a int "digit_identifier" and assign it 1
- in the original string, iterate from the last digit to the first digit
    - find int for each digit "number" using "char_to_num_dict"
    - add the "number" multiplied by "digit identifier" to "result_int"
    - multiply "digit_identifier" by 10
-return "result int"

'''
char_to_num_dict = {
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

def string_to_integer(string):
    result_int = 0
    digit_identifier = 1
    for idx in range(len(string)):
        char =  string[-(idx + 1)] # iterating from end to beginning
        number = char_to_num_dict[char] 
        result_int += (number * digit_identifier)
        digit_identifier *= 10
    
    return result_int


print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
print(string_to_integer("692025") == 692025)    # True
print(string_to_integer("0") == 0)    # True
print(string_to_integer("10") == 10)    # True