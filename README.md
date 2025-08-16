# Skycast

⚠️ Note: This project was developed as my graduation project in December 2022.
Please keep in mind that it may not be updated to reflect the latest changes, technologies, or best practices.

Abstract

This project aims to design and implement a real-time weather monitoring and forecasting system that combines Raspberry Pi–based sensors with external weather APIs (OpenWeatherMap and WeatherAPI). Data is processed in Python, stored in Firebase Realtime Database, and visualized through both a website/web apps and a dashboard (Power BI).

The system addresses the limitations of traditional weather stations by offering scalability, low cost, remote access, and rich analytics.

🎯 Objectives

Develop a low-cost IoT-based weather monitoring system using Raspberry Pi.

Collect real-time temperature, humidity, and pressure data from sensors.

Integrate data from external APIs (OpenWeatherMap & WeatherAPI) for forecasts, UV index, and air quality.

Store and manage data in Firebase Realtime Database.

Provide access through a website and web applications.

Build an interactive dashboard to visualize and compare sensor readings with API data.

Export structured datasets (CSV/Excel) for research purposes.

🏗 System Architecture

Hardware Layer

Raspberry Pi

DHT22 Sensor (temperature & humidity)

BMP180 Sensor (atmospheric pressure)

Software Layer

Python (data acquisition, processing, API integration)

Firebase Admin SDK (cloud database)

Power BI (dashboard & visualization)

Web technologies (for website + apps)

Data Sources

IoT sensor readings (local)

OpenWeatherMap API (current + forecast data)

WeatherAPI (air quality, UV index, precipitation)

User Access

Website + web apps for general users

Dashboard for researchers and advanced users

🌐 Website & Web Apps

Skycast includes a website and web applications that:

Display real-time local sensor readings.

Provide forecasts, air quality, and UV index data.

Offer user-friendly access on desktop and mobile.

(Add screenshots of your website/apps here!)

📊 Dashboard

An interactive dashboard (Power BI) is used to:

Compare sensor data vs API forecasts.

Analyze temperature, humidity, and pressure trends.

Track air quality, precipitation, and UV index.

Provide time-series visualizations for research.
