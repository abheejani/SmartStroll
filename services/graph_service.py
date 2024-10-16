from math import radians, cos, sin, sqrt

def euclidean_distance(coord1, coord2):
    lat1, lon1 = map(radians, coord1)
    lat2, lon2 = map(radians, coord2)
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return 2 * sqrt(a) * 6371 * 1000  # Distance in meters

def build_graph(start_coordinates, landmarks):
    """
    Build a graph where the landmarks are nodes, and the edges represent distances between them.
    If the start_coordinates are not available, omit them from the graph.
    """
    average_pace = 1.4  # meters/second
    graph = {i: [] for i in range(len(landmarks) + (1 if start_coordinates else 0))}  # +1 for the start node (vertex 0), if available

    # Create edges between landmarks
    for i, landmark in enumerate(landmarks, start=1):
        for j, other_landmark in enumerate(landmarks, start=1):
            if i != j:
                distance = euclidean_distance(
                    (landmark["geometry"]["location"]["lat"], landmark["geometry"]["location"]["lng"]),
                    (other_landmark["geometry"]["location"]["lat"], other_landmark["geometry"]["location"]["lng"]),
                )
                graph[i].append((j, round(distance / average_pace / 60)))

        # If start_coordinates are available, add distance from the landmark to the starting point
        if start_coordinates:
            distance_to_start = euclidean_distance(
                (landmark["geometry"]["location"]["lat"], landmark["geometry"]["location"]["lng"]),
                start_coordinates,
            )
            graph[i].append((0, round(distance_to_start / average_pace / 60)))  # Landmark to start

    # Add edges from the start point to all landmarks, if start_coordinates are available
    if start_coordinates:
        for i, landmark in enumerate(landmarks, start=1):
            distance = euclidean_distance(
                start_coordinates,
                (landmark["geometry"]["location"]["lat"], landmark["geometry"]["location"]["lng"]),
            )
            graph[0].append((i, round(distance / average_pace / 60)))  # Start to landmarks

    return graph