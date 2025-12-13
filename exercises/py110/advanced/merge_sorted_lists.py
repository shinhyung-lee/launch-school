'''
Input:  Two lists that are sorted 
Output: A list, two input lists are sorted in ascending order

Rules

Data Structures
- List 
Algorithms
IDEA
- Initialize an empty list MERGED
- From two lists, compare first element of each list and append the smaller
one to MERGED (until one list becomes empty)
- Append the remaining list that has element to MERGED
- Return MERGED

Pseudocode
- merged = []
- idx1, idx2 = 0, 0
- while idx1 is smaller than the length of list1, 
    or idx2 is smaller than the length of list2,
    - if list1[idx1] < list2[idx2]:
        - add list1[0] to merged 
        - increment idx1 by 1
    - else
        - add list2[0] to merged
        - increment idx2 by 1
- if idx1 is smaller than length of list 1
    - append list1[idx1:] to merged (extend)
- else,
    - append list2[idx2:] to merged (extend)
'''
# [2], [1, 5] 
# idx1 = 0, idx2 = 0
# [1]
# idx1 = 0, idx2 = 1
# [1, 2]
# idx1 = 1, idx2 = 1

def merge(lst1, lst2):
    merged = []
    idx1, idx2 = 0, 0
    while idx1 < len(lst1) and idx2 < len(lst2):
        if lst1[idx1] < lst2[idx2]:
            merged.append(lst1[idx1])
            idx1 += 1
        else:
            merged.append(lst2[idx2])
            idx2 += 1
            
    if idx1 < len(lst1):
        merged.extend(lst1[idx1:])
    else:
        merged.extend(lst2[idx2:])
    return merged

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)