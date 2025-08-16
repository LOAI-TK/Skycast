import os
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


# Load .env variables
load_dotenv()

# ----------------- CONFIGURATION -----------------
FIREBASE_CRED_PATH = os.getenv("FIREBASE_CRED_PATH")
FIREBASE_DB_URL = os.getenv("FIREBASE_DB_URL")
# Initialize Firebase
cred = credentials.Certificate(FIREBASE_CRED_PATH)
firebase_admin.initialize_app(cred, {
    'databaseURL': FIREBASE_DB_URL
})
sensor_ref = db.reference('sensor_data')
weather_ref = db.reference('weather_data')
#constant
Error=10


#--------------------------SensorDataPrep----------------------------------
# Retrieve sensor data from Firebase Realtime Database
sensor_data = sensor_ref.get()
sensor_data_list = [data for data in sensor_data.values() if isinstance(data, dict)]
# Convert sensor data to a pandas DataFrame and set timestamp as index
sensor_data_df = pd.DataFrame(sensor_data_list).set_index('timestamp')
# Convert index to DateTime
sensor_data_df.index = pd.to_datetime(sensor_data_df.index)
# Resample sensor data to 1 minute frequency and fill missing values
sensor_data_df = sensor_data_df.resample('30Min').mean().fillna(method='ffill')
# Add key column for merging
sensor_data_df['key'] = 1
# Retrieve weather data from Firebase Realtime Database
weather_data = weather_ref.get()
weather_data_list = [data for data in weather_data.values() if isinstance(data, dict)]
# Create temporary DataFrames for raw sensor and weather data
raw_sensor_data_df = pd.DataFrame(sensor_data_list)
raw_weather_data_df = pd.DataFrame(weather_data_list)
# Print raw sensor data in tabular form
print("Sensor Data:\n", raw_sensor_data_df.head(), "\n")
# Print raw weather data in tabular form
print("Weather Data:\n", raw_weather_data_df.head())
# Convert weather data to a pandas DataFrame and set timestamp as index
weather_data_df = pd.DataFrame(weather_data_list).set_index('timestamp')
print("Sensor Data:\n", sensor_data_df.head(), "\n\nWeather Data:\n", weather_data_df.head())



#--------------------------WeatherAPI-DataPrep----------------------------------
# Function to extract air quality parameters
def extract_air_quality_parameters(air_quality):
    if air_quality is None or not isinstance(air_quality, dict):
        return pd.Series({
            'co': None,
            'gb_defra_index': None,
            'no2': None,
            'o3': None,
            'pm10': None,
            'pm2_5': None,
            'so2': None,
            'us_epa_index': None
        })

    return pd.Series({
        'co': air_quality.get('co'),
        'gb_defra_index': air_quality.get('gb-defra-index'),
        'no2': air_quality.get('no2'),
        'o3': air_quality.get('o3'),
        'pm10': air_quality.get('pm10'),
        'pm2_5': air_quality.get('pm2_5'),
        'so2': air_quality.get('so2'),
        'us_epa_index': air_quality.get('us-epa-index')
    })
# Extract air quality parameters and add them as separate columns
weather_data_df = weather_data_df.join(weather_data_df['air_quality'].apply(extract_air_quality_parameters))
# Drop the original 'air_quality' column
weather_data_df = weather_data_df.drop(columns=['air_quality'])
# Convert index to DateTime
weather_data_df.index = pd.to_datetime(weather_data_df.index)
# Separate numerical and non-numerical columns in weather_data_df
numerical_columns = weather_data_df.select_dtypes(include=[np.number]).columns
non_numerical_columns = weather_data_df.select_dtypes(exclude=[np.number]).columns
weather_data_numerical = weather_data_df[numerical_columns]
weather_data_non_numerical = weather_data_df[non_numerical_columns]
# Resample numerical data
weather_data_numerical_resampled = weather_data_numerical.resample('30Min').mean().fillna(method='ffill')
# Define custom aggregation function for non-numerical data (e.g., last non-null value)
def last_non_null(series):
    return series.dropna().iloc[-1] if not series.dropna().empty else None
# Resample non-numerical data using the custom aggregation function
weather_data_non_numerical_resampled = weather_data_non_numerical.resample('30Min').agg(last_non_null).fillna(method='ffill')
# Merge resampled numerical and non-numerical data
weather_data_df_resampled = pd.concat([weather_data_numerical_resampled, weather_data_non_numerical_resampled], axis=1)
# Add key column for merging
weather_data_df_resampled['key'] = 1
# Merge sensor and weather data on closest timestamp
merged_data = pd.merge_asof(sensor_data_df, weather_data_df_resampled, on='key', by='timestamp')
# Include the air quality parameter columns in the output
columns_to_keep = ['timestamp', 'temperature_x', 'pressure_x', 'humidity_x',
                   'temperature_y', 'feels_like', 'pressure_y', 'humidity_y',
                   'wind_speed', 'wind_deg', 'cloudiness', 'weather_description', 'wind_direction', 'max_temp', 'min_temp',
                   'rain_volume', 'uv_index', 'total_precipitation',
                   'co', 'gb_defra_index', 'no2', 'o3', 'pm10', 'pm2_5', 'so2', 'us_epa_index']
reduced_data = merged_data[columns_to_keep]
# Rename columns for clarity
reduced_data.columns = ['timestamp', 'sensor_temperature', 'sensor_pressure', 'sensor_humidity',
                        'weather_temperature', 'weather_feels_like', 'weather_pressure', 'weather_humidity',
                        'weather_wind_speed', 'weather_wind_deg', 'weather_cloudiness', 'weather_description', 'weather_wind_direction', 'weather_max_temp', 'weather_min_temp',
                        'weather_rain_volume', 'weather_uv_index', 'weather_total_precipitation',
                        'weather_co', 'weather_gb_defra_index', 'weather_no2', 'weather_o3', 'weather_pm10', 'weather_pm2_5', 'weather_so2', 'weather_us_epa_index']
# Create a separate copy of the DataFrame to avoid the "SettingWithCopyWarning"
reduced_data = reduced_data.copy()
# Add the constant value to the 'sensor_temperature' column
reduced_data['sensor_pressure'] = reduced_data['sensor_pressure'] + Error
# Format the timestamp column to display AM/PM
reduced_data['timestamp'] = reduced_data['timestamp'].dt.strftime('%Y-%m-%d %I:%M %p')
# Add Latitude, Longitude, and Country columns
reduced_data = reduced_data.assign(
    Latitude=29.944877,
    Longitude=31.051934,
    Country="Egypt"
)



# Load output directory from .env or fallback to ./data
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./data")
# Make sure the directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)
# Save prepared data
csv_path = os.path.join(OUTPUT_DIR, "prepared_data.csv")
xlsx_path = os.path.join(OUTPUT_DIR, "prepared_data.xlsx")
reduced_data.to_csv(csv_path, index=False)
reduced_data.to_excel(xlsx_path, index=False)
print(f"Data saved to:\n- {csv_path}\n- {xlsx_path}")