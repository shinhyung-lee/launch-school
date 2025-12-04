''' 
PEDAC

Input:  number of minutes before or after midnight. 
Output: returns the time of day in 24-hour format (hh:mm) in string 

Rules
Explicit:
    - If the number of minutes is positive, the time is after midnight.
    - If the number of minutes is negative, the time is before midnight.
    - Should not use Python's datetime module.
Implicit:

Questions:
    - What if the input number is 0? => Return 00:00 
Data Structures:
    - int : using modulus and remainder 
    - string : output is in string format

Algorithms: 
    - if the minute is negative, convert the number to positive minute
        - "negative_minute_to_positive" function takes negative minute
        - 
    - using quotient and remainder, get hour and minute of the day from minute
        - if minute is greater than 1440, subtract 1440 from minutes until 0 <= minute < 1440
    - return the stringified time
'''
NUM_HOUR_IN_A_DAY = 24 
NUM_MINUTE_IN_AN_HOUR = 60
MINUTES_PER_DAY = NUM_HOUR_IN_A_DAY * NUM_MINUTE_IN_AN_HOUR

def time_of_day(minute):
    while minute < 0:
        minute += MINUTES_PER_DAY
    
    minute = minute % 1440
    
    final_hour, final_minute = divmod(minute, NUM_MINUTE_IN_AN_HOUR)
    return f"{final_hour:02d}:{final_minute:02d}"

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True