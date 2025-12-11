'''
Input:  Three int values, which are 3 angles of a triangle
Output: A string value indicating what type of triangle it is


Rules
Explicit:
Right: One angle is a right angle (90 degrees)
Acute: All three angles are less than 90 deg
Obtuse: One angle is greater than 90 deg 

-To be a valid triangle:
    - every angle must be greater than 0
    - sum of the angles must be exactly 180 degrees
    - 
'''
def is_valid(angle1, angle2, angle3):
    angles = [angle1, angle2, angle3]
    return all([angle > 0 for angle in angles]) and sum(angles) == 180

# 'right', 'acute', 'obtuse', or 'invalid'
def triangle(angle1, angle2, angle3):
    big = max(angle1, angle2, angle3)
    small = min(angle1, angle2, angle3)
    middle = 180 - big - small 
    
    if not is_valid(angle1, angle2, angle3):
        return 'invalid'
    
    if big > 90:
        return 'obtuse'
    elif big == 90:
        return 'right'
    else:
        return 'acute'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True