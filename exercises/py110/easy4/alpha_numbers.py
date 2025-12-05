'''
PEDAC

Input:  a list of integers between 0 and 19
Output: a list of those integers based on English word for each number

Rules
Explicit:
    - list will contain all numbers from 0 (inclusive) and 19 (inclusive)
    - 'a' comes before 'b', 'a' comes before 'z', etc.
Implicit:

Data Structures:
    - list: list comprehension
    - dictionary: number <> string key-value match
Algorithms: 
    - initialize a dictionary DICT and use integer value as a key, corresponding English word for value
    - using list comprehension, sort numbers based on their English word
        - sorted method, key=str(DICT[num])
'''

WORD_FOR_NUMS = ['zero', 'one', 'two', 'three', 'four', 'five',
            'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
            'twelve', 'thirteen', 'fourteen', 'fifteen',
            'sixteen', 'seventeen', 'eighteen', 'nineteen']

def word_for_number(num):
    return WORD_FOR_NUMS[num]

def alphabetic_number_sort(num_list):
    return sorted(num_list, key=word_for_number)

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True