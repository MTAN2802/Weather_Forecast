#This will be a workload for getting weather data
# 
# importing libraries
import pandas as pd
import numpy as np
import os
import requests
import json

#Extracting data
def extract_forecast(location):
    API_key = 'M39R4H5LW9W2UK4ELJDF7Y9GJ'
    URL = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&key={API_key}&contentType=json'
    response = requests.get(URL)
#Parsing results as JSON
    return response.json()


kogarah = extract_forecast("kogarah")
print(kogarah["days"][1]['datetime'])
#Transforming data
def transform_data(data):
    location_weather = {
        "name": data["resolvedAddress"],
        "description": data["description"],
        "date": data["days"]["datetime"]
    }