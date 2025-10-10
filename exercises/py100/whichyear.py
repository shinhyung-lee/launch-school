# difference between year attribute and isocalendar method?

# year is what we consider normally

# isocalendar is a variant of Gregorian calendar
# The ISO year consists of 52 or 53 full weeks, and where a week starts on a Monday and ends on a Sunday.
# first week of an ISO year is the first (Gregorian) calendar week of a year containig a Thursday 
# today.isocalendar will return year, week, and weekday tuple 
# by accessing the first element with code, today.isocalendar()[0] we are getting the year value 

from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]
