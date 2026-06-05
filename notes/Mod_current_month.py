#Print current month of the calendar

import datetime
import calendar

n = datetime.datetime.now()

print(f"Current Date: {n.day} {calendar.month_name[n.month]} {n.year}")
