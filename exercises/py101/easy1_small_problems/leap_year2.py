
def is_gregorian_leap_year(year):
    if year % 400 == 0:
        return True 
    elif year % 100 == 0:
        return False 
    elif year % 4 == 0:
        return True 
    else:
        return False 

def is_julian_leap_year(year):
    return year % 4 == 0

def is_leap_year(year):
    if year < 1752:
        return is_julian_leap_year(year)
    else:
        return is_gregorian_leap_year(year)
    
# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)