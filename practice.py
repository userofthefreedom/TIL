# import requests
# from pprint import pprint
# # url = 'https://fakestoreapi.com/carts'


# cityname = "Seul,KR"
# lat = 37.56
# lon = 126.97
# # type: ignore
# url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apkey}'
# data = requests.get(url).json()
# pprint(data)

# # type: ignore
# url = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={apkey}"
# jsn_resp = requests.get(url).json()
# description = jsn_resp['weather'][0]['description']
# print(f'날씨 설명 :{description}')

for i in range(5):
    print(i)
    if i == 3:
        print('중단')
        break
else:
    print("출력되지 않는다")

for i in range(5):
    print(i)
    if i == 6:
        print('중단')
        break
else:
    print("출력된다")
