import requests
from urllib.parse import quote_plus
from config.api_config import API_KEY

import requests
from urllib.parse import quote_plus
from config.api_config import API_KEY

def get_coordinates(address):
    """Get the latitude and longitude of an address."""
    encoded_address = quote_plus(address)
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={encoded_address}&key={API_KEY}"
    response = requests.get(url)
    if response.ok:
        results = response.json().get("results", [])
        if results:
            location = results[0]["geometry"]["location"]
            return location["lat"], location["lng"]
    return None

def get_famous_landmarks(city, radius=10000):
    """Fetch famous landmarks from the Google Places API."""
    coordinates = get_coordinates(city)
    if not coordinates:
        return []

    lat, lng = coordinates
    location = f"{lat},{lng}"
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=landmarks+in+{city}&location={location}&radius={radius}&key={API_KEY}"
    
    landmarks = []
    while url:
        response = requests.get(url)
        if response.ok:
            data = response.json()
            results = data.get("results", [])
            
            # Filter out landmarks with missing or invalid geometry/location
            for landmark in results:
                geometry = landmark.get("geometry", {})
                location = geometry.get("location", {})
                if location.get("lat") is not None and location.get("lng") is not None: # needs to be a valid location
                    if not landmark.get('name', '').strip().lower() == city.strip().lower(): # needs to not be same the same spot as the city itself
                        landmarks.append(landmark)
                        print(landmark.get('name', '') + str( "and the name of the city is ") + city.strip())

            # Handle pagination with next_page_token if needed
            next_page_token = data.get("next_page_token")
            if next_page_token:
                url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken={next_page_token}&key={API_KEY}"
            else:
                url = None
        else:
            break

    return landmarks[:30]  # Return the first 30 valid landmarks