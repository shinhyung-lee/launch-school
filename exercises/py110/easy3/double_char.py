'''
PEDAC

Input:  a string
Output: a string where every character in input string was doubled. 

Rules
Explicit:
    - If the input string is empty, return empty string
Implicit:

Data Structures:
    - string : 
    - 
Algorithms: 
    - use list comprehension
    - double every character in the string and append to a list "doubled_chars"
    - join all the elements in the above list into a string "doubled_string"
    - return "doubled_string"
'''
def repeater(string):
    doubled_chars = [char * 2 for char in string]
    doubled_string = "".join(doubled_chars)
    return doubled_string

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True