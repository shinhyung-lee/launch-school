'''
Input: Two lists
Output: Set that contains the union of two lists converted to sets

Data Structure: set

Algorithm:
    - get a union of two sets and return
'''

def merge_sets(list1, list2):
    return set(list1) | (set(list2))

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True