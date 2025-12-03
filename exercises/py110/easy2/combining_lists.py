'''
Prompt: Write a function that takes two lists as arguments and returns a set that contains the union 
of the values from the two lists. You may assume that both arguments will always be lists.

Input: two lists
Output: A set that contains the union of the values from the two lists

Rules:
Explicit:
    - both arguments wlil always be lists
Implicit:

Data Structures:
    - set: to combine elements from two lists

Algorithm:
    - initialize a variable "union_set" 
    - Iterate lst1, add each element to "union_set"
        -Do the same for lst2
    -return "union_set"
'''
def copy_non_dups_to(result_set, lst):
    for value in lst:
        result_set.add(value)

def union(lst1, lst2):
    union_set = set()
    copy_non_dups_to(union_set, lst1)
    copy_non_dups_to(union_set, lst2)
    
    return union_set 

def union2(lst1, lst2):
    return set(lst1).union(set(lst2))

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
print(union2([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True