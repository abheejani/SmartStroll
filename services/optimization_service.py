import heapq

def dijkstra_max_vertices_with_capacity(graph, start, capacity):
    priority_queue = [(1, 0, start, [start])]
    best_path = [start]
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

def greedy_refine_path(graph, best_path):
    """
    Greedy approach to refine the path by visiting the nearest unvisited node at each step.
    """
    refined_path = [best_path[0]]  # Start with the first node
    unvisited_nodes = set(best_path[1:])  # All other nodes that need to be visited

    current_node = best_path[0]

    while unvisited_nodes:
        # Find the nearest neighbor that hasn't been visited yet
        nearest_neighbor = None
        min_distance = float('inf')

        for neighbor, weight in graph.get(current_node, []):
            if neighbor in unvisited_nodes and weight < min_distance:
                nearest_neighbor = neighbor
                min_distance = weight

        # Move to the nearest unvisited neighbor
        if nearest_neighbor is not None:
            refined_path.append(nearest_neighbor)
            unvisited_nodes.remove(nearest_neighbor)
            current_node = nearest_neighbor
        else:
            # If no more unvisited neighbors are found, exit (shouldn't happen if all nodes are connected)
            break

    return refined_path
