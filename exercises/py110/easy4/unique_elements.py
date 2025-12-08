
'''
Input:  Two lists of numbers
Output: A set with difference of set1 and set2. 
Set1 is formed from list 1. Set2 is formed from list 2.

'''

def unique_from_first(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return set1.difference(set2)

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})