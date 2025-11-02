


# print all odd numbers from 1 to 99, inclusive, with each number on a separate line 
# bonus: Can you solve the problem by iterating over just the odd numbers?

# PEDAC
# P: understand the Problem
# E: Examples / Test cases
# D: Data structure
# A: Algorithm
# C: Code 

# input : None
# output : prints odd numbers from 1 to 99

# Data structure: range()
# could iterate range, increment count by 1
# or increment count by 2, just to get the odd numbers
def print_odd_nums():
    for odd_num in range(1, 100, 2):
        print(odd_num)
        
if __name__ == "__main__":
    print_odd_nums()