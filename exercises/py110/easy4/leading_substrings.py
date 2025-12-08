'''
Input: a string
Output: A list of strings that are substrings of the input string
    
Rules
Explicit:
    - each substring begin with the first letter of the word 
    - list should be ordered from shortest to longest
Implicit:

Questions:
    - can the input string be an empty string?
    
Data Structures:
    - list
    - string 
Algorithms:
    - if the length of input string is 0, return an empty list
    - initialize an empty list "substrings"
    - initialize an empty string "current_substring"
    - initialize "index" variable to 0
    - while "index" is less than the length of the original input string,
        - concatenate character at current index to "current_substring"
        - append "current_substring" to "substrings"
    - return "substrings"
'''
def leading_substrings(string):
    if len(string) == 0:
        return []
    substrings = [] 
    current_substring = ''
    idx = 0 
    while idx < len(string):
        current_substring += string[idx]
        substrings.append(current_substring)
        idx += 1
    return substrings

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])