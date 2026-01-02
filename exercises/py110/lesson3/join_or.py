def join_or(lst, delimiter=', ', word='or'):
    match len(lst):
        case 0:
            return ''
        case 1:
            return f'{lst[0]}'
        case 2:
            return f'{lst[0]} {word} {lst[1]}'
    
    leading_items = delimiter.join([str(elem) for elem in lst[:-1]])
    return f'{leading_items}{delimiter}{word} {lst[-1]}'

# test cases for 
# print(join_or([1, 2, 3]))               # => "1, 2, or 3"
# print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
# print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
# print(join_or([]))                      # => ""
# print(join_or([5]))                     # => "5"
# print(join_or([1, 2]))                  # => "1 or 2"
