from functools import reduce

strs = ['hello', 'world', 'my', 'name', 'yang yi']
string = reduce(lambda accm, start: accm + ' ' + start, strs)
print(string)