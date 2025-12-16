# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:36:44 2024

@author: kavin
"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymysql
import os
import webbrowser
import pandas as pd
from joblib import load

# Set up Chrome browser path based on the operating system
if os.name == 'nt':  # Windows
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
elif os.name == 'posix':  # macOS/Linux
    chrome_path = "/usr/bin/google-chrome %s"

app1 = Flask(__name__)
app1.secret_key = 'your_secret_key'

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'DB_USERNAME',  # Replace with your MySQL username
    'password': 'DB_PASSWORD',  # Replace with your MySQL password
    'database': 'DB_NAME'  # Replace with your database name
}

# Load the trained model
model = load("house_price_model.joblib")

# Database connection function
def get_db_connection():
    return pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )

@app1.route('/')
def home():
    return render_template('home.html')

@app1.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        connection = get_db_connection()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        user = cursor.fetchone()
        cursor.close()
        connection.close()

        if user:
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            return redirect(url_for('predict'))  # Redirect to `predict` directly
        else:
            flash("Invalid email or password!", "error")
            return redirect(url_for('login'))

    return render_template('login.html')

@app1.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, password))
            connection.commit()
            cursor.close()
            connection.close()

            flash("Registration successful! Please log in.", "success")
            return redirect(url_for('login'))

        except pymysql.MySQLError as err:
            flash(f"Error: {err}", "error")
            return redirect(url_for('register'))

    return render_template('register.html')

@app1.route('/logout', methods=['POST'])
def logout():
    # Perform logout operations (e.g., session.clear())
    session.clear()  # Clear the session
    return redirect(url_for('home'))

@app1.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get input data from the form
            square_footage = float(request.form['square_footage'])
            num_bedrooms = int(request.form['num_bedrooms'])
            num_bathrooms = int(request.form['num_bathrooms'])
            year_built = int(request.form['year_built'])
            lot_size = float(request.form['lot_size'])
            garage_size = float(request.form['garage_size'])
            neighborhood_quality = int(request.form['neighborhood_quality'])

            # Prepare input data for the model
            input_data = pd.DataFrame({
                'Square_Footage': [square_footage],
                'Num_Bedrooms': [num_bedrooms],
                'Num_Bathrooms': [num_bathrooms],
                'Year_Built': [year_built],
                'Lot_Size': [lot_size],
                'Garage_Size': [garage_size],
                'Neighborhood_Quality': [neighborhood_quality]
            })

            # Make prediction
            prediction = model.predict(input_data)
            predicted_price = f"Rs.{prediction[0]:,.2f}"

            # Pass prediction to the template
            return render_template('predict.html', predicted_price=predicted_price)

        except Exception as e:
            flash(f"An error occurred during prediction: {e}", "error")
            return redirect(url_for('predict'))

    return render_template('predict.html')

if __name__ == '__main__':
    # Register Chrome as the browser
    if os.name == 'nt':  # Windows
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))
    elif os.name == 'posix':  # macOS/Linux
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("/usr/bin/google-chrome"))

    # Open the Flask app in Chrome
    webbrowser.get('chrome').open("http://127.0.0.1:5000")

    # Run the Flask app
    app1.run(debug=True, use_reloader=False)  # use_reloader=False ensures no additional browser tab opens
