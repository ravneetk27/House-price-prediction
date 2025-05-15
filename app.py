from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('house_price_model.pkl')  # Load saved model

@app.route('/')
def home():
    return render_template('index.html')  # Show input form

@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])
    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])

    prediction = model.predict([[area, bedrooms, bathrooms]])[0]

    return f"<h2>Predicted House Price: ${round(prediction, 2)}</h2>"

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  
    app.run(host='0.0.0.0', port=port, debug=True)
