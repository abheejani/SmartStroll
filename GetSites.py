import requests
from urllib.parse import quote_plus
from math import radians, cos, sin, sqrt
import json

start_address = ""

api_key = "AIzaSyAxRbysMSFHt8_Dg8E8y9-8WxUP_GrS7TU"

def get_coordinates(address):
    encoded_address = quote_plus(address)
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={encoded_address}&key={api_key}"
    response = requests.get(url)
    if response.ok:
        results = response.json().get("results", [])
        if results:
            location = results[0]["geometry"]["location"]
            return (location["lat"], location["lng"])
    return None

def euclidean_distance(coord1, coord2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1 = map(radians, coord1)
    lat2, lon2 = map(radians, coord2)

    # Haversine formula to calculate the distance
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * sqrt(a)
    r = 6371  # Radius of the Earth in kilometers
    return c * r * 1000  # Distance in meters

def get_famous_landmarks(city, radius=10000):
    query = f"landmarks in {city}"
    coordinates = get_coordinates(city)
    if coordinates:
        lat, lng = coordinates
        location = f"{lat},{lng}"
        encoded_query = quote_plus(query)
        url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={encoded_query}&location={location}&radius={radius}&key={api_key}"
        response = requests.get(url)
        landmarks = []
        while response.ok:
            results = response.json().get("results", [])
            landmarks.extend(results)
            next_page_token = response.json().get("next_page_token")
            if next_page_token:
                url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?pagetoken={next_page_token}&key={api_key}"
                response = requests.get(url)
            else:
                break
        return landmarks[:20]
    return []

def build_graph(start_coordinates, landmarks):
    average_pace = 1.4  # Average walking pace in meters per second
    graph = {}
    for i, landmark in enumerate(landmarks, start=1):
        graph[i] = []
        for j, other_landmark in enumerate(landmarks, start=1):
            if i != j:
                distance = euclidean_distance(
                    (landmark["geometry"]["location"]["lat"], landmark["geometry"]["location"]["lng"]),
                    (other_landmark["geometry"]["location"]["lat"], other_landmark["geometry"]["location"]["lng"])
                )
                walking_time_minutes = round(distance / average_pace / 60)
                graph[i].append((j, walking_time_minutes))
        # Add distance from landmark to starting point
        distance_to_start = euclidean_distance(
            (landmark["geometry"]["location"]["lat"], landmark["geometry"]["location"]["lng"]),
            start_coordinates
        )
        walking_time_to_start = round(distance_to_start / average_pace / 60)
        graph[i].append((0, walking_time_to_start))
    # Add the starting address as vertex 0
    graph[0] = []
    for i, landmark in enumerate(landmarks, start=1):
        distance = euclidean_distance(
            start_coordinates,
            (landmark["geometry"]["location"]["lat"], landmark["geometry"]["location"]["lng"])
        )
        walking_time_minutes = round(distance / average_pace / 60)
        graph[0].append((i, walking_time_minutes))
    return graph

def main(start_address, city):
    start_coordinates = get_coordinates(start_address)
    landmarks = get_famous_landmarks(city)
    graph = build_graph(start_coordinates, landmarks)

    with open("graph.json", 'w') as f:
        json.dump({'graph': graph, 'landmarks': landmarks}, f)
