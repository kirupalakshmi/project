import requests

endpoint = "http://localhost:8000/api/products/9876543456787654334567887654321234567890987654321"

get_response = requests.get(endpoint)
print(get_response.json())
print(get_response.status_code)