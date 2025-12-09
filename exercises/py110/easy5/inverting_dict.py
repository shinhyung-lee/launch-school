''' 
PEDAC
INPUT:  A dict where both keys and values are unique 
OUTPUT: A dict, keys and values inverted from the input dict (keys become values, vice versa)

RULES
Explicit:
    - both keys and values are unique 
Implicit:

Data Structures:
    - dictionary, obviously 
    - dictionary comprehension
Algorithms:
IDEA:
    - For all items in dict, invert keys and values using dict comprehension
Pseudocode:
    - For each item in dict, switch keys and values 
        - use dict.items() 

'''

def invert_dict(dict):
    return { value: key for key, value in dict.items() }

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True