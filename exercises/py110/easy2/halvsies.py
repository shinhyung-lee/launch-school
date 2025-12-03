'''
PEDAC
Input: a list
Output: a list that contains two elements, both of which are lists.

Rules
Explicit:
- Put the first half of the original list in the first element of the return value
- Put the second half of the original list in the second element of the return value
- If the original list contains an odd number of elements, place the middle element in the first list 
Implicit:
- 

Questions:
-What if the original list is empty?
    -Both lists in the returning list will be empty lists

Data Structures:
-list 

Algorithm: 
    - initialize a "container_list" as an empty list []
    - initialize "first_element" as an empty list []
    - initialize "second_element" as an empty list []

    - if the length of the original list "container_list" is 0, 
        - container_list.append(first_element), container_list.append(second_element)
        - return container_list 
    - get the middle index of the original list 
        - "middle_index" = len(lst) / 2 
        - append first half of the original list to "first_element"
        - append second half of the original list to "second_element"
        - append first and second element to container_list
    - return container_list 
'''

def halvsies(lst):
    # 6 : 3, 5 : 3 / 4 : 2, 3 : 2
    middle_index = (len(lst) + 1) // 2
    first_half = lst[:middle_index]
    second_half = lst[middle_index:]
   
    return [first_half, second_half]
    
# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])