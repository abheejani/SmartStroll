SmartStroll
SmartStroll is an application that optimizes your walking routes based on your starting address and desired walking distance. By utilizing a custom graph-building algorithm and the Dijkstra's algorithm, SmartStroll provides the most efficient and enjoyable walking routes, allowing you to explore more landmarks within your preferred walking capacity.

Features
Optimized Walking Routes: Generates the most efficient route based on your starting address and walking distance.
Landmark Exploration: Includes notable landmarks in your walking route, maximizing the number of landmarks visited within your walking capacity.
Custom Graph Building: Uses Euclidean distance calculations to create a graph of landmarks and their distances from each other and the starting point.
Installation
To run SmartStroll locally, follow these steps:

Clone the repository:

sh
Copy code
git clone https://github.com/abheejani/SmartStroll.git
cd SmartStroll
Install dependencies:

sh
Copy code
pip install -r requirements.txt
Set up environment variables:
Create a .env file in the root directory and add your environment variables:

makefile
Copy code
START_ADDRESS="your_starting_address"
CITY="your_city"
Run the application:

sh
Copy code
python main.py
Usage
Set Preferences: Define your starting address and walking distance.
Generate Route: The application will generate the most optimized route for your walk, including notable landmarks.
Explore: Follow the suggested route to explore the landmarks efficiently.
