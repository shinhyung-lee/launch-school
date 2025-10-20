# print function prints out True
# with the values assigned to speed, acceleration, and breaking_force variables
# is_moving evaluates to True and (False or True) 
# this evaluates to True and True, which is True.

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)