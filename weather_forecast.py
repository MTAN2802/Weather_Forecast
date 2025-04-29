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


#Transforming data
def transform_data(data, days_ahead): #where days_ahead is how many days from current date to look at
    dateToSee = data["days"][days_ahead]
    location_weather = {
        "name": data["resolvedAddress"],
        "forecast_description": data["description"],
        "date": dateToSee["datetime"],
        "temp": dateToSee["temp"],
        "max_temp": dateToSee["tempmax"],
        "min_temp": dateToSee["tempmin"],
        "feelslike": dateToSee["feelslike"],
        "day_description": dateToSee["description"],
        "preciptype": ",".join(dateToSee["preciptype"]),
        "humidity": dateToSee["humidity"],
        "uvindex": dateToSee["uvindex"]
    }
    return location_weather