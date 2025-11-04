
'''
What is your age? 30
At what age would you like to retire? 70

It's 2024. You will retire in 2064.
You have only 40 years of work to go!
'''

from datetime import date 
current_year = date.today().year

current_age = int(input("What is your age? "))
retirement_age = int(input("At what age would you like to retire? "))
years_to_wait = retirement_age - current_age
retirement_year = current_year + years_to_wait

print(f"It's {current_year}. You will retire in {retirement_year}.\n"
      f"You have only {years_to_wait} years of work to go!")
