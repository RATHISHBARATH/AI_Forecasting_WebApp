# AI_Forecasting_WebApp

# 🔮 AI-Based Sales Forecasting Web App

This is a full-stack, AI-powered forecasting platform that helps businesses analyze historical data and predict future trends using powerful ML & DL models like Prophet and LSTM.

## 🚀 Features

- 🔐 User Authentication (Signup/Login)
- 📁 Upload CSV files for forecasting
- 📊 Select between Prophet & LSTM models
- 📈 Interactive Forecast Visualizations (Plotly, Matplotlib)
- 🧠 Automated Preprocessing, Cleaning & Scaling
- 🗃 MySQL Integration for user and forecast data
- 🎥 Video Demo Available

## 🛠 Tech Stack

**Frontend**: HTML, CSS, JS, Jinja (Flask)  
**Backend**: Python, Flask, MySQL  
**AI Models**: Prophet, LSTM (Keras)  
**Visualization**: Plotly, Matplotlib, Seaborn  
**Others**: SQLAlchemy, Pandas, NumPy, Scikit-Learn, Docker-ready

## 📦 Setup Instructions

```bash
git clone https://github.com/yourusername/forecasting-app
cd forecasting-app

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # (or venv\Scripts\activate on Windows)

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py
