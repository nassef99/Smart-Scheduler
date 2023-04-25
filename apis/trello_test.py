"""
API getter for Ambee API.
"""
from trello_sender import TRELLO_sender
from datetime import datetime, timedelta

class event_tester():
    def __init__(self, _name, _date, _complete = False):
        self.event_name = _name
        self.start_time = _date
        self.is_complete = _complete

date = datetime.now()
change = timedelta(hours=10)
new_date = date + change

sender = TRELLO_sender()
test_event = event_tester("AnotherTest", new_date, True)
print(sender.send_event(test_event))
