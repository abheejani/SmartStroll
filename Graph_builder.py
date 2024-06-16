from math import radians, cos, sin, sqrt
import GetSites

def euclidean_distance(coord1, coord2):
    lat1, lon1 = map(radians, coord1)
    lat2, lon2 = map(radians, coord2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * sqrt(a)
    r = 6371  # Radius of the Earth in kilometers
    return c * r * 1000  # Distance in meters

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