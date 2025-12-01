'''
PEDAC

Input: a string
Output: Boolean value to tell if the string is a palindrome or not

Rules:
Implicit:
- 

Explicit:
    - case-insensitive comparison
    - ignore all non-alphanumeric characters

Comment:
    - can use palindrome function from the previous problem

Questions:
    - empty string will return True (is a palindrome)

Data Structure:
    - string
    - list 
    - range 
    - dictionary (x)
    - tuple 
    - set, frozenset

Algorithm:
    - Create a variable cleaned_string
    - Iterate the original string. If the character is alphanumeric, add the character to cleaned_string
    - Compare if cleaned_string is equal to its reversed version. 
            -If yes, return True. Otherwise, return False
'''

def is_real_palindrome(sentence):
    cleaned_string = ''
    
    for char in sentence:
        if char.isalnum():
            cleaned_string += char.lower()

    return cleaned_string == cleaned_string[::-1]

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True