from flaskexample import app 

@app.route('/predict-birds')
def predict():
	#Get form data 
	#Use form data to get predicted total of bird pickups
	#1. convert address to coordinate using geolocation API 
	#2. convert address to geohash using geohash (precision 7) and convert back to lat/long 
	#3. convert dropdown value to day_of_the_week numeric, and map to weekend or not 
	#return pin drop of location with radius of segment and predicted value