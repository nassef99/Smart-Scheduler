"""
API getter for Ambee API.
"""
from accu_getter import ACCU_getter
from datetime import datetime, timedelta

now = datetime.now()
change = timedelta(hours=10)
date = now + change

place = "College Station"

getter = ACCU_getter()
print(getter.get_warnings(date, place))
