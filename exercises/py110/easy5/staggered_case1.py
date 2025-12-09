
'''
Input:  a string
Output: A string, every other character from the input string is capitalized 

Rules
Explicit:
- Non-alphabetic characters should not be changed

Data Structures:
- Boolean : to alternate between lowercase and capitalized letters
- string: will contain case-staggered string
- 

Algorithms:
IDEA
- capitalized = True 
- new_string = ''
- for every character in string
    - if the character is alphabetic character
    - check capitalized's current value and append correct version of the char to new_string 
    - toggle capitalized's value (True > False, False > True)
- return new_string
'I lOVe Code'
'I lOvE cOdE'
Pseudocode:
- is_capitalized = True 
- new_string = ''
- for char in string:
    if char.isalpha():
        new_string += char.upper() if is_capitalized else char.lower()
        is_capitalized = not is_capitalized
    else:
        new_string += char 
- return new_string
'''

def staggered_case(string):
    is_capitalized = True 
    new_string = '' 
    for char in string:
        if char.isalpha():
            new_string += char.upper() if is_capitalized else char.lower()
        else:
            new_string += char 
        is_capitalized = not is_capitalized
    return new_string 

print("Method 1")
string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

def staggered_case2(string):
    # depends on the index's even/odd property 
    results = ''
    for idx, char in enumerate(string):
        func = char.upper if idx % 2 == 0 else char.lower
        results += func()
    return results
    
print("Method 2")
string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case2(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case2(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case2(string) == result)  # True

print(staggered_case2('') == "")          # True