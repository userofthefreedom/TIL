import requests
from pprint import pprint
# url = 'https://fakestoreapi.com/carts'


cityname = "Seul,KR"
lat = 37.56
lon = 126.97
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apkey}' # type: ignore
data = requests.get(url).json()
pprint(data)

url = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={apkey}" # type: ignore
jsn_resp = requests.get(url).json()
description = jsn_resp['weather'][0]['description']
print(f'날씨 설명 :{description}')