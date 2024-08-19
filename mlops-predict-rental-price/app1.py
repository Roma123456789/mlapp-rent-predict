from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('rental_price_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    rooms_count = data.get('rooms')
    area_sqft = data.get('sqft')

    if rooms_count is None or area_sqft is None:
        return jsonify({'error': 'Please provide both rooms and sqft'}), 400

    user_input = np.array([[rooms_count, area_sqft]])
    predict_rental_price = model.predict(user_input)[0]

    return jsonify({'predicted_price': predict_rental_price})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
