from time import sleep
from urllib.request import urlopen
from urllib.parse import urlencode
from json import load

from restaurant import Restaurant

class GooglePlaces():
    def __init__(self):
        self.key = ""


    def request_restaurants(self, query):
        request_dict = self.__get_request_dict(query, "restaurant")
        return self.__restaurants_from_results(self.request_data(request_dict))


    def request_data(self, request_dict):
        required = ["location", "query", "key", "type"]
        if len([key for key in request_dict if key in required]) != len(required):
            print("Not enough info provided")
        if len(request_dict["location"].split(",")) != 2:
            print("Location format not correct: lat, lng")
        return self.__make_search_requests(request_dict)


    def __get_request_dict(self, query, request_type):
        return {
            "query": query,
            "type": request_type,
            "radius": 32000,
            "location": self.__get_current_location(),
            "key": self.key
        }


    def __make_search_requests(self, request_dict):
        base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
        results = []
        while True:
            request_url = f"{base_url}{urlencode(request_dict)}"
            response = urlopen(request_url)
            data = load(response)
            if data["status"] != "OK":
                sleep(1)
                continue
            if len(data["results"]) > 0:
                results = results + data["results"]
            if "next_page_token" not in data or len(data["next_page_token"]) == 0 or len(results) == 60:
                break
            request_dict["pagetoken"] = data["next_page_token"]
        return results


    def __get_current_location(self):
        url = "https://ipinfo.io/json"
        response = urlopen(url)
        data = load(response)
        if len(data) < 1:
            print("Current location was unable to be found")
            return ""
        return data["loc"]


    def __restaurants_from_results(self, results):
        return [Restaurant(result) for result in results]