'''
Input:  a string
Output: a list of all palindromes from substrings of the input string

Rules
Explicit:
- palindrome is case-sensitive ('Abcba' is not a palindrome)
- single characters are not palindromes 
- duplicate substrings should be included multiple times 
Implicit:

Questions

Data Structures:

Algorithms:

'''

def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

def substrings(string):
    results = []
    for index in range(len(string)):
        string_at_index = string[index:]
        for substring in leading_substrings(string_at_index):
            results.append(substring)
    return results

def is_palindrome(string):
    if len(string) <= 1:
        return False 
    first, last = 0, len(string) - 1
    while first < last: 
        if string[first] != string[last]:
            return False 
        first += 1
        last -= 1 
    return True 

def palindromes(string):
    return [substr for substr in substrings(string) if is_palindrome(substr)]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True