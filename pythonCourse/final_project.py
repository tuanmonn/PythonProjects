#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 16:15:40 2021

@author: tuanmonn
"""
#=====================

import tkinter as tk
from weather_data import *
from PIL import Image, ImageTk


#=====================
## Define click function

def clickSearch():
    global img
    global pic
    user_input = entry.get()
    city_name = user_input
    viz_data(city_name)
    
    ### Change the text
    loc_text.config(text=f"{get_forecast_data.location} ({get_forecast_data.current_date_conv})")
    weather_type.config(text=f"{get_forecast_data.weather_type}")
    feel_text.config(text=f"Feels like: {get_forecast_data.feels_like}")
    temp_text.config(text=f"{get_forecast_data.temp}°C")
    humidity.config(text=f"Humidity: {get_forecast_data.humidity}")
    windspeed.config(text=f"Wind speed: {get_forecast_data.windspeed}")
    uv_text.config(text=f"UV: {get_forecast_data.uvi}")
    
    ### Insert the image in the bot_frame
    
    # img = tk.PhotoImage(file="images/fig1.png")
    # canvas1.create_image(300, 250, image=img)
    
    img = Image.open("images/fig1.png")
    img = img.resize((500,357), Image.ANTIALIAS)
    pic = ImageTk.PhotoImage(img)
    canvas1.create_image(250,180,image=pic) # half the size of canvas so it's in the center
    
    
    
#=====================
window = tk.Tk()
window.title("Weather App")

# create canvas
canvas = tk.Canvas(window, width=650, height=1000)


## Set background image
background_image= tk.PhotoImage(file="bg-image.png")
canvas.create_image(0,0, image=background_image, anchor="nw")
canvas.pack()


## top frame
top_frame = tk.Frame(window)
top_frame.place(relx= 0.12, rely= 0.1, width=500, height=30)  


## Search entry
entry = tk.Entry(top_frame)
entry.focus()
entry.place(width=400, height=30)

## Search button
search_button = tk.Button(top_frame)
search_button.config(text = "Search", command=clickSearch)
search_button.place(relx = 0.8, width=100, height=30)

## Label
guide_text = tk.Label(window)
guide_text.config(text="Enter a city name")
guide_text.place(relx=0.12, rely=0.08)


#=====================
    
## mid frame
mid_frame = tk.Frame(window, bg="#0C4271")
mid_frame.place(relx= 0.12, rely= 0.18, width= 500, height= 400)

## all types of text
### Location
loc_text = tk.Label(mid_frame, bg="#0C4271",fg="#FFFFFF")
loc_text.config(text="Location text", font=("Courier", 20))
loc_text.place(x= 250, y= 30, anchor="center")

### Weather type
weather_type = tk.Label(mid_frame, bg="#0C4271",fg="#FFFFFF")
weather_type.config(text="Weather type", font=("Courier", 15))
weather_type.place(x= 250, y= 60, anchor= "center")

### Temperature
temp_text = tk.Label(mid_frame, bg="#0C4271", fg="#FFFFFF")
temp_text.config(text="Temperature", font=("Courier", 70))
temp_text.place(x= 250, y= 170, anchor= "center")

## Feel like®
feel_text = tk.Label(mid_frame, bg="#0C4271",fg="#FFFFFF")
feel_text.config(text="Feels like", font=("Courier", 20))
feel_text.place(x= 150, y= 280, anchor= "center")
                    
## Humidity
humidity = tk.Label(mid_frame, bg="#0C4271",fg="#FFFFFF")
humidity.config(text="Humidity", font=("Courier", 20))
humidity.place(x= 350, y= 280, anchor= "center")

## Wind speed
windspeed = tk.Label(mid_frame, bg="#0C4271",fg="#FFFFFF")
windspeed.config(text="Wind Speed", font=("Courier", 20))
windspeed.place(x= 150, y= 330, anchor= "center")
                    
## UV
uv_text = tk.Label(mid_frame, bg="#0C4271",fg="#FFFFFF")
uv_text.config(text="UV", font=("Courier", 20))
uv_text.place(x= 350, y= 330, anchor= "center")


#=====================

## bot frame
# bot_frame = tk.Frame(window, bg="#262A53")
# bot_frame.place(relx= 0.1, rely= 0.6, width= 500, height= 400)

 
## Create canvas
canvas1 = tk.Canvas(window)
canvas1.place(relx=0.12, rely=0.6, width = 500, height= 350, anchor="nw")




window.mainloop()
