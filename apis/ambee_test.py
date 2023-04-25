"""
API getter for Ambee API.
"""
from ambee_getter import AMBEE_getter
from datetime import datetime, timedelta

now = datetime.now()
change = timedelta(hours=10)
date = now + change

place = "College Station"

getter = AMBEE_getter()
print(getter.get_warnings(date, place))
