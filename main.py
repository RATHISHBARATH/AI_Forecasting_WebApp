# Flask Framework
from flask import (
    Flask, render_template, render_template_string, request,
    redirect, url_for, session, jsonify, flash, send_file
)
from flask import Blueprint, render_template, request


from flask_cors import CORS
from flask_mysqldb import MySQL
import io
import base64
from statistics import stdev
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.cluster import KMeans
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.cluster import KMeans
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import warnings
warnings.filterwarnings("ignore")
import base64
import io
import warnings
warnings.filterwarnings("ignore")
from scipy.stats import linregress
from io import BytesIO
from sklearn.linear_model import LinearRegression
import uuid
import warnings
# Web server & security
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from waitress import serve
from flask_sqlalchemy import SQLAlchemy
from io import StringIO


# OS and System Utilities
import os
import json
import uuid
import csv
import time
import re
import threading
import datetime
from datetime import datetime
from dateutil import parser

# Data Handling & Visualization
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.offline as pyo


from flask import Flask, render_template_string, request, redirect, url_for
import pandas as pd
import pymysql
from prophet import Prophet
import matplotlib.pyplot as plt
import tkinter as tk
import logging
from tkinter import filedialog, messagebox


# Document Handling
from docx import Document

# Machine Learning & Forecasting
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from prophet import Prophet
import io
import base64
import pandas as pd
from prophet import Prophet  # Use 'from fbprophet import Prophet' if you're on the older version
from flask import render_template_string, request
import pymysql


# Deep Learning (Using tensorflow.keras to avoid import issues)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, GRU, Dropout
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.cluster import KMeans

# For warnings suppression (cleaner logs)
import warnings
warnings.filterwarnings("ignore")
# PyTorch (Optional if you are using it somewhere)
import torch
import torch.nn as nn

# Facebook Prophet for Forecasting
from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics

# Database Connectors
import pymysql
import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine, text

# Apache Spark
from pyspark.sql import SparkSession

# Custom utilities
from utils import plot_forecast
import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from prophet import Prophet
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import warnings
from sqlalchemy import create_engine, text
warnings.filterwarnings("ignore")










logging.basicConfig(level=logging.INFO)


def run_ui():
    root = tk.Tk()
    root.mainloop()

threading.Thread(target=run_ui).start()



os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

app = Flask(__name__)


CORS(app)

STATIC_FOLDER = os.path.join(os.path.dirname(__file__), 'static')
os.makedirs(STATIC_FOLDER, exist_ok=True)

# DB connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rathish123",
        database="user_mangement"
    )


import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  


app = Flask(__name__)
# Database configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Rathish123"
DB_NAME = "user_management"

app.secret_key = "7688f36cc7df301843851a58011752c4"

@app.route('/')
def home():
    home_html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DataFlowX - Enterprise Data Engineering Platform</title>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f8f9fa;
                color: #333;
            }
            header {
                background: #0a1930;
                color: white;
                padding: 1rem 2rem;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .logo {
                font-size: 1.5rem;
                font-weight: bold;
                color: #00d1b2;
            }
            nav ul {
                list-style: none;
                display: flex;
                gap: 1.5rem;
                margin: 0;
            }
            nav ul li a {
                color: white;
                text-decoration: none;
                font-weight: 500;
            }
            .cta-button {
                background: #00d1b2;
                color: white;
                padding: 0.5rem 1rem;
                border-radius: 5px;
                text-decoration: none;
            }
            .hero {
                background: #001f3f;
                color: white;
                padding: 4rem 2rem;
                text-align: center;
            }
            .section {
                padding: 3rem 2rem;
                text-align: center;
            }
            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 2rem;
                padding-top: 1.5rem;
            }
            .card {
                background: white;
                padding: 1.5rem;
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }
            footer {
                background: #0a1930;
                color: white;
                text-align: center;
                padding: 1rem;
                font-size: 0.9rem;
            }
        </style>
    </head>
    <body>
        <header>
            <div class="logo">DataFlowX</div>
            <nav>
                <ul>
                    <li><a href="/signup">Sign Up</a></li>
                    <li><a href="/login">Log In</a></li>
                    <li><a href="#features">Features</a></li>
                    <li><a href="#solutions">Solutions</a></li>
                    <li><a href="#contact" class="cta-button">Contact</a></li>
                </ul>
            </nav>
        </header>

        <section class="hero">
            <h1>Build Scalable Data Pipelines for Tomorrow</h1>
            <p>Design, orchestrate, and monitor real-time and batch data workflows with confidence.</p>
            <a href="/dashboard" class="cta-button">Get Started</a>
        </section>

        <section id="features" class="section">
            <h2>Key Platform Features</h2>
            <div class="grid">
                <div class="card">
                    <h3>🚀 Fast ETL Pipelines</h3>
                    <p>Design robust Extract-Transform-Load flows using SQL, Python, or custom nodes.</p>
                </div>
                <div class="card">
                    <h3>📡 Real-Time Streaming</h3>
                    <p>Stream data from Kafka, Kinesis, or Pub/Sub to your data warehouse with ease.</p>
                </div>
                <div class="card">
                    <h3>🧮 Data Lake & Warehouse</h3>
                    <p>Connect to Snowflake, BigQuery, Redshift, and S3-compatible lakes.</p>
                </div>
                <div class="card">
                    <h3>📊 Pipeline Monitoring</h3>
                    <p>Live dashboards with retry logic, error logging, and performance stats.</p>
                </div>
            </div>
        </section>

        <section id="solutions" class="section" style="background:#eef2f7;">
            <h2>Solutions For Every Industry</h2>
            <div class="grid">
                <div class="card">
                    <h3>🏥 Healthcare</h3>
                    <p>Real-time patient analytics and predictive insights from EMRs.</p>
                </div>
                <div class="card">
                    <h3>💰 Finance</h3>
                    <p>Transaction pipelines, fraud detection, and audit trails.</p>
                </div>
                <div class="card">
                    <h3>🛍️ E-Commerce</h3>
                    <p>Behavioral tracking, inventory analytics, and real-time pricing engines.</p>
                </div>
                <div class="card">
                    <h3>🚚 Logistics</h3>
                    <p>Supply chain data unification, delivery ETAs, and route optimizations.</p>
                </div>
            </div>
        </section>

        <section id="contact" class="section">
            <h2>Contact Us</h2>
            <p>Ready to elevate your data infrastructure? Let’s talk!</p>
            <p><strong>Email:</strong> hello@dataflowx.io</p>
        </section>

        <footer>
            <p>&copy; 2025 DataFlowX Platform. All Rights Reserved.</p>
        </footer>
    </body>
    </html>
    '''
    return render_template_string(home_html)





# Sign Up Page
signup_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Sign Up - DataFlowX</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f8f9fa;
            margin: 0;
            padding: 0;
        }
        .signup-container {
            max-width: 400px;
            margin: 100px auto;
            background: white;
            padding: 30px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
            border-radius: 8px;
        }
        .signup-container h2 {
            text-align: center;
            margin-bottom: 25px;
        }
        input[type="text"], input[type="email"], input[type="password"] {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            width: 100%;
            background-color: #0a1930;
            color: white;
            padding: 12px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .error { color: red; }
    </style>
</head>
<body>
    <div class="signup-container">
        <h2>Create Your Account</h2>
        <form method="post">
            <input type="text" name="name" placeholder="Full Name" required>
            <input type="email" name="email" placeholder="Email Address" required>
            <input type="password" name="password" placeholder="Password" required minlength="6">
            <button type="submit">Sign Up</button>
        </form>
        <p class="error">{{ error_message }}</p>
        <p>Already have an account? <a href="/login">Login</a></p>
    </div>
</body>
</html>
'''

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error_message = ''
    if request.method == 'POST':
        name = request.form.get('name').strip()
        email = request.form.get('email').strip().lower()
        password = request.form.get('password').strip()

        # Basic server-side validation
        if not name or not email or not password:
            error_message = "All fields are required."
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            error_message = "Invalid email format."
        elif len(password) < 6:
            error_message = "Password must be at least 6 characters long."
        else:
            try:
                connection = pymysql.connect(
                    host=DB_HOST,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    database=DB_NAME,
                    cursorclass=pymysql.cursors.DictCursor
                )
                cursor = connection.cursor()

                # Check if email is already registered
                cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
                if cursor.fetchone():
                    error_message = "Email already exists."
                else:
                    # Hash password
                    hashed_password = generate_password_hash(password)

                    # Insert new user
                    cursor.execute(
                        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                        (name, email, hashed_password)
                    )
                    connection.commit()

                    # Log in the user automatically
                    session['user_email'] = email
                    return redirect('/dashboard')

            except pymysql.MySQLError as e:
                print("MySQL Error:", e)
                error_message = 'Server error. Please try again later.'

            finally:
                if 'connection' in locals() and connection:
                    connection.close()

    return render_template_string(signup_html, error_message=error_message)




dashboard_html = '''
     <!DOCTYPE html>
<html lang="en">
<head>
    <title>Data Analytics Pro - Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background-color: #f4f6f8;
        }
        .sidebar {
            width: 240px;
            height: 100vh;
            position: fixed;
            background-color: #1e1e2f;
            color: #fff;
            padding: 30px 15px;
        }
        .sidebar h4 {
            margin-bottom: 30px;
            font-weight: bold;
            color: #00d1b2;
        }
        .sidebar a {
            display: block;
            color: #cfd8dc;
            padding: 12px 10px;
            margin: 10px 0;
            text-decoration: none;
            border-radius: 5px;
        }
        .sidebar a:hover {
            background-color: #2a2a3d;
            color: #fff;
        }
        .content {
            margin-left: 260px;
            padding: 40px;
        }
        .hero-section {
            background: linear-gradient(135deg, #007bff, #6610f2);
            color: white;
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 40px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        }
        .hero-section h2 {
            font-weight: 700;
            font-size: 2rem;
        }
        .card {
            border: none;
            border-radius: 20px;
            padding: 25px;
            color: white;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .bg-analytics { background: #00b894; }
        .bg-users { background: #0984e3; }
        .bg-active { background: #6c5ce7; }
        .bg-credits { background: #fdcb6e; color: black; }
        .services {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }
        .service-box {
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.05);
            text-align: center;
        }
        .service-box h5 {
            margin-top: 10px;
            font-weight: bold;
        }
        .credit-btn {
            margin-top: 15px;
            background-color: #ffeaa7;
            color: #2d3436;
            border: none;
            padding: 8px 16px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <div class="sidebar">
        <h4>📊 DataPro</h4>
        <a href="/dashboard"><i class="bi bi-house-door-fill"></i> Dashboard</a>
        <a href="/upload_data"><i class="bi bi-upload"></i> Upload Data</a>
        <a href="/forecast-history"><i class="bi bi-bar-chart-line-fill"></i> Forecasts</a>
        <a href="/logout"><i class="bi bi-box-arrow-right"></i> Logout</a>
    </div>

    <div class="content">
        <div class="hero-section">
            <h2>Welcome back, {{ user_email }} 👋</h2>
            <p>AI-driven insights to power your business decisions like Zoho, Amazon, and Microsoft.</p>
        </div>

        <div class="row mb-5">
            <div class="col-md-3 mb-3">
                <div class="card bg-analytics">
                    <h5><i class="bi bi-lightbulb-fill"></i> Analytics Created</h5>
                    <h3>{{ analytics_created }}</h3>
                </div>
            </div>
            <div class="col-md-3 mb-3">
                <div class="card bg-users">
                    <h5><i class="bi bi-people-fill"></i> Total Users</h5>
                    <h3>{{ total_users }}</h3>
                </div>
            </div>
            <div class="col-md-3 mb-3">
                <div class="card bg-active">
                    <h5><i class="bi bi-graph-up-arrow"></i> Active Users</h5>
                    <h3>{{ active_users }}</h3>
                </div>
            </div>
            <div class="col-md-3 mb-3">
                <div class="card bg-credits text-center">
                    <h5><i class="bi bi-coin"></i> Available Credits</h5>
                    <h3 id="creditCount">0</h3>
                    <button class="credit-btn" onclick="addCredits()">Add Credits</button>
                </div>
            </div>
        </div>

        <h4 class="mb-3">Our Services</h4>
        <div class="services">
            <div class="service-box">
                <div>💼</div>
                <h5>Sales Forecasting</h5>
                <p>Accurate demand predictions tailored to your industry.</p>
            </div>
            <div class="service-box">
                <div>📊</div>
                <h5>Market Insights</h5>
                <p>Comprehensive market analysis powered by AI.</p>
            </div>
            <div class="service-box">
                <div>👥</div>
                <h5>Customer Analytics</h5>
                <p>Understand your customers with advanced segmentation.</p>
            </div>
            <div class="service-box">
                <div>🤖</div>
                <h5>AI Model Development</h5>
                <p>Custom ML models designed for your business success.</p>
            </div>
        </div>
    </div>

    <script>
        let creditCount = 0;
        function addCredits() {
            creditCount += 1;
            document.getElementById("creditCount").innerText = creditCount;
        }
    </script>
</body>
</html>


 '''


### 2. **Python Backend Code:**


@app.route('/dashboard')
def dashboard():
    if 'user_email' not in session:
        return redirect('/login')

    user_email = session['user_email']

    # Initialize metrics
    total_users = 0
    active_users = 0
    total_ingested = 0
    processed_successfully = 0
    processing_failed = 0
    pending_tasks = 0
    recent_jobs = []
    servers_running = 0
    disk_usage = 0
    analytics_created = 0

    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) AS total_users FROM users")
        total_users = cursor.fetchone()['total_users']

        cursor.execute("SELECT COUNT(*) AS active_users FROM users WHERE last_login > NOW() - INTERVAL 1 WEEK")
        active_users = cursor.fetchone()['active_users']

        cursor.execute("SELECT SUM(records_ingested) AS total_ingested FROM data_jobs")
        total_ingested = cursor.fetchone()['total_ingested'] or 0

        cursor.execute("SELECT SUM(success) AS processed_successfully, SUM(fail) AS processing_failed FROM data_jobs")
        result = cursor.fetchone()
        processed_successfully = result['processed_successfully'] or 0
        processing_failed = result['processing_failed'] or 0

        cursor.execute("SELECT COUNT(*) AS pending_tasks FROM data_jobs WHERE status = 'Pending'")
        pending_tasks = cursor.fetchone()['pending_tasks']

        cursor.execute("""
            SELECT name, status, started_at,
                   TIMESTAMPDIFF(MINUTE, started_at, NOW()) AS duration
            FROM data_jobs
            ORDER BY started_at DESC LIMIT 5
        """)
        recent_jobs = cursor.fetchall()

        # NEW: Fetch analytics created
        cursor.execute("SELECT COUNT(*) AS analytics_created FROM analytics_logs")
        analytics_created = cursor.fetchone()['analytics_created']

        # Simulated stats (replace with real logic if needed)
        servers_running = 5
        disk_usage = 70

    except pymysql.MySQLError as e:
        print("DB Error:", e)

    finally:
        try:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        except:
            pass

    return render_template_string(dashboard_html,
                                  user_email=user_email,
                                  total_users=total_users,
                                  active_users=active_users,
                                  total_ingested=total_ingested,
                                  processed_successfully=processed_successfully,
                                  processing_failed=processing_failed,
                                  pending_tasks=pending_tasks,
                                  recent_jobs=recent_jobs,
                                  servers_running=servers_running,
                                  disk_usage=disk_usage,
                                  analytics_created=analytics_created)











login_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Login - DataFlowX</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f8f9fa;
            margin: 0;
            padding: 0;
        }
        .login-container {
            max-width: 400px;
            margin: 100px auto;
            background: white;
            padding: 30px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
            border-radius: 8px;
        }
        .login-container h2 {
            text-align: center;
            margin-bottom: 25px;
        }
        input[type="email"], input[type="password"] {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            width: 100%;
            background-color: #0a1930;
            color: white;
            padding: 12px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .error { color: red; }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Login to Your Account</h2>
        <form method="post">
            <input type="email" name="email" placeholder="Email Address" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
        <p class="error">{{ error_message }}</p>
        <p>Don't have an account? <a href="/signup">Sign Up</a></p>
    </div>
</body>
</html>
'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = ''
    if request.method == 'POST':
        email = request.form.get('email').strip().lower()
        password = request.form.get('password').strip()

        try:
            connection = pymysql.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME,
                cursorclass=pymysql.cursors.DictCursor
            )
            cursor = connection.cursor()

            # Check if user exists in the database
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()

            if user and check_password_hash(user['password'], password):
                # Login successful, store the user's email in the session
                session['user_email'] = email
                return redirect('/dashboard')
            else:
                error_message = 'Invalid email or password.'

        except pymysql.MySQLError as e:
            print("DB Error:", e)
            error_message = 'Server error. Please try again later.'

        finally:
            if 'connection' in locals() and connection:
                connection.close()

    return render_template_string(login_html, error_message=error_message)











app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'.csv', '.json', '.docx', '.xlsx', '.xls'}

# Make sure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# ---------- HELPER FUNCTIONS ----------

def table_exists_in_mysql(table_name, db_name='user_management'):
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='Rathish123',
            database=db_name
        )
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES LIKE %s", (table_name,))
        return cursor.fetchone() is not None
    finally:
        if 'conn' in locals():
            conn.close()

def cleanup_orphan_file(upload_folder, dataset_name):
    for ext in ['.csv', '.xlsx', '.xls', '.json', '.docx']:
        path = os.path.join(upload_folder, dataset_name + ext)
        if os.path.exists(path) and not table_exists_in_mysql(dataset_name):
            os.remove(path)

def normalize_dataset_name(filename, upload_folder):
    name, ext = os.path.splitext(filename)
    cleaned = re.sub(r'[^A-Za-z0-9\s-]', '', name)
    parts = re.split(r'[-\s]+', cleaned)
    numbers = [p for p in parts if p.isdigit()]
    words = [p for p in parts if not p.isdigit()]
    new_name = "_".join(words + numbers).lower()
    if not new_name or not new_name[0].isalpha():
        new_name = "dataset_" + new_name

    # Clean up old file if its table is gone
    cleanup_orphan_file(upload_folder, new_name)

    base_name = new_name
    counter = 1

    while True:
        file_path = os.path.join(upload_folder, f"{new_name}{ext}")
        if not os.path.exists(file_path) and not table_exists_in_mysql(new_name):
            break
        new_name = f"{base_name}_{counter}"
        counter += 1

    return new_name

def preprocess_data(df):
    return df.dropna()



# ---------- HTML FORM ----------

html_form = '''
<!DOCTYPE html>
<html>
<head>
    <title>Upload CSV / Excel / JSON</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="p-5">
    <div class="container">
        <h2 class="mb-4">Upload CSV / Excel / JSON File</h2>
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                {% for msg in messages %}
                    <div class="alert alert-info">{{ msg }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        <form method="POST" enctype="multipart/form-data">
            <div class="mb-3">
                <input type="file" name="file" class="form-control" accept=".csv,.xls,.xlsx,.json,.docx" required>
            </div>
            <button type="submit" class="btn btn-primary">Upload</button>
        </form>

        <br>
        <form method="GET" action="" onsubmit="event.preventDefault(); redirectToForecast();">
            <div class="input-group">
                <input type="text" id="forecastTable" class="form-control" placeholder="Enter uploaded table name">
                <button class="btn btn-warning" type="submit">Forecasting</button>
            </div>
        </form>
    </div>

    <script>
        function redirectToForecast() {
            var table = document.getElementById('forecastTable').value;
            if (table.trim() !== "") {
                window.location.href = '/forecast/' + table.trim();
            } else {
                alert("Please enter a table name.");
            }
        }
    </script>
</body>
</html>
'''

# ---------- ROUTES ----------

@app.route('/upload_data', methods=['GET', 'POST'])
def upload_data():
    session['uploaded'] = False

    if request.method == 'POST':
        file = request.files.get('file')
        if not file or file.filename == '':
            flash("❌ No file selected.")
            return redirect(request.url)

        original_name = file.filename
        ext = os.path.splitext(original_name)[1].lower()

        if ext not in ALLOWED_EXTENSIONS:
            flash("❌ Unsupported format.")
            return redirect(request.url)

        cleaned_name = normalize_dataset_name(original_name, app.config['UPLOAD_FOLDER'])
        new_filename = f"{cleaned_name}{ext}"
        path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
        file.save(path)

        session['uploaded'] = True
        session['last_file'] = path

        try:
            # Load file
            if ext == '.csv':
                df = pd.read_csv(path)
            elif ext == '.json':
                try:
                    df = pd.read_json(path, lines=True)
                except:
                    with open(path) as f:
                        data = json.load(f)
                    df = pd.json_normalize(data)
            elif ext in ['.xlsx', '.xls']:
                df = pd.read_excel(path)
            elif ext == '.docx':
                from docx import Document
                doc = Document(path)
                text = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
                df = pd.DataFrame([{'content': text}])
            else:
                flash("❌ Unreadable format.")
                return redirect(request.url)

            if df.empty:
                flash("⚠️ File is empty.")
                return redirect(request.url)

            df.columns = [str(col).strip()[:250] for col in df.columns]

            # Database operations
            conn = pymysql.connect(host='localhost', user='root', password='Rathish123', database='user_management')
            cursor = conn.cursor()

            # Table creation with support for massive datasets
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS uploaded_datasets (
                    id BIGINT AUTO_INCREMENT PRIMARY KEY,
                    column_name VARCHAR(255),
                    value LONGTEXT,
                    row_index BIGINT,
                    table_name VARCHAR(255),
                    INDEX idx_table_name (table_name),
                    INDEX idx_row_index (row_index)
                )
            """)

            # Prepare bulk insert data
            bulk_data = []
            for i, row in df.iterrows():
                for col in df.columns:
                    val = row[col]
                    bulk_data.append((str(col), str(val), int(i), cleaned_name))

                # Optional: Insert in chunks for large files
                if len(bulk_data) > 50000:
                    cursor.executemany("""
                        INSERT INTO uploaded_datasets (column_name, value, row_index, table_name)
                        VALUES (%s, %s, %s, %s)
                    """, bulk_data)
                    conn.commit()
                    bulk_data = []

            if bulk_data:
                cursor.executemany("""
                    INSERT INTO uploaded_datasets (column_name, value, row_index, table_name)
                    VALUES (%s, %s, %s, %s)
                """, bulk_data)

            conn.commit()
            conn.close()

            flash(f"✅ File `{original_name}` uploaded as `{new_filename}` and stored in table `{cleaned_name}`.")
        
        except Exception as e:
            flash(f"❌ Error while uploading: {str(e)}")

        return redirect(url_for('upload_data'))

    return render_template_string(html_form)







def make_columns_unique(df):
    seen = {}
    new_cols = []
    for col in df.columns:
        if col not in seen:
            seen[col] = 0
            new_cols.append(col)
        else:
            seen[col] += 1
            new_cols.append(f"{col}_{seen[col]}")
    df.columns = new_cols
    return df

def detect_numeric_columns(df, threshold=0.5):
    numeric_cols = []
    for col in df.columns:
        coerced = pd.to_numeric(df[col], errors='coerce')
        if coerced.notna().mean() >= threshold:
            df[col] = coerced
            numeric_cols.append(col)
    return numeric_cols

def is_forecastable(series, min_length=10):
    return pd.api.types.is_numeric_dtype(series) and series.dropna().shape[0] >= min_length

def detect_metadata_columns(df, numeric_columns):
    return [col for col in df.columns if col not in numeric_columns]

def create_plot(model, forecast):
    fig = model.plot(forecast)
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

def analyze_trend(forecast):
    slope = forecast['yhat'].diff().mean()
    trend = "Increasing" if slope > 0 else "Decreasing" if slope < 0 else "Stable"
    stddev = forecast['yhat'].std()
    return trend, stddev

def ai_explanation(col_name, trend, stddev):
    explanation = f"The forecast for <b>{col_name}</b> shows a <b>{trend.lower()}</b> trend with a standard deviation of <b>{stddev:.2f}</b>."
    if trend == "Increasing":
        explanation += " This indicates potential growth or improvement over time."
    elif trend == "Decreasing":
        explanation += " This suggests a possible decline in performance."
    else:
        explanation += " The values appear to be relatively stable."
    return explanation

def get_best_performer(df, target_col, label_col):
    idx = df[target_col].idxmax()
    best_label = df.loc[idx, label_col] if label_col else "Unknown"
    best_value = df.loc[idx, target_col]
    return best_label, best_value

def preprocess(df):
    df = make_columns_unique(df)
    numeric_cols = detect_numeric_columns(df)
    imputer = SimpleImputer(strategy='mean')
    df[numeric_cols] = imputer.fit_transform(df[numeric_cols])
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df, numeric_cols

def cluster_importance(df, numeric_cols, n_clusters=3):
    km = KMeans(n_clusters=n_clusters, random_state=42)
    km.fit(df[numeric_cols])
    df['cluster'] = km.labels_
    return df

def get_column_summary(df, numeric_cols, metadata_col):
    summary = ""
    for col in numeric_cols:
        try:
            top = df[[metadata_col, col]].sort_values(by=col, ascending=False).iloc[0]
            summary += f"<li>According to <b>{col}</b>, <b>{top[metadata_col]}</b> performs best with value <b>{top[col]:.2f}</b>.</li>"
        except:
            continue
    return summary

def suggest_improvement_dynamic(col_name, forecast_values, original_values):
    suggestion = ""
    try:
        trend_slope = linregress(np.arange(len(forecast_values)), forecast_values).slope
        mean_forecast = np.mean(forecast_values)
        std_dev = np.std(forecast_values)
        latest_val = forecast_values[-1]
        original_mean = np.mean(original_values)
        col = col_name.lower()

        if any(x in col for x in ["mileage", "kmpl", "mpg", "fuel economy"]):
            suggestion = "Fuel efficiency is decreasing. Enhancing engine design may boost performance." if trend_slope < 0 else "Fuel efficiency is rising. Highlight it in your marketing campaigns."
        elif any(x in col for x in ["fuel tank", "capacity"]):
            suggestion = "Increase fuel tank capacity for better long-range appeal." if latest_val < original_mean else "Current fuel tank size is optimal. Focus on comfort and range."
        elif "transmission" in col:
            if "automatic" in str(original_values).lower():
                suggestion = "Automatic variants are trending. Consider launching more automatic models."
            elif "manual" in str(original_values).lower():
                suggestion = "Manual transmissions dominate. Analyze regions where automatic can be introduced."
            else:
                suggestion = "Diversify transmission options based on market demand."
        elif any(x in col for x in ["horsepower", "hp", "power"]):
            suggestion = "Low performance detected. Introduce models with higher horsepower." if mean_forecast < original_mean else "Powerful models forecast well. Emphasize performance features."
        elif any(x in col for x in ["price", "cost", "amount", "revenue"]):
            suggestion = "Pricing is high. Consider bundle offers or price drops for competitiveness." if latest_val > original_mean + std_dev else "Competitive pricing forecasted. Promote affordability to gain traction."
        elif any(x in col for x in ["brand", "model", "product", "category"]):
            suggestion = "Forecast by brand/model shows customer preferences. Optimize inventory accordingly."
        elif any(x in col for x in ["year", "date"]):
            suggestion = "Newer models are gaining attention. Highlight innovation in upcoming releases."
        elif any(x in col for x in ["region", "location", "area"]):
            suggestion = "Regional trends indicate strong performance. Focus marketing in these areas."
        elif any(x in col for x in ["rating", "satisfaction", "score"]):
            suggestion = "Customer satisfaction is key. Analyze support or feature impact."
        else:
            suggestion = f"{col_name} shows an upward trend. Leverage this for strategic planning." if trend_slope > 0 else f"{col_name} is declining. Re-evaluate feature alignment with market needs."

    except Exception as e:
        suggestion = f"Could not analyze {col_name} due to: {str(e)}"

    return f"<i>AI Suggestion:</i> {suggestion}"





















import logging

logging.basicConfig(level=logging.INFO)

def generate_forecast_report(table_name):
    logging.info(f"Generating forecast for: {table_name}")
    
    conn = pymysql.connect(host='localhost', user='root', password='Rathish123', database='user_management')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT column_name, value, row_index FROM uploaded_datasets
        WHERE table_name = %s
    """, (table_name,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        raise ValueError("No data found for the given table name.")

    # Organize into DataFrame
    data = {}
    for col_name, value, row_idx in rows:
        data.setdefault(col_name, []).append(value)

    df = pd.DataFrame(data)
    df, numeric_cols = preprocess(df)
    df = cluster_importance(df, numeric_cols)
    metadata_cols = detect_metadata_columns(df, numeric_cols)

    result_html = f"<h1>Forecast Report: {table_name}</h1>"
    summaries = []

    for col in numeric_cols:
        if not is_forecastable(df[col]):
            continue

        df_col = df[[col]].dropna().reset_index(drop=True)
        df_col['ds'] = pd.date_range(start='2024-01-01', periods=len(df_col), freq='D')
        df_col = df_col.rename(columns={col: 'y'})

        model = Prophet()
        model.fit(df_col[['ds', 'y']])
        future = model.make_future_dataframe(periods=30)
        forecast = model.predict(future)

        graph = create_plot(model, forecast)
        trend, stddev = analyze_trend(forecast)
        explanation = ai_explanation(col, trend, stddev)
        suggestion = suggest_improvement_dynamic(col, forecast['yhat'].values, df[col].values)

        top_performer_label = None
        if metadata_cols:
            label_col = metadata_cols[0]
            best_label, best_value = get_best_performer(df, col, label_col)
            summaries.append((col, best_label, best_value))
            top_performer_label = best_label

        forecast_html = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(30).to_html(index=False)

        result_html += f"""
            <h2>{col}</h2>
            <img src='data:image/png;base64,{graph}' style='max-width:100%;'/><br>
            <p><b>Trend:</b> {trend} | <b>Std Dev:</b> {stddev:.2f}</p>
            <p>{explanation}</p>
            <p>{suggestion}</p>
            <h4>Top performer: {top_performer_label if top_performer_label else 'N/A'} in {col}</h4>
            {forecast_html}
            <hr>
        """

    if summaries:
        overall_best = max(summaries, key=lambda x: x[2])
        result_html += f"<h2 style='color:green;'>🏁 Overall Performance Suggestion:</h2>"
        result_html += f"<p>Across all metrics, <b>{overall_best[1]}</b> stands out with <b>{overall_best[0]}</b> value of <b>{overall_best[2]:.2f}</b>.</p>"

    if metadata_cols:
        result_html += f"<h3>🔍 Column-wise Summary:</h3><ul>{get_column_summary(df, numeric_cols, metadata_cols[0])}</ul>"

    return result_html


@app.route('/forecast/<table_name>')
def forecast(table_name):
    def dynamic_date_range(start='2024-01-01', periods=1000):
        if periods <= 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
            freq = 'D'
        elif periods <= 2400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
            freq = 'H'
        elif periods <= 144000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
            freq = 'T'
        elif periods <= 864000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
            freq = 'S'
        else:
            freq = 'L'
        return pd.date_range(start=start, periods=periods, freq=freq)

    try:
        logging.info(f"Generating forecast for: {table_name}")
        
        conn = pymysql.connect(host='localhost', user='root', password='Rathish123', database='user_management')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT column_name, value, row_index FROM uploaded_datasets
            WHERE table_name = %s
        """, (table_name,))
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            return "<h3 style='color:red;'>No data found for the given table name.</h3>"

        data = {}
        for col_name, value, row_idx in rows:
            data.setdefault(col_name, []).append(value)

        df = pd.DataFrame(data)
        df, numeric_cols = preprocess(df)
        df = cluster_importance(df, numeric_cols)
        metadata_cols = detect_metadata_columns(df, numeric_cols)

        result_html = f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: #f4f7fa;
                    padding: 30px;
                    color: #333;
                }}
                h1 {{
                    text-align: center;
                    color: #2c3e50;
                }}
                .section {{
                    background: white;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.06);
                    border-radius: 10px;
                    padding: 20px;
                    margin-bottom: 30px;
                }}
                .section h2 {{
                    color: #2980b9;
                }}
                img {{
                    border-radius: 8px;
                    margin: 10px 0;
                }}
                p {{
                    margin: 5px 0;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 10px;
                }}
                table, th, td {{
                    border: 1px solid #ddd;
                }}
                th, td {{
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
                ul {{
                    padding-left: 20px;
                }}
                .highlight {{
                    background-color: #e8f8f5;
                    padding: 10px;
                    border-left: 5px solid #1abc9c;
                    margin-top: 10px;
                    border-radius: 5px;
                }}
            </style>
        </head>
        <body>
        <h1>📊 Forecast Report: {table_name}</h1>
        """

        summaries = []

        for col in numeric_cols:
            if not is_forecastable(df[col]):
                continue

            df_col = df[[col]].dropna().reset_index(drop=True)

            max_periods = 10000
            if len(df_col) > max_periods:
                df_col = df_col.sample(n=max_periods, random_state=42).sort_index().reset_index(drop=True)

            df_col['ds'] = dynamic_date_range(periods=len(df_col))
            df_col = df_col.rename(columns={col: 'y'})

            model = Prophet()
            model.fit(df_col[['ds', 'y']])
            future = model.make_future_dataframe(periods=30)
            forecast = model.predict(future)

            graph = create_plot(model, forecast)
            trend, stddev = analyze_trend(forecast)
            explanation = ai_explanation(col, trend, stddev)
            suggestion = suggest_improvement_dynamic(col, forecast['yhat'].values, df[col].values)

            top_performer_label = None
            if metadata_cols:
                label_col = metadata_cols[0]
                best_label, best_value = get_best_performer(df, col, label_col)
                summaries.append((col, best_label, best_value))
                top_performer_label = best_label

            forecast_html = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(30).to_html(index=False)

            result_html += f"""
                <div class='section'>
                    <h2>📈 {col} Forecast</h2>
                    <img src='data:image/png;base64,{graph}' style='max-width:100%;'/>
                    <div class='highlight'><b>Trend:</b> {trend} | <b>Std Dev:</b> {stddev:.2f}</div>
                    <p>{explanation}</p>
                    <p><b>💡 Suggestion:</b> {suggestion}</p>
                    <p><b>🏆 Top performer:</b> {top_performer_label if top_performer_label else 'N/A'} in <b>{col}</b></p>
                    {forecast_html}
                </div>
            """

        if summaries:
            overall_best = max(summaries, key=lambda x: x[2])
            result_html += f"""
            <div class='section'>
                <h2 style='color:green;'>🏁 Overall Performance Suggestion</h2>
                <p>Across all metrics, <b>{overall_best[1]}</b> stands out with <b>{overall_best[0]}</b> value of <b>{overall_best[2]:.2f}</b>.</p>
            </div>
            """

        if metadata_cols:
            result_html += f"""
            <div class='section'>
                <h3>🔍 Column-wise Summary</h3>
                <ul>{get_column_summary(df, numeric_cols, metadata_cols[0])}</ul>
            </div>
            """

        result_html += "</body></html>"
        return render_template_string(result_html)

    except Exception as e:
        logging.error("Forecasting failed", exc_info=True)
        return f"<h3 style='color:red;'>Forecasting failed: {str(e)}</h3>"




if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  # default to 10000 locally
    app.run(host="0.0.0.0", port=port, debug=False)


    

