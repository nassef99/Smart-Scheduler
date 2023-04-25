"""
Wrapper to take input from the application and interface with the APIs used.
"""
from accu_getter import *
from ambee_getter import *

class API_wrapper:
    def __init__(self):
        # Create an object for each API and load into a list
        ambee = AMBEE_getter()
        accu = ACCU_getter()
        # Lists of objects and warnings
        self.api_gets = [ambee, accu]
        self.warnings = []

    def get_warnings(self, date, place):
        for api in self.api_gets:
            self.warnings.append(api.get_warnings(date, place))
        return self.warnings
