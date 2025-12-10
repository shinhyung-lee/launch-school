'''
Input:  int number
Output: int number but maximum rotation applied

Rules
Explicit
Implicit
    - If the digits in number is n, maximum rotation rotates the number n - 1 times
    - 

Questions

Data Structures:
    - str
    - int (putting strings back)
    - rotate_rightmost_digits (RRD) function
Algorithms: 
IDEA
    - RESULT = ''
    - Rotate the n-digit num with RRD (num, n)
    - Divide the number into two parts. 
        - KEEP: first digit
            - concatenate to RESULT 
        - ROTATE: str(num)[1:]
        - Rotate gets fed into RRD function 
    - Repeat the above process until num >= 2 
        - stringified_num = str(num)
        - len(stringified_num) >= 2

Pseudocode:
    - result = '' 
    - str_num = str(num)
    - while len(stringified_num) >= 2:
        str_num = str(RRD(str_num, len(str_num)))
        result += str_num[0]
        str_num = str_num[1:]
    - result += str_num
    - return int(str_num)
35 
int(53)
105 
result = '015'
return int(015)
'''

def rotate_rightmost_digits(num, digit):
    untouched = str(num)[:-digit]
    rotate_target = str(num)[-digit:]
    rotated = rotate_target[1:] + rotate_target[0]
    return int(untouched + rotated)

def max_rotation(num):
    number_digits = len(str(num))
    for count in range(number_digits, 1, -1):
        num = rotate_rightmost_digits(num, count)
    
    return num 
    
print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True