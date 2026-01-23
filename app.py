import streamlit as st
import pickle
import numpy as np

st.set_page_config(
    page_title="IPL Score Predictor",
    page_icon="🏏",
    layout="centered"
)

filename = "Batting-score-LassoReg-model.pkl"
with open(filename, "rb") as f:
    regressor = pickle.load(f)

st.title("🏏 IPL Score Predictor")
st.write("Predict the final IPL score using Machine Learning")

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

batting_team = st.selectbox("Batting Team", teams)
bowling_team = st.selectbox("Bowling Team", teams)
venue = st.selectbox("Venue", venues)

col1, col2 = st.columns(2)

with col1:
    overs_whole = st.number_input("Overs Completed", 5, 20, 10)
with col2:
    overs_balls = st.number_input("Balls in Over", 0, 5, 0)

runs = st.number_input("Current Score", 0, 300, 80)
wickets = st.number_input("Wickets Fallen", 0, 10, 3)
runs_in_prev_5 = st.number_input("Runs in Last 5 Overs", 0, 100, 40)
wickets_in_prev_5 = st.number_input("Wickets in Last 5 Overs", 0, 10, 2)

if st.button("Predict Score"):
    temp_array = []

    temp_array += [1 if batting_team == team else 0 for team in teams]
    temp_array += [1 if bowling_team == team else 0 for team in teams]
    temp_array += [1 if venue == v else 0 for v in venues]

    overs = overs_whole + overs_balls / 6

    temp_array += [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]

    data = np.array([temp_array])

    prediction = int(regressor.predict(data)[0])

    st.success(f"🏏 Predicted Score Range: {prediction-10} to {prediction+5}")
