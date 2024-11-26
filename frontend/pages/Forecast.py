import streamlit as st
import requests

URL = "https://weather-prediction-07g1.onrender.com"


def get_prediction(weather_variable, days):
    url = f"{URL}/predict"
    payload = {"weather_variable": weather_variable, "days": days}
    response = requests.post(url, data=payload)
    return response.json()


st.title("Forecast")
weather_variable = st.text_input("Weather Variable","")
days = st.number_input("Days", min_value=1, max_value=365, value=7)

if st.button("Get Prediction"):
    if weather_variable and days:
        prediction = get_prediction(weather_variable, days)
        for key, value in prediction["forecast"].items():
            st.write(key, "-", f"{value:.2f}")
    else:
        st.error("Please enter weather variable and days")
    
