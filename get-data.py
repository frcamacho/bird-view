#! /usr/bin/env

from pandas.io.json import json_normalize #package for flattening json in pandas df
from pathlib import Path
import pandas as pd
import json
import os 

#function to convert json data to pandas df 
def createDF(json_data):
    json_df = json_normalize(json_data['data'],record_path=['birds'],sep="_")
    time_stamp = json_data['timestamp']
    bird = pd.concat([json_df.drop(['location'], axis=1), json_df['location'].apply(pd.Series)], axis=1)
    bird['timestamp'] = time_stamp 
    return bird

def createCSV():
    pathlist = Path("./responses").glob('**/*.json') # return path object 
    bird_data_list = []
    for path in pathlist:
        path_in_str = str(path)
        with open(path_in_str) as f:
            json_f_data = json.load(f)
            try:
                json_bird_df = createDF(json_f_data)
                json_bird_df = json_bird_df.rename(columns = {'id':'bird_id'})
                bird_data_list.append(json_bird_df)
            except ValueError: # no data for scooters, scooters are offline 
                continue
    bird_data = pd.concat(bird_data_list, axis=0)
    bird_data.to_csv('bird-data.csv', index = None) # output aggregated json data to csv
    print("Completed!")


createCSV()