# Python print example

import datetime
import calendar

now = datetime.datetime.now()

print("\n At this moment, the time is:", now)
print("\n")

# Print this year calendar 
print(calendar.month(now.year, now.month))

print('\n This output is from the app.py file copied into the alpine image')


