import requests

city = input("Введите город чтобы узнать погоду: ")
key = 'df90b50dc6d6065d7abf012f3d7a7e77'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={'df90b50dc6d6065d7abf012f3d7a7e77'}'
params = {'APPID': key, 'q': city, 'units': 'imperial'}
result = requests.get(url, params=params)
weather = result.json()

info = f'{str(weather["name"])}: {weather["main"]["temp"]} F'
print(weather)
print(info)