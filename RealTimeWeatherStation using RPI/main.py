import time
from sensors import read_sensors
from weather import (
    get_weather_data, process_weather_data,
    get_forecast_data, process_forecast_data,
    get_weatherapi_data, process_weatherapi_data,
    get_uv_data, process_uv_data
)
from firebase_service import sensor_ref, weather_ref

sensor_readings_count = 0

while True:
    sensor_data = read_sensors()
    if sensor_data:
        sensor_ref.push(sensor_data)
        print(f"Stored sensor data: {sensor_data}")
        sensor_readings_count += 1

        if sensor_readings_count % 1 == 0:  # Every cycle
            weather_data = get_weather_data()
            forecast_data = get_forecast_data()
            weatherapi_data = get_weatherapi_data()
            uv_data = get_uv_data()

            if weather_data and forecast_data and weatherapi_data and uv_data:
                merged = {
                    **process_weather_data(weather_data),
                    **process_forecast_data(forecast_data),
                    **process_weatherapi_data(weatherapi_data),
                    **process_uv_data(uv_data)
                }
                weather_ref.push(merged)
                print(f"Stored weather data: {merged}")

    time.sleep(1800)  # 30 minutes