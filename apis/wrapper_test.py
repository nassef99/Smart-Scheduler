"""
Wrapper to take input from the application and interface with the APIs used.
"""
from api_wrapper import API_wrapper
from datetime import datetime, timedelta

date = datetime.now()
change = timedelta(hours=10)
new_date = date + change

tester = API_wrapper(new_date, "College Station")
print(tester.get_warnings())

