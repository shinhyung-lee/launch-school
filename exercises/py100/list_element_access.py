# Locate the documentation for the list built-in object in Python Documentation.

# How can we access the second element ('and') in the list ['fish', 'and', 'chips']?

def access_second(l):
  return l[1]


if __name__ == '__main__':
  assert access_second(['fish', 'and', 'chips']) == 'and'
  print(access_second(['fish', 'and', 'chips']))