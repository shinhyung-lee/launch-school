
'''
Input: a list, delim (optional), ending_delimiter (optional)
Output: a string 

Rules:
- 

'''

def join_or(lst, delimiter=', ', ending_delimiter='or'):
    str_lst = [str(elem) for elem in lst]
    if len(lst) == 1:
        return str(lst[0])
    elif len(lst) == 2:
        return f'{lst[0]} {ending_delimiter} {lst[1]}'
    
    initial = lst[:-1]
    last = lst[-1]
    
print(join_or([1, 2]))                   # => "1 or 2"
print(join_or([1, 2, 3]))                # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))          # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))   # => "1, 2, and 3"