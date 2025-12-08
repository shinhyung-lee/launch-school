
'''
Input:  a string
Output: a list of strings that are substrings of the input string

Rules:
Explicit:
Implicit:

Questions:

Data Structures:
    - list 
Algorithms:
    - from index 0 to last index, len(string) - 1, get all substrings 
    using leading_substrings function which we already have.
        - use string slice to feed argument into leading_substrings 
        function while index < len(string)
    - 
'''
def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

# def substrings(string):
#     index = 0
#     substrings = []
#     while index < len(string):
#         substrings_at_index = leading_substrings(string[index:])
#         substrings.extend(substrings_at_index)
#         index += 1
#     return substrings 

def substrings(string):
    results = []
    for index in range(len(string)):
        string_at_index = string[index:]
        for substring in leading_substrings(string_at_index):
            results.append(substring)
    return results
    

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True