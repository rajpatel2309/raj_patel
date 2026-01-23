# 🚗 Car Price Predictor – Used Car Valuation Web App

A fast, production-ready **Flask web application** that predicts used car prices in real time.  
Deployed on **Render.com** with **Gunicorn** for reliable serving.

## ✨ Live Demo

→ **[Car Price Predictor – Live on Render](https://olx5.onrender.com)**  

## Features

- Clean, responsive web interface (Flask + Bootstrap / plain HTML/CSS)
- Predicts used car price based on:
  - Brand / Make
  - Model
  - Year
  - Kilometers driven
  - Fuel type
  - Transmission
  - Owner type
  - Mileage / Engine / Seats (if available in your model)
- Instant prediction with clear output formatting
- Production-grade deployment using Gunicorn on Render

## Tech Stack

- **Backend**: Flask (lightweight Python web framework)
- **Server**: Gunicorn (WSGI HTTP server for production)
- **Model**: scikit-learn (e.g., Random Forest / XGBoost / Linear Regression)
- **Data handling**: pandas, numpy
- **Serialization**: joblib / pickle
- **Deployment**: Render.com (free tier)
