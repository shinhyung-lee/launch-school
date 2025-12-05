'''
PEDAC

Input:  a list
Output: a reversed list 

Rules
Explicit:
    - Mutate the input list in-place
    - returned list is the same object as the argument
    - should not use python list.reverse
    - should not use a slice [::-1]
Implicit:

Questions:
    - What if the list is empty?
        - return an empty list 
    - Is swap different odd-length and even-length lists? 

Data Structures:
    - list 

Algorithms: 
- "left_index": (len(list) // 2) - 1
- from index 0 to "left_index", perform swap for each element
    - Swap
        - earlier index: "earlier"
        - later index "later": (len(list) - 1) - i
        - there are two indexes. i, j
        - store the value of earlier-indexed element in temp
        - reassign the earlier-indexed element the value of later-indexed element
        - reassign the later-indexed element the value of temp
'''


def reverse_list(list):
    left_index = len(list) // 2 - 1
    for idx in range(0, left_index + 1):
        earlier_idx = idx 
        later_idx = (len(list) - 1) - earlier_idx
        temp = list[earlier_idx]
        list[earlier_idx] = list[later_idx] 
        list[later_idx] = temp
    return list

print("Method 1")
list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True


def reverse_list2(list):
    first = 0
    last = -1
    
    while first < (len(list) // 2):
        list[first], list[last] = list[last], list[first]
        first += 1
        last -= 1
    
    return list 
    

print("\nMethod 2")
list1 = [1, 2, 3, 4]
result = reverse_list2(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list2(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list2(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list2(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True