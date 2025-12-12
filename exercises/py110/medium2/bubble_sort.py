'''
Input  : a list of numbers
Output : a list, sorted using bubble sort

Rules
Explicit:
- list contains at least two elements 

Data Structure
- List

Algorithms:
IDEA
- iterate the list using bubble sort until the list is completely
sorted
- for each iteration, keep how many swaps happen using "num_swap" 
variable
- return the sorted list 

Pseudocode
[2, 5, 3]
[2, 3, 5] num_swap = 1
- num_swap = -1 
- while num_swap != 0:
    num_swap = 0 
    for idx in range(len(list) - 1):
        if list[idx] > list[idx + 1]:
            swap_list_elems(list, idx, idx + 1)
            num_swap += 1
- return list 

- swap_list_elems(list, a, b):
    temp = list[a]
    list[a] = list[b]
    list[b] = temp
'''

# def swap_list_elems(list, a, b):
#     temp = list[a]
#     list[a] = list[b]
#     list[b] = temp

def bubble_sort(lst):
    # num_swap = -1 
    while True:
        # num_swap = 0 
        swapped = False 
        for idx in range(len(lst) - 1):
            if lst[idx] > lst[idx + 1]:
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
                swapped = True 
            else:
                continue 
        if not swapped:
            break 
    return lst

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True