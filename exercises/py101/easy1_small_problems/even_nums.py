# print all even numbers from 1 to 99, inclusive, with each number printed on a separate line


# PEDAC
# P: understand the problem
# E: Examples / Test cases
# D: Data structure
# A: Algorithm
# C: Code

# identify even numbers, print them.
# inclusive (1 or 99, not even). Starts from 2, ends at 98

def print_even_nums():
    for even_nums in range(2, 100, 2):
        print(even_nums)
        
if __name__ == "__main__":
    print_even_nums()