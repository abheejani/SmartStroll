# app.py

from flask import Flask, render_template, request

from services.site_service import get_coordinates, get_famous_landmarks
from services.graph_service import build_graph
from services.optimization_service import dijkstra_max_vertices_with_capacity

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
        path = dijkstra_max_vertices_with_capacity(graph, start=0, capacity=capacity)

        # Convert the path indices to landmark names for display
        path_names = [landmarks[node - 1]['name'] for node in path if node > 0]

        # Render the result with the optimized path
        return render_template('index.html', path=path_names)

    return render_template('index.html', path=[])

if __name__ == '__main__':
    app.run(debug=True)
