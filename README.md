# Skycast

# Abstract

This project aims to design and implement a real-time weather monitoring and forecasting system that combines Raspberry Pi–based sensors with external weather APIs (OpenWeatherMap and WeatherAPI). Data is processed in Python, stored in Firebase Realtime Database, and visualized through both a website/web apps and a dashboard (Power BI).

The system addresses the limitations of traditional weather stations by offering scalability, low cost, remote access, and rich analytics.

**Disclaimer:** This project was developed as my graduation project in December 2022.
Please keep in mind that it may not be updated to reflect the latest changes, technologies, or best practices.

---
# Objectives

- Develop a low-cost IoT-based weather monitoring system using Raspberry Pi.

- Collect real-time temperature, humidity, and pressure data from sensors.

- Integrate data from external APIs (OpenWeatherMap & WeatherAPI) for forecasts, UV index, and air quality.

- Store and manage data in Firebase Realtime Database.

- Provide access through a website and web applications.

- Build an interactive dashboard to visualize and compare sensor readings with API data.

- Export structured datasets (CSV/Excel) for research purposes.

---
# System Architecture

## Hardware Layer

- Raspberry Pi

- DHT22 Sensor (temperature & humidity)

- BMP180 Sensor (atmospheric pressure)

## Software Layer

- Python (data acquisition, processing, API integration)

- Firebase Admin SDK (cloud database)

- Power BI and Tableau (dashboard & visualization) 

- Web technologies (for website + apps)

## Data Sources

- IoT sensor readings (local)

- OpenWeatherMap API (current + forecast data)

- WeatherAPI (air quality, UV index, precipitation)

## User Access

- Website + web apps for general users

- Dashboard for researchers and advanced users

---

# Website & Web Apps

## Skycast includes a website and web applications that:

- Display real-time local sensor readings using Tableau.

- A responsive sidebar the website aint responsive

- A web App which Provides forecasts, air quality, and UV index data.

- A web App for news
  
---

## Website Screenshots

- Home Page
<p align="center">
  <img width="420" height="266" alt="image" src="https://github.com/user-attachments/assets/399e8ba8-2589-4796-a190-ba5406df7bfa" />
</p>

---

- Tableau Dashboard
<p align="center">
<img width="302" height="227" alt="image" src="https://github.com/user-attachments/assets/c7858745-5692-4272-b171-dbf825ce73af" />
</p>

---

- News
<p align="center">
<img width="418" height="176" alt="image" src="https://github.com/user-attachments/assets/892e99fa-a1dd-44e2-8baf-e72f79b17297" />
</p>

---

- About Us Page
<p align="center">
<img width="348" height="198" alt="image" src="https://github.com/user-attachments/assets/3bc0dd79-6732-4e1d-a900-1f0159f914ef" />
</p>

---

- Dark Mode Functionality
<p align="center">
<img width="227" height="149" alt="image" src="https://github.com/user-attachments/assets/98af4db1-08d4-4230-bcec-88c89a578ae4" />
</p>

---

# Dashboard

An interactive dashboard (Power BI) and Tableau is used to:

- Compare sensor data vs API forecasts.
- Analyze temperature, humidity, and pressure trends.
- Track air quality, precipitation, and UV index.
- Provide time-series visualizations for research.

---
- Tableau Dashboard Sample
![! (3)](https://github.com/user-attachments/assets/f684f7fb-e96d-41ca-9873-02e099fa34d0)

---
- Power Bi Dashboard Sample
<img width="1365" height="789" alt="image" src="https://github.com/user-attachments/assets/6beabdf9-d285-481d-a2f1-b67c506c9fb3" />


---

# Installation & Setup

## Clone the Repository

git clone https://github.com/LOAI-TK/Skycast.git

cd skycast

## Install Dependencies

pip install -r requirements.txt

## Configure Environment Variables

Create a .env file in the root directory:

FIREBASE_CRED_PATH=/path/to/serviceAccountKey.json

FIREBASE_DB_URL=https://your-project.firebaseio.com/

OPENWEATHER_API_KEY=your_openweather_api_key

WEATHER_API_KEY=your_weatherapi_key

---

# 🏗 System Design  

## Use Case Diagram  
![Case Diagram](https://github.com/user-attachments/assets/60e2c134-4f3e-4c55-a8ef-63cf15bc44a9)

## Flowchart

### RPI
![RPI Flowchart](https://github.com/user-attachments/assets/4a1d5519-3f1d-45e0-b5df-de840ee48f83)

### Preprocessing
![Data Prep Flowchart](https://github.com/user-attachments/assets/daafb660-3c01-40ea-8bf9-d63b84418745)

  


# Future Work


---
# Web 
- Make the website fully responsive across devices.
- Develop a web app for maps and radar visualization.

# Data Analysis
- Add lag and rolling window features for time-series analysis.

# Visualisation
- Build a more advanced dashboard with:
- Interactive filters (date ranges, location-based queries).
- Time-series anomaly detection highlights.
- Multi-panel comparison (sensor vs. API vs. forecast).
- Integration with the web app for live weather visualization.

# Hardware 
- Build a complete weather station that integrates additional missing sensors (e.g., wind speed/direction, rainfall gauge).

---


# Conclusion

Skycast demonstrates the feasibility of a low-cost, scalable, and accessible weather monitoring solution. By combining Raspberry Pi IoT hardware, Firebase cloud storage, external weather APIs, and modern visualization tools, the system provides accurate, real-time, and user-friendly weather insights accessible via sensors, APIs, a website, web apps, and dashboards.
