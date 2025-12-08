'''
Input:  A dictionary 
Output: A list (keys from dictionary sorted by values associated with each key)

Rules
Explicit:
    - key: string, value: number 
Implicit:

Questions

Data Structures:
    - list (returning value is list)
    
Algorithms: 
    - helper function "sort_by_value"
        - given key, value pair
        - return value
    - initialize an empty list "sorted_keys"
        - use list comprehension to sort dictionary by values and return corresponding keys
'''

# return its keys sorted by values associated with each key
def sort_key(item):
    return item[1] 

def order_by_value(dict):
    sorted_items = sorted(dict.items(), key=sort_key)
    return [key for key, _ in sorted_items]

my_dict = {'p': 8, 'q': 2, 'r': 6}

keys = ['q', 'r', 'p']
print(order_by_value(my_dict)) #== keys)  # True