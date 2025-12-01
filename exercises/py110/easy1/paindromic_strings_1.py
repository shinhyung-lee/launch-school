'''
PEDAC
returns True if the string passed as an argument is a palindrome, False otherwise.
reads the same forwards and backdwards. case matters and all characters matter

Input    : string
Output   : Boolean value expressing if the string is a palindrome

Rules
Explicit : 
    - case sensitive
    - all characters matter, including spaces and other characters
Implicit :

Questions
    -What if the string is empty? Yes 

Guard Clauses
    -If the length of the string is 0 (empty string), return True

Data Structure: 
    - list: 
    - tuple:
    - set, frozen set:
    - dictionary:
    - range:
    - string: string slicing (reverse them and compare)

Algorithm:
    - compare the original string with the reversed version of it.
    - if the above two are equal, return True. Otherwise, return False
'''

def is_palindrome(sentence):
    reversed = sentence[::-1]
    return sentence == reversed

# All of these examples should print True
print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)