# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         num_dict = {}
#         for i in range(len(nums)):
#             num_dict[i] = nums[i]
        
        
# Method 1: Brute-force (n^2)
# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if (nums[i] + nums[j] == target):
#             return [i, j]

# Method 2: using dictionary O(n)
# DOESN'T PASS TEST CASE 3
# num_dict = {}
#     for i in range(len(nums)):
#         num_dict[nums[i]] = i 
    
    
#     for num in num_dict:
#         diff = target - num 
#         if diff in num_dict:
#             return [num_dict[num], num_dict[diff]]
        
# is it better to have 
#   - idx be a key and num be a value?
#   OR
#   - num be an idx and idx be a value?
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    '''
    In: list, num
    Out: two ints
        - two indexes from the list that values sum up to `target`
        
    === EXAMPLES ===
    [2, 7, 11, 15] target = 9
    returns [0, 1]
    
    [3, 2, 4] target = 6
    returns [1, 2]
    
    
    === DATA STRUCTURES ===
    - dict (for better time complexity)
    
    - for loop (Brute-force)
        - O(n^2): solved it this way
    
    === ALGORITHMS ===
    
    
    === BRAINSTORM ===
    
    
    '''
    num_dict = {}
    for i in range(len(nums)):
        currNum = nums[i]
        print(i)
        diff = target - nums[i]
        print(diff)
        if diff in num_dict:
            return [i, num_dict[diff]]
        else:
            num_dict[currNum] = i

        
print(twoSum([2, 3, 7, 1], 10))
        
