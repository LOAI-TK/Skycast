import datetime
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP
import board, busio

# Initialize sensors
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
i2c = busio.I2C(board.SCL, board.SDA)
bmp180 = BMP.BMP085()

def read_sensors():
    try:
        pressure = bmp180.read_pressure() / 100  # convert to hPa
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        return {
            'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'temperature': temperature,
            'pressure': pressure,
            'humidity': humidity
        }
    except RuntimeError as error:
        print(f"Error reading sensor data: {error}")
        return None
