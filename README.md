House Price Prediction using Linear Regression
This project implements a Linear Regression model to predict house prices based on:
1.Area 
2.Number of bedrooms
3.Number of bathrooms

The model is trained using Python's Scikit-learn, and the predictions are deployed via a Flask web application. Users can input property details through a simple web form and get an instant predicted price.

Project Features:
Exploratory Data Analysis (EDA) using pandas and matplotlib
Linear Regression Model using scikit-learn
Model serialization using joblib
Web Interface using Flask
Deployed locally 

Dataset :
The dataset includes features like:
1. Area: Size of the house
2. Bedrooms: Number of bedrooms
3. Bathrooms: Number of bathrooms
4. Price: Target variable (house price)


Machine Learning Model :
Model used: Linear Regression
Libraries: scikit-learn, numpy
Training data: Preprocessed dataset with area, bedrooms, and bathrooms
Output: Predicted price of the house

Web App : 
The project uses Flask to create a simple web interface:
Users enter area, bedrooms, and bathrooms
The app displays the predicted price instantly

Technologies Used:
Python	Programming language
pandas, numpy	Data manipulation
scikit-learn	ML model training
joblib	Saving and loading the model
Flask	Web framework
HTML/CSS Frontend templating
