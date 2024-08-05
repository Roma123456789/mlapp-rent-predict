#Importing all Libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Data Processing
rentalDF = pd.read_csv('data/rental_1000.csv')

# Data Transformation(Featurerization  - Use Features for Model Development)
X = rentalDF[['rooms','sqft']].values   # Features 
y = rentalDF['price'].values           # Label

# Split Data into Training and Testing 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Model Training
model = LinearRegression().fit(X, y)

# Model Prediction
predict_rental_price = model.predict(X_test[0].reshape(1,-1))[0]
print("The Real Rental Price for Rooms count=",X_test[0][0],"and","Area in Sqft =",X_test[0][1],"is =",y_test[0])
print("The Predicted Rental Price for Rooms count=",X_test[0][0],"and","Area in Sqft =",X_test[0][1],"is =",predict_rental_price)