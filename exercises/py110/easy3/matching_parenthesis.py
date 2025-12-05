'''
PEDAC

Input:  a string 
Output: boolean value indicating if the input string's parentheses are properly balanced 

Rules
Explicit:
    -To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

Implicit:
    - only remove '(' (opening parentheses) if we see ')' (closing parentheses) 
    - ignore all other characters other than '()'
Data Structures:
    - list: order needs to be preserved

Algorithms:
    - initialize an empty list "parentheses"
    - Iterate through string and look for '(' and ')'.
        - '(': append to "parenthese" list
        - ')': if the rightmost element in "parentheses" is '(', remove that element 
            - use pop method
            - removes and returns the object at a specified index position
            - if no index is specified, removes and returns the last item in the index. 
    - if parentheses list is empty, return True. Else return False
'''


def is_balanced(string):
    parentheses = []
    length = len(parentheses)
    for char in string: 
        if char == '(':
            parentheses.append(char)
        elif char == ')':
            if parentheses != [] and parentheses[length - 1] == '(':
                parentheses.pop() 
            else:
                parentheses.append(char)
    return parentheses == []

print("Method 1: ")
print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True

def is_balanced2(string):
    parens = 0 
    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1
        if parens < 0: 
            return False 
    return parens == 0
        

print("\nMethod 2: ")
print(is_balanced2("What (is) this?") == True)        # True
print(is_balanced2("What is) this?") == False)        # True
print(is_balanced2("What (is this?") == False)        # True
print(is_balanced2("((What) (is this))?") == True)    # True
print(is_balanced2("((What)) (is this))?") == False)  # True
print(is_balanced2("Hey!") == True)                   # True
print(is_balanced2(")Hey!(") == False)                # True
print(is_balanced2("What ((is))) up(") == False)      # True