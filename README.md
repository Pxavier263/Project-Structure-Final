# **Weather Forecast Prediction Application**

**Description**

This project is a cutting-edge, interactive web application designed to predict weather variables for a specified time frame using the power of machine learning. It seamlessly integrates Streamlit, FastAPI, and a built-in machine learning model to provide users with accurate and intuitive weather forecasts.

# **Key Features**

1. Integrated Machine Learning
   Incorporates a trained weather prediction model directly within the project, eliminating the reliance on external resources or APIs.
2. Streamlined Data Flow
   Utilizes FastAPI as a RESTful API framework to manage seamless communication between the frontend and backend.
3. User-Friendly Interface
   Powered by Streamlit, the app offers a clean and intuitive interface, allowing users to input weather variables and specify a forecasting time frame effortlessly.
4. Clear and Informative VisualizationsGenerates dynamic and interactive visualizations of weather data over time, ensuring users can easily interpret forecast trends.

# **Getting Started**

**Prerequisites**

To successfully run this application, ensure the following:

* Basic understanding of Python programming.
* Familiarity with Streamlit and FastAPI concepts.

**Installation**

1. Clone the Repository
   Clone the project repository to your local machine using:

   ```
   git clone https://github.com/Pxavier263/Project-Structure-Final.git
   ```
2. Navigate to the Project Directory

   ```
   cd weather-forecast-application
   ```
3. Set Up a Virtual Environment (Optional but Recommended)
   Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate       # On MacOS/Linux
   venv\Scripts\activate  
   ```

       # On Windows
4. Install Dependencies
   Install all necessary packages from the `requirements.txt` file:

   ```
   pip install -r requirements.txt
   ```

**Run the Application**

1. Start the Backend API
   Launch the FastAPI backend:

   ```
   python backend/main.py
   ```
2. Start the Frontend Application
   Run the Streamlit app:

   ```
   streamlit run frontend/main.py
   ```

## **Application Structure**

```

├── backend/
│   ├── main.py                # FastAPI backend setup
│   ├── model/                 # Contains the weather prediction ML model
│   └── utils/                 # Utility scripts for data processing and API handling
├── frontend/
│   ├── main.py                # Streamlit main file for app navigation
│   ├── pages/
│       ├── homepage.py        # Homepage layout and content
│       ├── forecast.py        # Forecasting page with user inputs and visualizations
├── requirements.txt           # List of dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore file
```

## **How It Works**

1. User Input

   - Users provide weather variables (e.g., temperature, humidity) and a time frame for forecasting.
2. Data Processing

   - Input is sent to the FastAPI backend, where the pre-trained ML model processes the data and generates predictions.
3. Visualization

   - Predictions are displayed via Streamlit with interactive plots, showing trends over the selected time frame.

## **Contributing**

Contributions are welcome! If you have suggestions for improvement, feel free to:

* Fork the repository.
* Create a feature branch (`git checkout -b feature/AmazingFeature`).
* Commit your changes (`git commit -m 'Add some AmazingFeature'`).
* Push to the branch (`git push origin feature/AmazingFeature`).
* Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## **Contact**

For questions, suggestions, or support, please contact:

**Charles Ogu**
Email: p[xavier.corp@gmail.com]()
Linkedin: [https://www.linkedin.com/in/ogucharles/]()

Enjoy predicting the weather with precision and ease! 🌤️
