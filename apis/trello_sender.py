"""
API getter for Ambee API.
"""

import requests
from decouple import config

class TRELLO_sender():
    def __init__(self, _token = config('TRELLO_TOKEN')):
        # Adding tokens may be useful in the future
        self.key = config('TRELLO_KEY')
        self.oauth = config('TRELLO_OAUTH')
        self.token = _token
    
    def send_event(self, event):
        # Get the user's first board and first list of board
        boards_url = "https://api.trello.com/1/members/me/boards?key=%s&token=%s" % (self.key, self.token)
        boards_req = requests.request("GET", boards_url)
        boards_json = boards_req.json()
        if not boards_json:
            print("No boards to use, exiting without sending event")
            return False

        list_id = boards_json[0]["id"]
        
        list_url = "https://api.trello.com/1/boards/%s/lists?key=%s&token=%s" % (list_id, self.key, self.token)
        list_req = requests.request("GET", list_url)
        list_json = list_req.json()
        if not list_json:
            print("No lists to add cards to, exiting without sending event")
            return False

        trello_list_id = list_json[0]["id"]
        card_url = "https://api.trello.com/1/cards"
        query = {
            'key' : self.key,
            'token' : self.token,
            'idList' : trello_list_id,
            'pos' : 'top'
        }

        # Add various options if they're filled in the Event
        # Complete, convert True and False to Javascript's text equivalent
        if hasattr(event, "is_complete"):
            query['dueComplete'] = "true" if event.is_complete else "false"

        # Due date
        if hasattr(event, 'end_time'):
            query['due'] = event.end_time

        elif hasattr(event, 'start_time'):
            query['due'] = event.start_time

        # Name, if available
        if hasattr(event, 'event_name'):
            query['name'] = event.event_name

        else:
            query['name'] = "No Event Name"

        card_req = requests.request("POST", card_url, params=query)
        # print("DEBUG\n", card_req.text)
        
        # On success
        return True
