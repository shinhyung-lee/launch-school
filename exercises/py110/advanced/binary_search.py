'''
Input:  
Output: -1 if target not found in lst. Otherwise, The index 
        where it was found

Algorithm:
- if lst[0] == target:
    return 
- middle_val = lst[len(lst) // 2]
- get first_half = lst[:len(lst) // 2]
- later_half = lst[len(lst) // 2:]

- if target > middle_val:
    - binary_search(later_half)
- else:
    - binary_search(first_half)
-

['chris', 'chao', 'john', 'peter'] 'jason'
mid = 1 > low = 2 
mid = (2) + (0) = 2

'''

def binary_search(lst, target):
    low = 0 
    high = len(lst) - 1 
    
    while low <= high:
        mid = low + (high - low) // 2
        if lst[mid] == target:
            return mid 
        elif lst[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1 

# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)