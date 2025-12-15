# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:52:57 2024
@author: kavin
"""

import streamlit as st
import base64
import pandas as pd
from joblib import load

# ---------------- LOAD MODEL ----------------
model = load("house_price_model.joblib")

def run_prediction(input_data):
    return model.predict(input_data)

# ---------------- SESSION STATE INIT ----------------
defaults = {
    "sqft": 0.0,
    "beds": 0,
    "baths": 0,
    "year": None,
    "lot": 0.0,
    "garage": 0.0,
    "neigh": 5
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ---------------- BACKGROUND IMAGE ----------------
file_path = "static/bg1.jpg"
with open(file_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: 100% 100%;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    label {{
        font-size: 20px !important;
        color: #00008B !important;
        background-color: rgba(255,255,255,0.6);
        padding: 5px 10px;
        border-radius: 5px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- APP CONTENT ----------------
st.title("House Price Prediction App")
st.write("Enter house details to predict the price.")

# ---------------- INPUTS (STABLE) ----------------
st.number_input(
    "Enter square footage:",
    min_value=0.0,
    step=1.0,
    format="%.0f",
    key="sqft"
)

st.number_input(
    "Enter number of bedrooms:",
    min_value=0,
    step=1,
    format="%d",
    key="beds"
)

st.number_input(
    "Enter number of bathrooms:",
    min_value=0,
    step=1,
    format="%d",
    key="baths"
)

st.number_input(
    "Enter the year built:",
    min_value=1800,
    max_value=2024,
    step=1,
    format="%d",
    key="year"
)

st.number_input(
    "Enter lot size (in acres):",
    min_value=0.0,
    step=0.1,
    format="%.2f",
    key="lot"
)

st.number_input(
    "Enter garage size (in square feet):",
    min_value=0.0,
    step=1.0,
    format="%.0f",
    key="garage"
)

st.slider(
    "Neighborhood quality (1-10):",
    min_value=1,
    max_value=10,
    key="neigh"
)

# ---------------- PREDICTION ----------------
if st.button("Predict Price"):
    try:
        if st.session_state.year is None:
            st.warning("Please enter the year built.")
            st.stop()

        new_data_df = pd.DataFrame({
            'Square_Footage': [st.session_state.sqft],
            'Num_Bedrooms': [st.session_state.beds],
            'Num_Bathrooms': [st.session_state.baths],
            'Year_Built': [st.session_state.year],
            'Lot_Size': [st.session_state.lot],
            'Garage_Size': [st.session_state.garage],
            'Neighborhood_Quality': [st.session_state.neigh]
        }).astype(float)

        result = run_prediction(new_data_df)
        price = f"$ {result[0]:,.2f}"

        st.markdown(
            f"""
            <div style="
                background-color: white;
                padding: 20px;
                border-radius: 10px;
                border: 2px solid #ccc;
                width: fit-content;
                margin: auto;
                text-align: center;
            ">
                <h3 style="color:#00008B;">Predicted House Price</h3>
                <p style="font-size:24px;font-weight:bold;color:#0A9548;">
                    {price}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"An error occurred: {e}")

