# ==============================
# IPL Score Predictor - Streamlit
# ==============================

import streamlit as st
import pickle
import numpy as np

# Page config
st.set_page_config(
    page_title="IPL Score Predictor",
    page_icon="🏏",
    layout="centered"
)

# Load model
filename = "Batting-score-LassoReg-model.pkl"
with open(filename, "rb") as f:
    regressor = pickle.load(f)

# Title
st.title("🏏 IPL Score Predictor")
st.write("Predict the **final score** of an IPL match using Machine Learning")

st.divider()

# ------------------------------
# Input Section
# ------------------------------

teams = [
    "Chennai Super Kings",
    "Delhi Daredevils",
    "Kings XI Punjab",
    "Kolkata Knight Riders",
    "Mumbai Indians",
    "Rajasthan Royals",
    "Royal Challengers Bangalore",
    "Sunrisers Hyderabad"
]

venues = [
    "M Chinnaswamy Stadium",
    "Eden Gardens",
    "Feroz Shah Kotla",
    "MA Chidambaram Stadium, Chepauk",
    "Punjab Cricket Association Stadium, Mohali",
    "Wankhede Stadium",
    "Sawai Mansingh Stadium",
    "Rajiv Gandhi International Stadium, Uppal"
]

batting_team = st.selectbox("Batting Team", teams)
bowling_team = st.selectbox("Bowling Team", teams)
venue = st.selectbox("Venue", venues)

st.divider()

col1, col2 = st.columns(2)

with col1:
    overs_whole = st.number_input("Overs Completed", min_value=5, max_value=20, value=10)
with col2:
    overs_balls = st.number_input("Balls in Current Over", min_value=0, max_value=5, value=0)

runs = st.number_input("Current Score", min_value=0, value=80)
wickets = st.number_input("Wickets Fallen", min_value=0, max_value=10, value=3)
runs_in_prev_5 = st.number_input("Runs in Last 5 Overs", min_value=0, value=40)
wickets_in_prev_5 = st.number_input("Wickets in Last 5 Overs", min_value=0, max_value=10, value=2)

# ------------------------------
# Prediction
# ------------------------------

if st.button("Predict Score"):
    temp_array = []

    # Batting team one-hot encoding
    temp_array += [1 if batting_team == team else 0 for team in teams]

    # Bowling team one-hot encoding
    temp_array += [1 if bowling_team == team else 0 for team in teams]

    # Venue one-hot encoding
    temp_array += [1 if venue == v else 0 for v in venues]

    # Overs calculation
    overs = overs_whole + overs_balls / 6

    # Numerical features
    temp_array += [
        overs,
        runs,
        wickets,
        runs_in_prev_5,
        wickets_in_prev_5
    ]

    # Convert to numpy array
    data = np.array([temp_array])

    # Prediction
    prediction = int(regressor.predict(data)[0])

    st.success(
        f"🏏 **Predicted Final Score Range:** {prediction - 10}  to  {prediction + 5}"
    )
