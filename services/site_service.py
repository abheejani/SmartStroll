# services/site_service.py

import requests
from urllib.parse import quote_plus
from config.api_config import API_KEY
from services.graph_service import build_graph

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
            landmarks.extend(data.get("results", []))
            next_page_token = data.get("next_page_token")
            if next_page_token:
                url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken={next_page_token}&key={API_KEY}"
            else:
                url = None
        else:
            break
    return landmarks[:20]