import requests
import config



def get_google_coords(city, state):
	"""
	Takes in a string of city and state and returns the coordinates depending on the google pin
	of the city location given.
	Parameters:
	City - City name in String
	State - State/Country name in String
	"""
    google_api = "https://maps.googleapis.com/maps/api/geocode/json?address={}+{}&key=" + config.google_api_key
    url = google_api.format(city, state)
    js = requests.get(url).json()['results'][0]['geometry']
    lat = js['location']['lat']
    long = js['location']['lng']
    coords = (float(lat), float(long))
    return coords

