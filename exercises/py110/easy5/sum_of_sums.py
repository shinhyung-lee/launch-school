'''
Input:  A list of numbers
Output: Sum of sums of integers of each leading subsequence in the numbers list

Rules:
Explicit:
- List contains at least one number

Data Structures:
- Int: to keep track of sum of sums
- List: to keep track of leading subsequence
- Sum: built-in sum function to sum numbers in each subsequence

Algorithm:
    - total = 0
    - current_subsequence = []
    - Iterate through all indexes in the input nums list
        - add number at current index to current_subsequence
        - current_total : sum numbers at current_subsequence
        - add current_total to total 
    - return total 
'''

def sum_of_sums(nums):
    total = 0
    current_subsequence = []
    for idx in range(len(nums)):
        current_subsequence.append(nums[idx])
        total += sum(current_subsequence)
    return total 

print("Method 1")
print(sum_of_sums([3, 5, 2]) == 21)               # True
print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
print(sum_of_sums([4]) == 4)                      # True

def sum_of_sums2(nums):
    total_sum = 0
    running_sum = 0 
    
    for num in nums:
        running_sum += num 
        total_sum += running_sum 
    
    return total_sum

print("\nMethod 2")
print(sum_of_sums2([3, 5, 2]) == 21)               # True
print(sum_of_sums2([1, 5, 7, 3]) == 36)            # True
print(sum_of_sums2([1, 2, 3, 4, 5]) == 35)         # True
print(sum_of_sums2([4]) == 4)                      # True