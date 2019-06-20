from flaskexample import app 
from flask import request, jsonify
import sys 
import logging
import requests
import datetime

@app.route('/predict-birds')
def predict():
    day_of_week = request.args.get('day')
    day_of_week = datetime.datetime.strptime(day_of_week, '%m/%d/%Y').strftime('%w')
    location = request.args.get('location')
    time = request.args.get('time') 
    print(day_of_week, file=sys.stderr)
    coordinatesResult = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key=AIzaSyDqoIdz9z4_JwerQJgtqDMKqYPl0SAsr_w').json()
    lat, lng = getCoordinates(coordinatesResult)

    print(coordinatesResult, file=sys.stderr)
    # Return something like:
    # {"lat": 100, "lng": -100, "total_scooters": 19}
    return jsonify({"HELLO": 23434})

def getCoordinates(json):
    lat = json["results"][0]["geometry"]["location"]["lat"]
    lng = json["results"][0]["geometry"]["location"]["lng"]
    return lat, lng

def getGeohash(lat, lng):
	return

	#Get form data 
	#1. convert address to coordinate using geolocation API 
	#2. convert address to geohash using geohash (precision 7) and convert back to lat/long 
	#3. convert dropdown value to day_of_the_week numeric, and map to weekend or not 
	# Use form data to get predicted total of bird pickups
	#return pin drop of location with radius of segment and predicted value

