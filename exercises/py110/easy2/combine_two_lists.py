'''
PEDAC

Input: two lists 
Output: a new list that contains all elements from both list arguments, 
with each element taken in alternation.

Rules
Explicit:
    - both input lists are non-empty
    - they have the same number of elements
Implicit:

Questions

Data Structures:

Algorithms:
    - initialize an empty list "combined"
    - combine two lists into "zipped_tuple" using built-in zip function
    - iterate through "zipped_tuple"
        - for each tuple pair, unpack them into "first" and "second" variable
        - append "first" and "second" into "combined" list
    -return "combined" list 

'''
def interleave(lst1, lst2):
    combined = []
    zipped_tuple = zip(lst1, lst2)

    for first, second in zipped_tuple:
        combined.extend([first, second])
    return combined

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

list1 = [9, 10, 'abc']
list2 = ['acd', {'a': 1}, 100]
expected = [9, 'acd', 10, {'a': 1}, 'abc', 100]
print(interleave(list1, list2) == expected)      # True


# second version
def interleave2(lst1, lst2):
    new_list = []
    for idx in range(len(lst1)):
        new_list.extend([lst1[idx], lst2[idx]])
    return new_list

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave2(list1, list2) == expected)      # True