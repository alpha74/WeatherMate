"""
	WEATHER MATE
		* Uses OpenWeather API to get JSON of weather data of a city
	
	Author: Aman Kumar @alpha74
"""

import requests

# Set API address: Add API address
api_address = " " + "&q="

city = input( "City: " )		# Taking city as input
	
api_url = api_address + city	# Concatenating API address and city

json_output = requests.get( api_url ).json()

# Extracting some information
city_weather = json_output['weather'][0]['main']			# Weather	
city_temp =  float( json_output['main']['temp'] ) - 273.15	# Temperature
city_humd = float( json_output['main']['humidity'] )		# Humidity

print( "\n  " + city + " Weather" )
print( " Weather: \t", city_weather )
print( " Temperature: \t", city_temp, "C" )
print( " Humidity: \t", city_humd, "%" )



