
'''
Input:  an integer
Output: an integer, but the number with digits reversed from the input int

Rules
Explicit:

Implicit:

Questions

Data Structures:
    - list 
    - string
    - int
Algorithms:
    - declare an empty list "nums"
    - for the stringified version of input int "number", append each digit into "nums"
    - initialize a list "reversed_nums" and assign a reversed list of nums using reversed function
    - join "reversed_nums" into a string "reversed_num_string"
    - return a int version of that "reversed_num_string"
'''

def reverse_number(number):
    nums = []
    for digit in str(number):
        nums.append(digit) # each char (string) is appended to nums 
    reversed_nums = reversed(nums)
    reversed_num_string = "".join(reversed_nums)
    return int(reversed_num_string)

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True