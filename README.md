Smart Stroll

Smart Stroll is a web application designed to help users optimize their walking routes to visit multiple tourist sites within a given time limit. The application allows users to input their start address, city, and maximum walking time, and it returns an optimized path of tourist sites to visit. The optimization is achieved using a modified Dijkstra's algorithm, which creates a graph of landmarks and calculates the best path within the specified walking time and a set vertex capacity.

To set up the project, ensure you have Python installed. Create a virtual environment and install the required dependencies listed in the `requirements.txt` file. Once the environment is set up, you can start the Flask application by running the command `python -m flask run`. This will launch the web server, allowing you to access the application in your browser.

The application uses a JSON file to store graph data, which includes the connections between various landmarks and their distances. The `dijkstra_max_vertices_with_capacity` function calculates the optimal path by considering the walking time and a vertex capacity limit. The graph is built using the `build_graph` function, which calculates the distances between landmarks based on their geographical coordinates.

To run the application, navigate to the project directory, set up your environment, and run the Flask server. Input your desired start address, city, and maximum walking time into the form, and the application will display the optimized path of tourist sites for you to visit.
