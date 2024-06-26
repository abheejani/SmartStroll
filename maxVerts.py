import heapq
import json
import GetSites

with open('graph.json', 'r') as f:
    data = json.load(f)
    graph = data['graph']
    landmarks = data['landmarks']

def dijkstra_max_vertices_with_capacity(graph, start, capacity, vertCapacity=20):
    priority_queue = []
    start_element = (1, 0, start, [start])
    heapq.heappush(priority_queue, start_element)
    
    best_path = []

    while priority_queue:
        num_vertices, current_distance, current_node, current_path = heapq.heappop(priority_queue)
        num_vertices = -num_vertices

        if len(current_path) > len(best_path):
            best_path = current_path

        if len(best_path) < vertCapacity:
            for neighbor, weight in graph[str(current_node)]:
                if neighbor not in current_path:
                    new_distance = current_distance + weight
                    if new_distance <= capacity:
                        new_num_vertices = num_vertices + 1
                        if new_num_vertices > vertCapacity:
                            continue
                        new_path = current_path + [neighbor]
                        new_element = (-new_num_vertices, new_distance, neighbor, new_path)
                        heapq.heappush(priority_queue, new_element)

    return best_path


def main(capacity):
    # Read the graph and landmarks from the file
    with open('graph.json', 'r') as f:
        data = json.load(f)
        graph = data['graph']
        landmarks = data['landmarks']

    start = 0  # Start from the 0th node (starting address)

    ret_path = []

    max_path = dijkstra_max_vertices_with_capacity(graph, start, capacity)
    print(f"Path with the largest number of vertices from {GetSites.start_address} within capacity {capacity}:")
    for node in max_path:
        ret_path.append(landmarks[node - 1]['name'])
        print(landmarks[node - 1]['name'])
    return ret_path

if __name__ == "__main__":
    main()
