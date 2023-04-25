"""
API getter for Ambee API.
"""

from .api_getter import API_getter
import requests
from decouple import config

class ACCU_getter(API_getter):
    def __init__(self):
        API_getter.__init__(self)
        self.key = config('ACCUWEATHER_KEY')

    def get_loc_key(self, name):
        # Get the location key for AccuWeather based on the entered location
        # TODO: Use more than the first result
        q = name
        apikey = self.key
        url = "http://dataservice.accuweather.com/locations/v1/cities/autocomplete?apikey=%s&q=%s" % (apikey, q)

        # Request from accuweather
        location_req = requests.request("GET", url)
        loc_json = location_req.json()

        # Check if no results
        # TODO: Check if message was successful
        if not loc_json:
            print("Dictionary empty, cannot give data")
            return -1

        # Use the first result for now and pull out key
        loc_key = loc_json[0]["Key"]
        return loc_key
        

    def get_warnings(self, date, name):
        # First translate the name to a location key
        loc_key = self.get_loc_key(name)
        if loc_key == -1:
            print("No weather data available, marking as warning")
            return True

        # Create url for request
        weather_url = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/%s?apikey=%s" % (loc_key, self.key)

        # Request and turn into json and get daily forecasts
        wthr_req = requests.request("GET", weather_url)
        wthr_json = wthr_req.json()

        if not wthr_json:
            print("Weather data empty, cannot determine weather")
            return True

        # print("DEBUG: json=\n", wthr_json)
        forecasts = wthr_json["DailyForecasts"]
        # Determine closest prediction to date
        timestamp = date.timestamp()
        distances = []
        for day in forecasts:
            time = day["EpochDate"]
            distance = abs(time - timestamp)
            distances.append(distance)
        closest_index = [i for i, x in enumerate(distances) if x == min(distances)][0]

        
        # Determine if there's a risk for rain (HasPrecipitation)
        data = forecasts[closest_index]
        if data["Day"]["HasPrecipitation"] or  data["Night"]["HasPrecipitation"]:
            return True
        else:
            return False
