import requests
from hello_plumber.consume import RApiConsumer
        
url = "http://localhost:8000/sum"
data = {"a": 4, "b": 5}
headers = {"Content-Type": "application/json"}

with RApiConsumer(port=8000):
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        print(f"Sum: {result}")
    else:
        print(f"Request failed with status code: {response.status_code}")