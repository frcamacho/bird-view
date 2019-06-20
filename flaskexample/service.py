from flaskexample import app 
from flask import request, jsonify
import pygeohash as gh
import geohash
import pandas as pd
import sys 
import logging
import requests
import datetime
import joblib


@app.route('/predict-birds')
def predict():
    day_of_week = request.args.get('day')
    day_of_week = datetime.datetime.strptime(day_of_week, '%m/%d/%Y').strftime('%w')
    location = request.args.get('location')
    time = request.args.get('time') 
    coordinatesResult = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key=AIzaSyDqoIdz9z4_JwerQJgtqDMKqYPl0SAsr_w').json()
    lat, lng = getCoordinates(coordinatesResult)
    data = {'day_of_week':[day_of_week], 'latitude':[lat], 'longitude':[lng], 'timestamp':[time]}
    data_query = pd.DataFrame(data) 
    data_query = getGeohash(data_query)
    data_query = checkIfWeekend(data_query)
    data_query = convertTimeStamp(data_query)
    data_query['latitude'] = data_query['geohash'].apply(lambda geo: decodegeo(geo, 0))
    data_query['longitude'] = data_query['geohash'].apply(lambda geo: decodegeo(geo, 1))
    data_query = data_query.drop(['geohash', 'timestamp'], axis=1)
    # Return something like:
    # {"lat": 100, "lng": -100, "total_scooters": 19}
    return jsonify({"HELLO": 23434})

def getCoordinates(json):
    lat = json["results"][0]["geometry"]["location"]["lat"]
    lng = json["results"][0]["geometry"]["location"]["lng"]
    return lat, lng

def getGeohash(df):
    df['geohash']= df.apply(lambda x: gh.encode(x.latitude, x.longitude, precision=6), axis=1) 
    #drop lat long here 
    return df

def decodegeo(geo, which):
    if len(geo) >= 6:
        geodecoded = geohash.decode(geo)
        return geodecoded[which]
    else:
        return 0

def checkIfWeekend(df):
    df['weekend'] = df['day_of_week'].apply(lambda x: 1 if x == 0 or x == 6 else 0) 
    return df

def convertTimeStamp(df):
    df.timestamp = pd.to_datetime(df.timestamp, format='%H:%M')
    df['hour'] = df.timestamp.apply(lambda x: x.hour)
    df['minute'] = df.timestamp.apply(lambda x: x.minute)
    return df

# def runModel(df):
#     pipe = joblib.load('finalized_model.sav')
#     total_num_scooters = pipe.predict(df)[0]
#     return df 

    #Get form data 
    #1. convert address to coordinate using geolocation API 
    #2. convert address to geohash using geohash (precision 7) and convert back to lat/long 
    #3. convert dropdown value to day_of_the_week numeric, and map to weekend or not 
    # Use form data to get predicted total of bird pickups
    #return pin drop of location with radius of segment and predicted value