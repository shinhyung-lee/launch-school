'''
Input:  A list of strings
Output: A list of strings from the input, but with all vowels (a, e, i, o, u)
        removed

Rules
Explicit
    -
Implicit
    -
    
Data Structures:
    - list:
    - string: 
    
Algorithms: 
    IDEA
    - results = []
    - For each string in the strings list, remove vowels and add the string to result
    - Return results
    
    Pseudocode:
    - RESULTS = []
    - VOWELS = [ 'a', 'i', 'o', 'u', 'e' ]
    - for WORD in WORD:
        - CURRENT_WORD = ''
        - for CHAR in WORD:
            - if CHAR not in VOWELS:
                CURRENT_WORD += CHAR 
        - RESULTS += CURRENT_WORD  
    
    Return Value
    - return RESULTS
'''
def remove_vowels(words):
    VOWELS = [ 'a', 'i', 'o', 'u', 'e' ]
    results = []
    for word in words:
        current_word = ''
        for char in word:
            if char.casefold() not in VOWELS:
                current_word += char 
        results.append(current_word)
    return results 
        
# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True