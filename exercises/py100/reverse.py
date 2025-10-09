# there are different ways to reverse a string "hello" to "olleh"
# one way to do is using slicing 

my_str = "hello"
reversed_str = my_str[::-1]

# second way is using reversed() function with join()
my_str2 = "hello"
reversed_str2 = "".join(reversed(my_str2))