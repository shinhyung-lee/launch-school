'''
Input:  Two lists of integers of the same length
Output: A new list where each element is the product of the corresponding elements from the two lists 

Data Structures:
    - list: 
    - range and idx
    - len built-in function 
Algorithms:
IDEA
    - MULTIPLIED = []
    - for every index in list 1,
        - multiply elements with the same index, append to MULTIPIED
    - return MULTIPLIED
Pseudocode:

Examples: 
Input: [1, 2], [3, 4]
Output: [3, 8]
'''

def multiply_items(nums1, nums2):
    list_length = len(nums1)
    multiplied = []
    
    for idx in range(list_length):
        multiplied.append(nums1[idx] * nums2[idx])
        
    return multiplied

print('Method 1')
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

def multiply_items2(nums1, nums2):
    return [nums1[i] * nums2[i] for i in range(len(nums1))]

print('\nMethod 2')
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items2(list_a, list_b) == [4, 10, 18]) # True