# Importing all Libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import joblib

# Data Processing
rentalDF = pd.read_csv('data/rental_1000.csv')

# Data Transformation (Feature Engineering - Use Features for Model Development)
X = rentalDF[['rooms', 'sqft']].values   # Features 
y = rentalDF['price'].values             # Label

# Split Data into Training and Testing 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Model Training
model = LinearRegression().fit(X_train, y_train)

# Save the Model
joblib.dump(model,'rental_price_model.joblib')

# Load the Model
model = joblib.load('rental_price_model.joblib')

# Model Prediction
y_pred = model.predict(X_test)

# Compute RMSE
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse}")

# Example prediction for a specific test sample
sample_index = 0  # Change this index to test different samples
predict_rental_price = model.predict([X_test[sample_index]])[0]
print(f"The Real Rental Price for Rooms count={X_test[sample_index][0]} and Area in Sqft={X_test[sample_index][1]} is={y_test[sample_index]}")
print(f"The Predicted Rental Price for Rooms count={X_test[sample_index][0]} and Area in Sqft={X_test[sample_index][1]} is={predict_rental_price}")

# User Inputs For Predictions
# rooms_count = int(input("Enter the number of rooms:="))
# area_sqft   = float(input("Enter the Area in Sqft:="))

# user_input = np.array([[rooms_count,area_sqft]])

# predict_rental_price = model.predict(user_input)[0]

# print(f"The Predicted Rental Price for Rooms count={rooms_count} and Area in Sqft={area_sqft} is={predict_rental_price}")

