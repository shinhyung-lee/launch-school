# the code below will print 'neigh' because animal variable is assigned a string
# value 'horse'. 
# in our match-case statement, we are seeing what the value of animal is
# each case compares the value of animal with string values.

animal = 'horse'

match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse':
        print('neigh')
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricket*')