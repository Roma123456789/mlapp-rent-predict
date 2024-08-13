# Importing all Libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import joblib

# Load the Model
model = joblib.load('rental_price_model.joblib')

rooms_count = int(input("Enter the number of rooms:="))
area_sqft   = float(input("Enter the Area in Sqft:="))

user_input = np.array([[rooms_count,area_sqft]])

predict_rental_price = model.predict(user_input)[0]

print(f"The Predicted Rental Price for Rooms count={rooms_count} and Area in Sqft={area_sqft} is={predict_rental_price}")