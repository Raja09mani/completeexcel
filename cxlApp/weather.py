import requests

def call_weather_api(data):
    api_key = '91e7bb48e38a84ebb1ba1560bd8238d6'  # Replace with your actual API key
    city = data.get('city')
    print(city)
    if not city:
        return {"error": "City is required"}, 400
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    print(url)
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}, 500
