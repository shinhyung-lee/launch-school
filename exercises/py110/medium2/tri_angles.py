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
def is_valid(angles):
    total_angle = sum(angles)
    all_non_zero = all([angle > 0 for angle in angles])
    return all_non_zero and total_angle == 180

def is_right_triangle(angle):
    return angle == 90 

def is_acute_triangle(angle):
    return angle < 90

def get_triangle_type(angles):
    if any([is_right_triangle(angle) for angle in angles]):
        return 'right'
    elif all([is_acute_triangle(angle) for angle in angles]):
        return 'acute'
    else:
        return 'obtuse'

# 'right', 'acute', 'obtuse', or 'invalid'
def triangle(angle1, angle2, angle3):
    angles = [angle1, angle2, angle3]
    
    if is_valid(angles):
        return get_triangle_type(angles)
    else:
        return 'invalid'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True