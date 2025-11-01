
# Vlad, your solution is correct.
# It will correctly tell leap or from non-leap years.
# However, it can improve in a few ways.
# First of all, your indentation is not consistent. Try to have 4-space indentation for your python code.
# Secondly, the logic can be improved. The code is going through multiple if statements.
# Going through each if statement, is_a_leap_year is getting reassigned.
# It's worth 

def is_leap_year(year):
    is_a_leap_year = False
    if year % 4 == 0:
        is_a_leap_year = True
    if year % 100 == 0:
        is_a_leap_year = False
    if year % 400 == 0:
        is_a_leap_year = True
    return is_a_leap_year