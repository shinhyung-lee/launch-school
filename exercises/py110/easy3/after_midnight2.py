'''
Input:  (string) a time of day in 24 hour format
Output: (int) return the number of minutes before and after midnight, respectively

Rules
Explicit:
    - Both functions should return a value in the range 0 through 1439
Implicit:

Questions:

Data Structures:
    - int
    - string slicing
Algorithms (after_midnight):
    - extract "hour" and "minute" from "time_string" using string slicing
    - calculate "total_minutes" by multipling 60 to "hour" and adding "hour" and "minute"
        - if "total_minutes" is greater than 1440, get a modulus of "total_minutes" % 1440
    - return "total_minutes"

'''
MINUTES_IN_AN_HOUR = 60
HOURS_IN_A_DAY = 24 
MINUTES_IN_A_DAY = MINUTES_IN_AN_HOUR * HOURS_IN_A_DAY
def trim_leading_zero(time_unit):
    if time_unit[0] == '0':
        return time_unit[1]
    return time_unit

def after_midnight(time_string):
    hour = int(trim_leading_zero(time_string[0:2]))
    minute = int(trim_leading_zero(time_string[3:]))

    total_minutes = hour * MINUTES_IN_AN_HOUR + minute 
    if total_minutes >= MINUTES_IN_A_DAY:
        total_minutes %= MINUTES_IN_A_DAY 

    return total_minutes


def before_midnight(time_string):
    hour = int(trim_leading_zero(time_string[0:2]))
    minute = int(trim_leading_zero(time_string[3:]))

    total_minutes = hour * MINUTES_IN_AN_HOUR + minute 
    total_minutes += MINUTES_IN_A_DAY 
    if total_minutes >= MINUTES_IN_A_DAY:
        total_minutes %= MINUTES_IN_A_DAY 

    if total_minutes == 0:
        print(total_minutes)
        return total_minutes
    else:
        print(MINUTES_IN_A_DAY - total_minutes)
        return MINUTES_IN_A_DAY - total_minutes


# After Midnight
print(after_midnight("00:00") == 0)     # True
print(after_midnight("12:34") == 754)   # True
print(after_midnight("24:00") == 0)     # True

# Before Midnight
print(before_midnight("00:00") == 0)    # True
print(before_midnight("12:34") == 686)  # True
print(before_midnight("24:00") == 0)    # True