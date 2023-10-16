import requests

headers = {'Authorization' : 'bearer 441cce1187e40bc32c2e9cfeaa6356babd0f628f'}
endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "this field is done",
    "price": 32.99
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
print(get_response.status_code)