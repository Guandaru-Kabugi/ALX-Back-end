import datetime as dt
import requests
from weather_retrieval import weather_data

BASE_URl = "https://api.openweathermap.org/data/2.5/weather?" #we create a base url that is present on the website
API_KEY = "3ec8406738737a8dbc88cf36d1b89987"
CITY = "Nairobi"

url = BASE_URl +"appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json() #convert it into a json file (dictionaries)
# print(response)
def convert_kelvin_to_celcius (kelvin_temp):
    celcius = kelvin_temp-273.15
    return celcius

weather = weather_data['weather']
weather_descp = weather_data['weather'][0]['description']
temperature = weather_data['main']['temp']
print(temperature)
print(f"The weather description is: {weather_descp}")
current_temp = convert_kelvin_to_celcius(temperature)
print(f"The current temperature is: {current_temp: .2f}")