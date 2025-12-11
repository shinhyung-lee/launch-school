'''
Input:  3 ints representing sides of a triangle
Output: A string representing the type of triangle / or
"invalid" to tell the triangle is not valid

Rules
- sum of the lengths of the two shortest sides must be greater
than the length of the longest side
- every side must have a length greater than 0 
- if any of the above two condition is not satisfied, invalid 
triangle
Questions

Data Structures
- int, float 
- if all three sides have the same length, return 'E'
- two sides have the same length, third one is different, return 'I'
- all three sides different: return 'S'

Algorithms:
IDEA
- guard clauses:
    - if any of the number is 0, return invalid
    - if the sum of two shorter lenghts aren't greater than the 
    longest one, return invalid 

Pseudocode:
- nums = [num1, num2, num3]
- using list NUMS and list comprehension, check invalid
- using min and max func, determine shortest and longest
- determine middle_val from min and max
- if sum shorter lengths not > longest one, return invalid
- min == middle == max, return 'Equilateral'
- min == middle OR middle == max, return 'Isosceles'
- min != middle AND middle != max, return 'Scalene'
'''

# [1, 3, 4]
def triangle(num1, num2, num3):
    sides = [num1, num2, num3]
    if any([side <= 0 for side in sides]):
        return 'invalid'
    min_side = min(sides)
    max_side = max(sides)
    sides.remove(min_side)
    sides.remove(max_side)
    middle_side = sides[0]
    if not (min_side + middle_side > max_side):
        return 'invalid'
    if min_side == middle_side == max_side:
        return 'equilateral'
    elif (min_side == middle_side) or (middle_side == max_side):
        return 'isosceles'
    elif (min_side != middle_side) and (middle_side != max_side):
        return 'scalene'
    

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True