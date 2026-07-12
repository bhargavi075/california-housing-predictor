import streamlit as st
import numpy as np
import pickle

# Load the saved model
with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("California House Price Predictor")
st.write("Input housing parameters below to predict the median house value.")

# Create input fields for the 8 features
med_inc = st.number_input("Median Income (in $10,000s)", value=3.5)
house_age = st.number_input("Median House Age", value=28.0)
ave_rooms = st.number_input("Average Rooms per Dwelling", value=5.0)
ave_bedrms = st.number_input("Average Bedrooms per Dwelling", value=1.0)
population = st.number_input("Block Population", value=1400.0)
ave_occup = st.number_input("Average House Occupancy", value=3.0)
latitude = st.number_input("Block Latitude", value=35.6)
longitude = st.number_input("Block Longitude", value=-119.5)

if st.button("Predict Price"):
    features = np.array([[med_inc, house_age, ave_rooms, ave_bedrms, population, ave_occup, latitude, longitude]])
    prediction = model.predict(features)[0]
    predicted_val = max(0, prediction) * 100000
    st.success(f"Predicted Median House Value: ${predicted_val:,.2f}")
