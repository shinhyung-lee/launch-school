
'''
PEDAC
Input:  a floating point number representing an angle between 0 and 360 degrees. 
Output: a string representing the angle in degrees, minutes, and seconds. 

Rules
Explicit:

Implicit:
    - 360 degrees = 0 degrees. If the angle exceeds 360 deg, it will be original degree - 360 degree.
    - Degree: whole number to the left of the decimal point
    - Minute: Take decimal part of the degrees and multiply it by 60
        - The whole number is your minutes
    - Seconds: take the remaining decimal part from previous step and multiply by 60
        - the result is seconds. Round to the nearest whole number if there is a decimal remaining
    
Questions:

Data Structures:
    - list: to store degree, minute, and seconds. 
    - float: involves multiplication and divmod
    - string: to make the final string that is returned

Algorithms:
    - Given the original floating point number "number", get a quotient and modulus of that number by 
        dividing the number by 1
            -"degree" variable: quotient
            -"remainder" variable: modulus part
    -We use "remainder" variable from the previous step to get "minute"
        - Multiply "remainder" by 60. 
        - Whole number part is "minute"
        - Store decimals as "remainder"
    -We use "remainder" variable from the previous step to get "second"
        - Multiply "remainder" by 60.
        - Whole number part is "second".
    - Compose and return a string with "degree", "remainder", and "second" variables using 
      string interpolation
        - f-string

Challenge 2
Degree not 0 <= angle <= 360 
Algorithm:
'''

DEGREE = "\u00B0" # degree symbol
def dms(angle):
    is_negative = False 
    if angle < 0:
        is_negative = True 

    angle = abs(angle)
    degree, remainder = divmod(angle, 1)
    remainder = remainder * 60
    minute, remainder = divmod(remainder, 1)
    remainder = remainder * 60
    second, remainder = divmod(remainder, 1)

    if is_negative:
        return f"-{int(degree)}{DEGREE}{int(minute):02d}'{int(second):02d}\""
    else:
        return f"{int(degree)}{DEGREE}{int(minute):02d}'{int(second):02d}\""

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

# Challenge 1 (Got'em)
# print(dms(-1))   # -1°00'00"
# print(dms(400))  # 400°00'00"
# print(dms(-40))  # -40°00'00"
# print(dms(-420)) # -420°00'00"

# Challenge 2
print(dms(-1))   # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420)) # 300°00'00"