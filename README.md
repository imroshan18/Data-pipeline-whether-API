# Real-Time Weather Analytics System

## Overview

The Real-Time Weather Analytics System is a comprehensive data pipeline and visualization tool designed to fetch, process, and analyze current weather data. The application monitors weather parameters such as temperature, humidity, pressure, and wind speed in real-time, providing users with actionable insights and statistical trends through an interactive dashboard.

## Purpose

The primary objective of this project is to demonstrate a robust ETL (Extract, Transform, Load) pipeline integrated with a real-time analytics dashboard. By automating data ingestion and applying statistical methods for anomaly detection, the system serves as a reliable tool for monitoring environmental changes and identifying unusual weather patterns.

## Features

- Real-Time Data Ingestion: Automatically fetches current weather data from the Weatherstack API.
- Automated Data Persistence: Stores historical weather records in a local SQLite database for long-term analysis.
- Data Transformation: Implements rolling window calculations to determine mean and standard deviation of temperature.
- Anomaly Detection: Identifies temperature fluctuations that deviate significantly from historical trends.
- Interactive Dashboard: Visualizes temperature, humidity, and pressure trends using Plotly charts within a Streamlit interface.
- Statistical Summary: Provides a detailed breakdown of mean, median, standard deviation, and mode for recorded metrics.

## Tech Stack

- Language: Python
- Frontend/Visualization: Streamlit, Plotly
- Data Processing: Pandas, NumPy
- Database: SQLite
- API Integration: Requests (Weatherstack API)

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/saiiexd/live-weather-API.git
   cd live-weather-API
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the API Key:
   Open `pipeline.py` and replace the `API_KEY` placeholder with your valid Weatherstack API key.

## Usage

Once the installation is complete, you can launch the application by running:

```bash
streamlit run app.py
```

The dashboard will automatically refresh every 30 seconds to fetch and display the latest weather data.

## Project Structure

- `app.py`: The main Streamlit application script for the user interface and visualizations.
- `pipeline.py`: Contains the ETL logic, including data fetching, database operations, and analytical transformations.
- `weather_live.db`: SQLite database storing historical weather data.
- `requirements.txt`: List of Python libraries required for the project.
- `.streamlit/`: Configuration folder for Streamlit settings.

## License

This project is licensed under the MIT License.
