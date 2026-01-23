# IPL Score Predictor 🏏 | Live Cricket Score Forecasting Web App

A beautiful **Streamlit web application** that predicts the **final batting team score** in IPL matches using historical data and a trained **Lasso Regression model**.
## ✨ Live Demo

→ **[IPL Score Predictor – Try it now!](https://endtoendprojects-qndjqbqxa2phppnyfv8elc.streamlit.app/)**  
(Deployed on Streamlit Community Cloud)

## Features

- Predict final score based on:
  - Batting team
  - Bowling team
  - Venue
  - Current runs & wickets
  - Overs completed + balls in current over
  - Runs & wickets in last 5 overs
- Clean, mobile-friendly UI with emojis & real-time prediction
- Input validation & helpful error messages
- Model accuracy improved with feature engineering (overs, recent performance)

## Tech Stack

- **Frontend**: Streamlit
- **Model**: Lasso Regression (trained on historical IPL data)
- **Libraries**: pandas, numpy, scikit-learn, pickle, joblib
- **Deployment**: Streamlit Community Cloud (free tier)
