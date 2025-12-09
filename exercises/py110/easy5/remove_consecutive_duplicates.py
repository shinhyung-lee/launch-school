

'''
Input:
Output:

Data Structures:
    - int 
    - list: to store new_list 
Algorithms:
IDEA
    - if len(nums) == 0: 
        return []
    - new_nums = [nums[0]]
    - current_num = nums[0]
    - from index 1 to the end of list
        - if number at current index is not equal to current_num,
            - add to new_nums 
            - update current_num to number at current index
        - else: 
            - move onto the next index
    - return new_nums

Pseudocode:
'''

def unique_sequence(nums):
    if len(nums) == 0:
        return []
    new_nums = [ nums[0] ]
    current_num = nums[0]
    for idx in range(1, len(nums)):
        if nums[idx] != current_num:
            new_nums.append(nums[idx])
            current_num = nums[idx]
        else: # nums[idx] == current_num
            continue 
    return new_nums

print("Method 1")
original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

# Non-consecutive duplicates are kept
original = [1, 2, 1, 3]
expected = [1, 2, 1, 3]
print(unique_sequence(original) == expected)      # True