"""
API getter for Ambee API.
"""

from api_getter import API_getter
import requests
from decouple import config

class AMBEE_getter(API_getter):
    def __init__(self):
        API_getter.__init__(self)
        self.key = config('AMBEE_KEY')

    @staticmethod
    def get_warnings(date, place):
        # Placewise search with Ambee
        # TODO: Add check date to make sure the date isn't too far out

        # Create query
        url = "https://api.ambeedata.com/forecast/pollen/by-place"
        querystring = {"place":place}
        headers = {
            'x-api-key':self.key,
            'Content-type': "application/json"
        }

        # TODO: Add try-catch block in case request goes wrong
        response = requests.request("GET", url, headers = headers, params = querystring)
        json = response.json()
        # print("DEBUG: json =\n", json)
        if(json["message"] != 'success'):
            print("Request failed, likely exceeded number allowed.")
            return True

        # Determine closest prediction to date
        timestamp = date.timestamp()
        distances = []
        for point in json["data"]:
            time = point["time"]
            distance = abs(time - timestamp)
            distances.append(distance)
        closest_index = [i for i, x in enumerate(distances) if x == min(distances)][0]

        # Determine if there's a risk for any pollen type
        data = json["data"][closest_index]
        for risk in data["Risk"]:
            if data["Risk"][risk] == "High":
                return True

        return False
