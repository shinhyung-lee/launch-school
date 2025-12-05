'''
Input:  two integers. 1) count, 2) starting number of a seq that your function will create
Output: A list containing the same number of elements as the "count" arg

Rules
Explicit:
    - Value of each element in the returning list should be a multiple of the starting number 
    - count will always be an integer greater than or equal to 0 (count >= 0)
    - If count is 0, the function should return an empty list 

Data Structures:
    - list: to contain the returning list 
    - range: to iterate the range of numbers from starting number up to "count" number of numbers. 
Algorithms: 
    - create an empty list "multiples"
    - iterate a range from "starting_number" to "count" + 1
        - append "starting number" * "count" to list "multiples"
    - return "multiples"
'''
def sequence(count, starting_number):
    multiples = [] 
    for multiplier in range(1, 1 + count):
        multiples.append(starting_number * multiplier)
    return multiples

print("Method 1")
print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True

def sequence2(count, starting_number):
    # using list comprehension
    return [starting_number * multiplier for multiplier in range(1, 1 + count)]

print("Method 2")
print(sequence2(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence2(4, -7) == [-7, -14, -21, -28])     # True
print(sequence2(3, 0) == [0, 0, 0])                # True
print(sequence2(0, 1000000) == [])                 # True