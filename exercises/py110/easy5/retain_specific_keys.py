'''
INPUT: A dict and a list of keys
OUTPUT: A new dict that contains only the key/value pairs from the specified keys

Data Structures:
- dictionary : dict comprehension

Algorithms:
IDEA
    - Filter through the dictionary, only select the key value pairs with the specified keys from the list 
Pseudocode:
    - 
'''
# { 'red': 1, 'green': 2 }, input_list = ['red']
def keep_keys(dict, keys):
    return { key: value for key, value in dict.items() if key in keys }

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True