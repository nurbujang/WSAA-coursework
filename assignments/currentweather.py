'''
Assignment 1 for Web Services and Applications (Spring 2024)
currentweather.py
Author: Nur Bujang

Using the URL below:
https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m

Write a python program called currentweather.py 
that will print out the current temperature on the console (and only the temperature).
I have set the lat/long to my location, you may use that or a different location.

Last few marks:
Look at the documentation (below) and print out the current wind direction (10m) as well.

🌤️ Free Open-Source Weather API | Open-Meteo.com (https://open-meteo.com/)

Save the file into your assignments directory (or you can make a separate repo for it, I do not mind).
Copy a link to the directory/repo to here (please only put a link in here, other information can be in the readme).

'''

# Current temperature
# https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m
# Beatty (2024)

import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m"
response = requests.get(url)
data=response.json()

with open("currenttemperature2m.json", "w") as fp:
   json.dump(data, fp)

# get object "current" and "temperature_2m" 

current = data["current"]
temp2m = current["temperature_2m"]

print(temp2m)

# Current wind direction (10m)
# https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=wind_direction_10m

url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=wind_direction_10m"
response = requests.get(url)
data=response.json()

response = requests.get(url)
data=response.json()

with open("currentwinddir10m).json", "w") as fp: # with open, "w" is write mode (note.nkmk.me, 2023)
   json.dump(data, fp)

# get object "current" and "temperature_2m"

current = data["current"]
winddir10m = current["wind_direction_10m"]

print(winddir10m)


'''
REFERENCES

Beatty, A. (2024). andrewbeattycourseware/wsaa-course-material. [online] GitHub. Available at: https://github.com/andrewbeattycourseware/wsaa-course-material [Accessed 17 Feb. 2024].
https://api.open-meteo.com. (n.d.). Available at: https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m [Accessed 17 Feb. 2024].
https://open-meteo.com/. (n.d.). Available at: https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=wind_direction_10m [Accessed 17 Feb. 2024].
note.nkmk.me. (2023). Read, write, and create files in Python (with and open()) | note.nkmk.me. [online] Available at: https://note.nkmk.me/en/python-file-io-open-with/#open-a-file-for-writing-modew [Accessed 17 Feb. 2024].
_______________________________________________________________________________________________
End
'''
