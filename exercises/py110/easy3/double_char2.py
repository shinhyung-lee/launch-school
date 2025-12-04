''' 
PEDAC

Input:
Output: 

Rules
Explicit:
Implicit:

Questions

Data Structures

Algorithms: 
'''
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
def double_consonants(string):
    doubled_chars = []
    for char in string:
        doubled_chars.append(char * 2 if char.casefold() in CONSONANTS else char)
    return "".join(doubled_chars)

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")