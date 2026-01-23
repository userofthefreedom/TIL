import requests
from pprint import pprint
url = 'https://fakestoreapi.com/carts'
data = requests.get(url).json()
pprint(data)


