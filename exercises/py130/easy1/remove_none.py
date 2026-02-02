vals = [1, 'hello', None, 15.3, 'kiwi', None, 'jimmy']
none_removed = list(filter(lambda val: val is not None, vals))
print(none_removed)