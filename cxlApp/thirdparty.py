import requests

def call_third_party_api(data):
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
    return response.json(), response.status_code
