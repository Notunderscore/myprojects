import json
import requests
# Request variables
lang = 'en'
city = 'donramiro'
appid = 'OPENWEATHERMAP_KEY'

wth = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&lang='+ lang +'&appid='+ appid).text
response = json.loads(wth)
print(response)
print(response['weather'][0]['id'])
print(LOL)
# print(main['temp'])
# print(main['feels_like'])
# print(main['temp'])
# print(main['temp_min'])
# print(main['temp_max'])
