'''
Input:  A list
Output: A list sorted in ascending order (sorted with merge sort)

Rules 
Explicit:
- 
Implicit:

Data Structures:
- list 
- 

Algorithms:
- base case
- divide it into two lists 
    - apply merge function into each list 
- feed the divided lists into merge_sort 
- 

- each list length is 1 
'''

# merge two lists into one
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

def merge_sort(lst):
    pass

# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)