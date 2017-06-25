import requests
import json

apikey = 'ff7565be27395d18408df74dfd5728c7'
cities = ['Tokyo,JP', 'London,UK', 'New York,US']
api = 'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}'


def k2c(k):
    return k - 273.15


for name in cities:
    url = api.format(city=name, key=apikey)
    r = requests.get(url)
    data = json.loads(r.text)
    print('+ 都市 =', data['name'])
    print('| 天気 =', data['weather'][0]['description'])
    print('| 最低気温 =', k2c(data['main']['temp_min']))
    print('| 最高気温 =', k2c(data['main']['temp_max']))
    print('| 最高気温 =', k2c(data['main']['temp_max']))
    print('| 温度 =', data['main']['humidity'])
    print('| 気圧 =', data['main']['pressure'])
    print('| 風向き =', data['wind']['deg'])
    print('| 風速度 =', data['wind']['speed'])
    print('')
