# services/optimization_service.py

import heapq

def dijkstra_max_vertices_with_capacity(graph, start, capacity):
    """Optimize the path within the given capacity using Dijkstra's algorithm."""
    priority_queue = [(1, 0, start, [start])]
    best_path = []
    visited = set()

    while priority_queue:
        num_vertices, current_distance, current_node, current_path = heapq.heappop(priority_queue)
        num_vertices = -num_vertices

        if len(current_path) > len(best_path):
            best_path = current_path

        for neighbor, weight in graph.get(current_node, []):
            if neighbor not in current_path:
                new_distance = current_distance + weight
                if new_distance <= capacity:
                    new_path = current_path + [neighbor]
                    state = (neighbor, new_distance)

                    if state not in visited:
                        visited.add(state)
                        heapq.heappush(priority_queue, (-num_vertices - 1, new_distance, neighbor, new_path))

    return best_path