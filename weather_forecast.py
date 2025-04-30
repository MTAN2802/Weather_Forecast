#This will be a workload for getting weather data
# 
# importing libraries
import pandas as pd
import numpy as np
import os
import requests
import json

#Extracting data from visualcrossing
def extract_forecast(location):
    API_key = 'M39R4H5LW9W2UK4ELJDF7Y9GJ'
    URL = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&key={API_key}&contentType=json'
    response = requests.get(URL)
#Parsing results as JSON
    return response.json()


#Transforming data
def transform_data(data, days_ahead): #where days_ahead is how many days in the future to forecast the weather, max 2 weeks
    info_list = []
    for i in range(days_ahead+1):
        dateToSee = data["days"][i]
        location_weather = {
            "name": data["address"],
            "date": dateToSee["datetime"],
            "forecast_description": data["description"],
            "temp": dateToSee["temp"],
            "max_temp": dateToSee["tempmax"],
            "min_temp": dateToSee["tempmin"],
            "feelslike": dateToSee["feelslike"],
            "preciptype": ",".join(dateToSee["preciptype"]) if isinstance(dateToSee.get("preciptype"), (list, tuple)) else "Normal",
            "humidity": dateToSee["humidity"],
            "uvindex": dateToSee["uvindex"]
        }
        info_list.append(location_weather)
    return info_list

#Loading data
def load_data(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

#Run the ETL Pipeline altogether
def run_etl(location, days_ahead=0):
    extracted_data = extract_forecast(location)
    transformed_data = transform_data(extracted_data, days_ahead)
    load_data(transformed_data, "weather_forecast.csv")

run_etl('Kogarah', 14)