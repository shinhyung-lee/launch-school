# using datetime module in python, how would you obtain the current date and time?
from datetime import datetime

now = datetime.now()

print(f'Current date: {now.strftime("%x")}')
print(f'Current time: {now.strftime("%X")}')
