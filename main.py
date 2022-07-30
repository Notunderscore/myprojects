import json
import requests
# Request variables
lang = 'en'
city = 'donramiro'
appid = '3fcef97161f2ee10c05746de56fb066b'

wth = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&lang='+ lang +'&appid='+ appid).text
response = json.loads(wth)
print(response)
print(response['weather'][0]['id'])
# print(main['temp'])
# print(main['feels_like'])
# print(main['temp'])
# print(main['temp_min'])
# print(main['temp_max'])
