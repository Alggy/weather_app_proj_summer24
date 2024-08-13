
from pgeocode import Nominatim
import requests
import json
from IPython.display import Image, display
from IPython.core.display import HTML
from pandas import DataFrame

import re

def is_valid_zip(zip_code):
    """Validates a US zip code."""
    zip_regex = r'^\d{5}(?:-\d{4})?$'
    return re.match(zip_regex, zip_code) is not None

degree_sign = u"\N{DEGREE SIGN}"

def to_image(url):
    return '<img src="'+ url + '" width="32" >'

def chopped_date(start_time):
    return start_time[5:10]

def display_forecast(zip_code, country_code="US"):
    """
    Displays a seven day weather forecast for the provided zip code.

    Params :

        country_code (str) a valid country code (see supported country codes list). Default is "US".

        zip_code (str) a valid US zip code, like "20057" or "06510".

    """
    nomi = Nominatim(country_code)
    geo = nomi.query_postal_code(zip_code)
    latitude = geo["latitude"]
    longitude = geo["longitude"]

    request_url = f"https://api.weather.gov/points/{latitude},{longitude}"
    response = requests.get(request_url)
    #print(response.status_code)
    parsed_response = json.loads(response.text)

    forecast_url = parsed_response["properties"]["forecast"]
    forecast_response = requests.get(forecast_url)
    #print(forecast_response.status_code)
    parsed_forecast_response = json.loads(forecast_response.text)

    periods = parsed_forecast_response["properties"]["periods"]
    daytime_periods = [period for period in periods if period["isDaytime"] == True]


    df = DataFrame(daytime_periods)
    
    df["date"] = df["startTime"].apply(chopped_date)

    df["img"] = df["icon"].apply(to_image)
 
    # # combined column for temp display
    # # ... h/t: https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-pandas-dataframe
    df["temp"] = df["temperature"].astype(str) + " " + degree_sign + df["temperatureUnit"]
 
    # # rename cols:
    df.rename(columns={
         "name":"day",
         "shortForecast": "forecast"
    }, inplace=True)

     # drop unused cols:
    df.drop(columns=[
        "temperature", "temperatureUnit", "temperatureTrend",
        "windSpeed", "windDirection",
        "startTime", "endTime",
        "number", "isDaytime", "detailedForecast"
        ], inplace=True)
 
    # re-order columns:
    df = df.reindex(columns=['day', 'date', 'temp', 'forecast', 'img'])
    
    # return df
    print("---")
    print("SEVEN DAY FORECAST")
    print("LOCATION:", f"{geo.place_name}, {geo.state_code}".upper())
    print("---")
    #return HTML(df.to_html(escape=False, formatters=dict(icon=to_image)))
    print(df)
    return df
    
 

if __name__ == "__main__":
    my_zip = input("Please enter a 5 digit zip code (i.e., 20057): ")
    if is_valid_zip(my_zip):
        display_forecast(my_zip)
    else:
        print("You entered invalid US zip code. Please try again")