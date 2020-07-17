import sys
from random import choice

from googleplaces import GooglePlaces

def main():
    query = "Restaurant" if len(sys.argv) < 2 else " ".join([ argv for argv in sys.argv if argv != sys.argv[0]])
    google_places = GooglePlaces()
    restaurants = google_places.request_restaurants(query)
    chosen_restaurant = choice(restaurants)

    print(chosen_restaurant)

if __name__ == "__main__":
    main()