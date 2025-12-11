'''
Input:  int representing a year
Output: number of friday the 13th in that year 
Jan 13, Feb 13, Mar 13, ... Dec 13

Rules
Explicit:
- input year > 1752
Implicit:

Data Structures
- int : to tally how many Friday the 13ths are in a year
- datetime module python
- range : to iterate through months in a year

Algorithms
IDEA
- for each month in a year, if Friday is the 13th, tally 
- return the tallied number 
Pseudocode
- import datetime module
- NUM_MONTHS_IN_A_YEAR = 12
- FRIDAY = 4
- total = 0
- for every month in a year, check if 13th is Friday (using range)
    - If so, increment total
- return total
'''
import datetime

def friday_the_13ths(year):
    NUM_MONTHS_IN_A_YEAR = 12
    FRIDAY = 4
    total = 0
    for month in range(1, NUM_MONTHS_IN_A_YEAR + 1):
        if datetime.date(year, month, 13).weekday() == FRIDAY:
            total += 1

    return total

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True