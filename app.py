import streamlit as st
import pickle
import numpy as np
import os

# Page configuration
st.set_page_config(
    page_title="IPL Score Predictor",
    page_icon="🏏",
    layout="centered"
)

# Load the model safely
filename = "Batting-score-LassoReg-model.pkl"

if os.path.exists(filename):
    with open(filename, "rb") as f:
        regressor = pickle.load(f)
else:
    st.error(f"❌ Model file '{filename}' not found! Please ensure it's in the same folder as this script.")
    st.stop()

st.title("🏏 IPL Score Predictor")
st.markdown("---")

# Data options (ensure these match your model's training order!)
teams = [
    "Chennai Super Kings", "Delhi Daredevils", "Kings XI Punjab",
    "Kolkata Knight Riders", "Mumbai Indians", "Rajasthan Royals",
    "Royal Challengers Bangalore", "Sunrisers Hyderabad"
]

venues = [
    "M Chinnaswamy Stadium", "Eden Gardens", "Feroz Shah Kotla",
    "MA Chidambaram Stadium, Chepauk",
    "Punjab Cricket Association Stadium, Mohali",
    "Wankhede Stadium", "Sawai Mansingh Stadium",
    "Rajiv Gandhi International Stadium, Uppal"
]

# Layout for inputs
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Batting Team", sorted(teams))
    bowling_team = st.selectbox("Bowling Team", sorted(teams))
    venue = st.selectbox("Venue", sorted(venues))

with col2:
    runs = st.number_input("Current Score", min_value=0, max_value=350, value=80)
    wickets = st.number_input("Wickets Fallen", min_value=0, max_value=10, value=3)
    overs_whole = st.number_input("Overs Completed", 5, 20, 10)
    overs_balls = st.number_input("Balls in current Over", 0, 5, 0)

runs_in_prev_5 = st.number_input("Runs in Last 5 Overs", 0, 120, 40)
wickets_in_prev_5 = st.number_input("Wickets in Last 5 Overs", 0, 10, 2)

if st.button("Predict Score"):
    # Preprocessing logic to match model input
    temp_array = []

    # One-hot encoding for teams and venue
    temp_array += [1 if batting_team == team else 0 for team in teams]
    temp_array += [1 if bowling_team == team else 0 for team in teams]
    temp_array += [1 if venue == v else 0 for v in venues]

    # Feature engineering: Overs
    overs = overs_whole + (overs_balls / 6)
    temp_array += [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]

    # Convert to array and predict
    data = np.array([temp_array])
    prediction = int(regressor.predict(data)[0])

    # Display results
    st.success(f"### 🏏 Predicted Final Score: {prediction-10} to {prediction+5}")
    st.info("Note: Predictions are based on historical Lasso Regression data.")