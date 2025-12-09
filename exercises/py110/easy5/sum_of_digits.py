'''
Input:  A positive integer
Output: The sum of digits from the input int

Rules
Explicit:
    - Function takes only one argument (positive int)
Implicit:

Data Structures:
    - int : original int, str to int, total sum
    - string : first convert int to str 

Algorithm:
IDEA
    - convert int to str (stringified_int)
    - total = 0 
    - for each digit in the stringified_int, add int(digit) to total
    - return total
Pseudocode:
    - digits = str(num)
    - total = 0 
    - for digit in digits: # digit : str
    - total += int(digit)
    - return total
'''

def sum_digits(num):
    total = 0 
    digits = str(num)
    for digit in digits: # digit : type 'str'
        total += int(digit)
        
    return total

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True