'''
Input:  number, digit to rotate
Output: number, rotated according to the input digit 

Data Structures:
    - str : 
    - int : convert str to int 
Algorithms:
    - divide original int into two strings 
        - untouched = str(num)[:-digit] # string
        - rotate_target = str(num)[-digit:] 
        - rotated = str[1:] + str[0] # string
    - return ''.join([untouched, rotated])
'''

# code is rather messy
def rotate_rightmost_digits(num, digit):
    untouched = str(num)[:-digit]
    rotate_target = str(num)[-digit:]
    rotated = rotate_target[1:] + rotate_target[0]
    return int(''.join([untouched, rotated]))

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True