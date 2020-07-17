class Restaurant():
    __slots__ = ["name", "location", "open_now", "rating", "user_rating", "price_level"]
    def __init__(self, result_json):
        self.name = result_json["name"]
        self.location = result_json["formatted_address"]
        self.open_now = self.__is_open(result_json)
        self.rating = result_json["rating"]
        self.user_rating = result_json["user_ratings_total"]
        self.price_level = result_json["price_level"] if "price_level" in result_json.keys() else 0
    
    def __str__(self):
        return f"Name: {self.name}\nLocation: {self.location}\nOpen: {self.open_now}\nRating: {self.rating}\nRating: {self.user_rating}\nPrice Level: {self.price_level}"
    
    def __is_open(self, result_json):
        if "opening_hours" in result_json:
            return "Yes" if result_json["opening_hours"]["open_now"] else "No"
        else:
            return "Maybe?"