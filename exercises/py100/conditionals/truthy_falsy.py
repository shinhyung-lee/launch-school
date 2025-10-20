
# falsy values
'''
0 - int
0.0 -float
'' - empty string
False - False boolean 
[] - empty list
'''

values = [False, None, 0, 0.0, 0j, '', [], {}, (), set(), frozenset(), range(0)]

for value in values:
  print(f'{repr(value)} -> {bool(value)}')