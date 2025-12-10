'''
Input:  Positive integer
Output: Boolean value indicating whether the input integer is a prime or not 

Rules:
Explicit
    - Cannot use any of Python's add-on packages to solve the problem.
Implicit:
    - All positive integers can be divided by 1. 
    
Data Structures:
    - int     : integer division and modulus being 0 
    - range   : range(2, num)
    - Boolean : return value 
Algorithms: 
IDEA:
    - see if the input int can be divided by any of the numbers between 2 and number itself. If yes, return False. Otherwise, return True
Pseudocode:
    - for divisor in range(2, num):
        - if num gets divided by divisor, return False
        - otherwise, return True 
'''


def is_prime(num):
    if num == 1: # guard clause 
        return False 
    
    for divisor in range(2, num):
        if num % divisor == 0:
            return False
    return True    

print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True