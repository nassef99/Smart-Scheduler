"""
A virtual class for all APIs that give warnings to follow.
Has to initialize with a key, 
"""
class API_getter():

    def __init__(self):
        # Nothing needed here, but a key will have to be set
        # in the child classes
        self.key = -1
        self.warnings = []

    def get_warnings(self, date, place):
        # All child classes should implement this
        return self.warnings
