## **SmartStroll 🗺️ – Explore Smarter, Travel Better**  

Welcome to **SmartStroll**, your personalized travel companion! 🚶‍♂️✨ This application helps you discover the best routes between famous landmarks within a city, optimizing your travel experience based on **time constraints** and walking distances. Whether you're visiting museums, parks, or monuments, **SmartStroll** ensures you make the most of your time!

---

## **Features 🎉**  

- **Optimized Travel Routes** 🛤️  
  Find the best walking path through popular landmarks in a city using the **Dijkstra algorithm**.  

- **Flexible Trip Planning** ⏰  
  Enter a **maximum walking time** and get the best route that fits your schedule.  

- **Famous Landmarks** 🌍  
  Automatically fetch landmarks for your desired city using the **Google Places API**.

- **Easy-to-Use Interface** 💻  
  A simple web form allows you to enter your starting location, city, and travel capacity.  

---

## **How It Works 🔧**  

1. **Enter Start Address and City**  
   Provide your **starting point** and the **city** you want to explore.  

2. **Set Maximum Walking Time**  
   Set how much time you're willing to walk (in minutes), and we'll do the rest!  

3. **Optimized Route**  
   SmartStroll runs **Dijkstra’s algorithm** to find the best path through the city's landmarks that fits your time constraint.  

4. **Enjoy Your Adventure!**  
   A list of landmarks is displayed in the optimized order – just follow along and explore! 🎒

---

## **Getting Started 🚀**

Here’s how you can run **SmartStroll** on your local machine:

### **Prerequisites 📋**

1. **Python 3.x** installed on your machine.  
2. **Google Places API Key**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com).
   - Create a project and enable the **Places API** and **Geocoding API**.
   - Generate an **API key** and restrict it to specific APIs and IPs if needed.

---

### **Installation Steps ⚙️**

1. **Clone the Repository**  
   Open your terminal and run:
   ```bash
   git clone <repository_url>
   cd SmartStroll
   ```

2. **Create a Virtual Environment (Optional, Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**  
   Install the required Python packages from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Your API Key**  
   Create a **`.env`** file in the root directory and add your Google API key:
   ```
   GOOGLE_API_KEY=your-google-api-key-here
   ```

5. **Run the Application**  
   Launch the Flask app with:
   ```bash
   python app.py
   ```

6. **Open the App in Your Browser**  
   Once the app is running, go to:
   ```
   http://127.0.0.1:5000
   ```

---

### **Project Structure 🗂️**

```
SmartStroll/
│
├── app.py                         # Flask app entry point
├── templates/                     # HTML templates for the web interface
│   └── index.html                 # Main webpage for user interaction
├── services/                      # Service logic for the app
│   ├── site_service.py            # Fetches landmarks and coordinates via Google Places API
│   ├── graph_service.py           # Builds in-memory graph of landmarks
│   └── optimization_service.py    # Dijkstra algorithm to optimize the route
├── config/                        # Configuration management
│   └── api_config.py              # Loads API key from environment variables
├── .env                           # Stores your API key securely (not committed to Git)
├── requirements.txt               # List of required Python packages
└── README.md                      # Documentation (you are here!)
```

---

### **How to Use 🛠️**

1. **Open the Web App** in your browser (`http://127.0.0.1:5000`).  
2. **Enter**:
   - **Starting Address:** Where you’ll begin your journey.
   - **City:** The city you want to explore.
   - **Walking Time:** How much time you’re willing to walk.  
3. **Click Optimize Route** to see the best path through the city’s landmarks!  

---

### **Technologies Used 🛠️**

- **Python 3**: Core backend logic  
- **Flask**: Web framework  
- **Google Places API & Geocoding API**: To fetch landmarks and coordinates  
- **Dijkstra Algorithm**: For path optimization  

---

### **Possible Future Improvements 🚀**

- **Interactive Maps Integration:** Add a Google Maps view to visualize the optimized path.
- **User Authentication:** Save user routes and itineraries for future trips.
- **Multiple Transport Modes:** Include bike routes, public transport, or driving options.
- **Weather Integration:** Suggest routes based on the weather conditions.

---

### **Security Notes 🔒**

- **API Key Management:** Your Google API key is stored securely in the **`.env`** file.  
  Ensure that this file is added to **`.gitignore`** to prevent it from being pushed to version control.  
- **API Key Restrictions:** Restrict the API key in the Google Cloud Console to only the **required APIs** and **IP addresses**.

---

### **Contributing 👥**

We welcome contributions! If you’d like to improve **SmartStroll**, follow these steps:

1. Fork the repository.
2. Create a new feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request.

---

### **Issues and Feedback 📝**

If you encounter any bugs or have suggestions for improvement, please **open an issue** in the repository or send a pull request.

---

### **License 📄**

This project is licensed under the **MIT License** – see the `LICENSE` file for details.

---

### **Enjoy Your Adventure with SmartStroll! 🏞️**

Get out there and explore the world smarter, one stroll at a time! 🌍✨