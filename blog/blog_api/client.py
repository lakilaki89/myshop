import requests


url = 'http://127.0.0.1:8000/api'

print(requests.get(f'{url}/categories').json())
