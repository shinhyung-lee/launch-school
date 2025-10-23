# numbers should be a collection, but instead the original code added 6 numbers as arguments
# that's why the typeError is complaining we gave the function 6 when only 1 positional argument is allowed.

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0)
find_first_nonzero_among(1)