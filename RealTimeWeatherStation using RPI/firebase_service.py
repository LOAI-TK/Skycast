import os, firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv

load_dotenv()
cred_path = os.getenv("FIREBASE_CRED_PATH")

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://skycast-a73fa-default-rtdb.firebaseio.com'
})

sensor_ref = db.reference('sensor_data')
weather_ref = db.reference('weather_data')
