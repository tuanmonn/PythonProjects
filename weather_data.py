#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 17:56:48 2021

@author: tuanmonn
"""

import requests
from datetime import date
import pandas as pd
import json
from datetime import datetime as dt
import time
import plotly.express as px
import plotly.graph_objs as go
import matplotlib as plt
import os


## Call real time

api_key = "4c927552bd6270096ecd24976efd3a03"

def get_city_lat_lon(city_name):
    API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        "q": city_name,
        "appid": api_key
        }
    response = requests.get(url= API_ENDPOINT, params=params)
    response.raise_for_status()
    data = response.json()
    
    get_city_lat_lon.lat = data["coord"]["lat"]
    get_city_lat_lon.lon = data["coord"]["lon"]



## Call 7 days

def get_forecast_data(city_name):
    get_city_lat_lon(city_name)
    API_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
    
    params = {
        "lat": get_city_lat_lon.lat,
        "lon": get_city_lat_lon.lon,
        "exclude": "minutely,hourly",
        "appid": api_key
        }
    
    response = requests.get(url= API_ENDPOINT, params=params)
    response.raise_for_status()
    get_forecast_data.forecast_data = response.json()
    
    ## Getting metadata
    
    get_forecast_data.weather_type = get_forecast_data.forecast_data["current"]["weather"][0]["description"]
    get_forecast_data.location = get_forecast_data.forecast_data["timezone"]
    get_forecast_data.temp = round(float(get_forecast_data.forecast_data["current"]["temp"] - 273.15),2)
    get_forecast_data.feels_like = round(float(get_forecast_data.forecast_data["current"]["feels_like"] - 273.15), 2)
    get_forecast_data.humidity = get_forecast_data.forecast_data["current"]["humidity"]
    get_forecast_data.windspeed = get_forecast_data.forecast_data["current"]["wind_speed"]
    get_forecast_data.uvi = get_forecast_data.forecast_data["current"]["uvi"]
    
    current_date = get_forecast_data.forecast_data["current"]["dt"]
    get_forecast_data.current_date_conv = date.fromtimestamp(current_date)


def viz_data(city_name):
    get_forecast_data(city_name)
    
    ## Get the daily data
    data = get_forecast_data.forecast_data["daily"]
    df = pd.DataFrame(data)  
    
    ## convert from unix to datetime
    
    ### write function to convert
    def conv_day(day):
        newday = time.strftime('%A', time.localtime(day))
        return newday
    
    df_date = df["dt"].apply(conv_day)
    
    
    ### Explode the dict in temp
    df_temp = df['temp'].apply(pd.Series)
    
    ### Merge the 2 dataFrame
    df_final = pd.concat([df_date, df_temp], axis = 1)
    df_final = df_final.loc[1:,:]
    
    ### Convert from kelvin to celsius
    df_final["cel_day"] = df_final["day"] - 273.15
    df_final["cel_night"] = df_final["night"] - 273.15
    
    ## Visualize
    trace1 = go.Scatter(x= df_final["dt"], y= df_final["cel_day"],name="day")
    trace2 = go.Scatter(x= df_final["dt"], y= df_final["cel_night"],name="night")
    
    layout = go.Layout(title= "Forecast of the next 7 days", xaxis= {"title": "Day of week"}, yaxis= {"title": "Temp"})

    
    figure = go.Figure(data= [trace1,trace2], layout = layout)
    figure.show()
    
    ### create a directory for the images
    if not os.path.exists("images"):
        os.mkdir("images")
    
    figure.write_image("images/fig1.png", engine="kaleido")











