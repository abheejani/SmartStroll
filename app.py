from flask import Flask, render_template, request
from config.api_config import API_KEY
from services.site_service import get_coordinates, get_famous_landmarks
from services.graph_service import build_graph
from services.optimization_service import dijkstra_max_vertices_with_capacity, greedy_refine_path

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from the form
        start_address = request.form.get('start_address')
        city = request.form.get('city')
        capacity = int(request.form.get('capacity'))

        # Step 1: Fetch coordinates and landmarks (from site_service)
        start_coordinates = get_coordinates(start_address)
        landmarks = get_famous_landmarks(city)

        # Step 2: Build the graph in memory (from graph_service)
        graph = build_graph(start_coordinates, landmarks)

        # Step 3: Optimize the path directly from the graph (from optimization_service)
        best_path = dijkstra_max_vertices_with_capacity(graph, start=0, capacity=capacity)

        # Step 4: Greedy refinement of the best path
        refined_path = greedy_refine_path(graph, best_path)

        # Step 5: Prepare the path names (place names)
        path_names = [start_address] + [landmarks[node - 1]['name'] for node in refined_path if node > 0]

        # Step 6: Prepare the path coordinates (latitude and longitude)
        path_coords = [{"lat": start_coordinates[0], "lng": start_coordinates[1]}]
        path_coords += [{"lat": landmarks[node - 1]['geometry']['location']['lat'],
                         "lng": landmarks[node - 1]['geometry']['location']['lng']} 
                         for node in refined_path if node > 0]

        # Step 7: Pass form data, path, and API key to the template
        return render_template('index.html', 
                               start_address=start_address, 
                               city=city, 
                               capacity=capacity, 
                               path=path_names, 
                               path_coords=path_coords, 
                               api_key=API_KEY)

    # On GET request, render the form without pre-filled data
    return render_template('index.html', 
                           start_address='', 
                           city='', 
                           capacity='', 
                           path=[], 
                           path_coords=[],
                           api_key=API_KEY)

if __name__ == '__main__':
    app.run(debug=True)
