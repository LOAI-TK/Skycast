import os, requests, datetime
from dotenv import load_dotenv
from utils import degrees_to_cardinal

load_dotenv()

openweather_api_key = os.getenv("OPENWEATHER_API_KEY")
weather_api_key = os.getenv("WEATHER_API_KEY")

latitude = '29.944877'
longitude = '31.051934'

API_URL = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={openweather_api_key}&units=metric'
FORECAST_API_URL = f'https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={openweather_api_key}&units=metric'
WEATHERAPI_URL = f'http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={latitude},{longitude}&aqi=yes'
UV_API_URL = f'http://api.weatherapi.com/v1/forecast.json?key={weather_api_key}&q={latitude},{longitude}&days=1&aqi=yes&alerts=no'

def get_weather_data():
    r = requests.get(API_URL)
    return r.json() if r.status_code == 200 else None

def process_weather_data(data):
    return {
        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'temperature': data['main']['temp'],
        'feels_like': data['main']['feels_like'],
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'wind_deg': data['wind']['deg'],
        'cloudiness': data['clouds']['all'],
        'weather_description': data['weather'][0]['description']
    }

def get_forecast_data():
    r = requests.get(FORECAST_API_URL)
    return r.json() if r.status_code == 200 else None

def process_forecast_data(data):
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    temperature_forecast = [entry for entry in data['list'] if entry['dt_txt'].startswith(today)]
    max_temp = max(entry['main']['temp_max'] for entry in temperature_forecast)
    min_temp = min(entry['main']['temp_min'] for entry in temperature_forecast)
    wind_deg = temperature_forecast[0]['wind']['deg']
    return {
        'max_temp': max_temp,
        'min_temp': min_temp,
        'wind_direction': degrees_to_cardinal(wind_deg)
    }

def get_weatherapi_data():
    r = requests.get(WEATHERAPI_URL)
    return r.json() if r.status_code == 200 else None

def process_weatherapi_data(data):
    return {
        'rain_volume': data['current']['precip_mm'],
        'total_precipitation': data['current']['precip_in'],
        'air_quality': data['current']['air_quality']
    }

def get_uv_data():
    r = requests.get(UV_API_URL)
    return r.json() if r.status_code == 200 else None

def process_uv_data(data):
    return {'uv_index': data['forecast']['forecastday'][0]['day']['uv']}
