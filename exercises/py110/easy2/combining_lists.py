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
def union(lst1, lst2):
    union_set = set()
    for num in lst1:
        union_set.add(num)
    for num in lst2:
        union_set.add(num)
    
    return union_set 

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True