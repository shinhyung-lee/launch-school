
'''
Algorithms:
    - intialize an empty list "name_list"
    - split our name string and store in "name_list"
    - using list unpacking, initialize variables "first" and "last" to two values from "name_list"
    - return f-string "{last}, {first}"
'''

def swap_name(name):
    first, last = name.split()
    return f"{last}, {first}"

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True