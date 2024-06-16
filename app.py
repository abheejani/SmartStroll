from flask import Flask, render_template, request
import OptimizeRoute
import GetSites

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start_address = request.form.get('start_address')
        city = request.form.get('city')
        capacity = int(request.form.get('capacity'))  # Convert capacity to integer

        # Set the start address and city in GetSites
        GetSites.start_address = start_address
        GetSites.city = city

        try:
            # Run the tourist sites optimization
            path = OptimizeRoute.run_tourist_sites(capacity)
        except Exception as e:
            path = []
            print(f"Error: {e}")  # Log the error

        return render_template('index.html', path=path)
    return render_template('index.html', path=[])

if __name__ == '__main__':
    app.run(debug=True)
