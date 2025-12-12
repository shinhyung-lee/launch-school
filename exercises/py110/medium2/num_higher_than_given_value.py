'''
Input:  An integer
Output: A featured integer that's greater than the input

Rules
Explicit:
- Largest featured num: 9876543201
- Featured Number:
    - odd number
    - multiple of 7
    - all of its digits occurring exactly once each
    
Data Structures:
- range : numbers from input to 9876543201 (+1 for range)
- str : convert int to string to count occurrence of each character
- dict : to count frequency of each character in a stringified
    version of int 
- 

Algorithms:
IDEA
- from current(input) to limit number,
    - find a featured number and return it 

Pseudocode:
- helper functions
- is_odd, multiple_of_7, unique_digits

unique_digits (helper function)
Input:  dict
Output: Boolean value to tell if all digits are unique (for all 
values, value < 2)

DS: dict, string
Algorithm:
- for num in range(input, limit_num + 1):
    - string_num = str(num)
    - frequency = {}
    - for each digit in string_num:
        - use digit as a key, value as how many times digit appeared
        in string_num 
    if is_odd(num) and multiple_of_7 and unique_digits(num):
        - supply frequency dict as an argument to unique_digits
        return the number 
- return error msg 
    
'''
def is_odd(num):
    return num % 2 != 0

def multiple_of_7(num):
    return num % 7 == 0

def unique_digits(freq_dict):
    frequencies = freq_dict.values()
    # print(frequencies)
    return all([value < 2 for value in frequencies])

def next_featured(num):
    LAST_FEATURED_NUM = 9876543201
    for current in range(num + 1, LAST_FEATURED_NUM + 1):
        # print(f'current: {current}')
        str_num = str(current)
        freq = {}
        for digit in str_num: 
            freq.setdefault(digit, 0)
            freq[digit] += 1 
        # print(freq)
        if is_odd(current) and multiple_of_7(current) and unique_digits(freq):
            return current 
    return ('There is no possible number that ' 
            'fulfills those requirements.')

# print("\nMethod 1")
# print(next_featured(12) == 21)                  # True
# print(next_featured(20) == 21)                  # True
# print(next_featured(21) == 35)                  # True
# print(next_featured(997) == 1029)               # True
# print(next_featured(1029) == 1043)              # True
# print(next_featured(999999) == 1023547)         # True
# print(next_featured(999999987) == 1023456987)   # True
# print(next_featured(9876543186) == 9876543201)  # True
# print(next_featured(9876543200) == 9876543201)  # True

# error = ("There is no possible number that "
#          "fulfills those requirements.")
# print(next_featured(9876543201) == error)       # True

# odd, multiple of 7, unique letters

def find_next_odd_multiple_of_7(num):
    num += 1
    while (num % 2 == 0) or (num % 7 != 0):
        num += 1 
    return num 

def unique_digits(num):
    digits = list(str(num))
    return len(digits) == len(set(digits))

def next_featured2(num):
    featured_num = find_next_odd_multiple_of_7(num)

    while featured_num <= 9876543201:
        if unique_digits(featured_num):
            return featured_num
        featured_num += 14 
    return ('There is no possible number that ' 
            'fulfills those requirements.')
        
print("\nMethod 2")
print(next_featured2(12) == 21)                  # True
print(next_featured2(20) == 21)                  # True
print(next_featured2(21) == 35)                  # True
print(next_featured2(997) == 1029)               # True
print(next_featured2(1029) == 1043)              # True
print(next_featured2(999999) == 1023547)         # True
print(next_featured2(999999987) == 1023456987)   # True
print(next_featured2(9876543186) == 9876543201)  # True
print(next_featured2(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured2(9876543201) == error)       # True