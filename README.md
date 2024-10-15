## **SmartStroll 🗺️ – Explore Smarter, Travel Better**  

Welcome to **SmartStroll**, your personalized travel companion! 🚶‍♂️✨ This application helps you discover the best routes between famous landmarks within a city, optimizing your travel experience based on **time constraints** and walking distances. Whether you're visiting museums, parks, or monuments, **SmartStroll** ensures you make the most of your time!


## **How to Use**  

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

### **Issues and Feedback 📝**

If you encounter any bugs or have suggestions for improvement, please **open an issue** in the repository or send a pull request.

Get out there and explore the world smarter, one stroll at a time! 🌍✨