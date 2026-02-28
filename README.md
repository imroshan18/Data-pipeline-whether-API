

### Real-Time Weather ETL & Monitoring Dashboard

WeatherPulse Analytics is a real-time data engineering and visualization system designed to collect, process, store, and analyze live weather data. The project demonstrates an end-to-end ETL pipeline integrated with a statistical monitoring dashboard.

This repository highlights practical implementation of:

* API-driven data ingestion
* Automated data persistence
* Rolling statistical analysis
* Anomaly detection
* Interactive visualization

---

## Author

**imroshan18**

---

## Project Objective

The goal of WeatherPulse Analytics is to simulate a production-style environmental monitoring system.

The system:

* Extracts live weather metrics from an external API
* Transforms raw data into structured analytical formats
* Loads processed data into a persistent storage layer
* Detects abnormal temperature variations
* Visualizes trends through an interactive dashboard

This project reflects core principles of data engineering and real-time analytics.

---

## System Architecture

The application follows a structured ETL workflow.

---

### 1. Extract Layer

Weather data is retrieved programmatically from the Weatherstack API, including:

* Temperature
* Humidity
* Atmospheric pressure
* Wind speed

API communication is handled through HTTP requests.

---

### 2. Transform Layer

The transformation pipeline performs:

* Data cleaning
* Rolling mean calculations
* Standard deviation computation
* Statistical summary metrics
* Temperature anomaly detection

An anomaly is flagged when temperature deviates significantly from rolling historical averages.

---

### 3. Load Layer

Processed data is stored in a local SQLite database.

This enables:

* Historical trend analysis
* Persistent data retention
* Lightweight local deployment

---

### 4. Visualization Layer

The frontend dashboard (Streamlit + Plotly) provides:

* Time-series visualizations
* Dynamic temperature trends
* Humidity and pressure charts
* Statistical summaries
* Automated refresh cycle (30 seconds)

---

## Technology Stack

| Layer                | Technology        |
| -------------------- | ----------------- |
| Programming Language | Python            |
| Data Processing      | Pandas, NumPy     |
| Visualization        | Streamlit, Plotly |
| Database             | SQLite            |
| API Integration      | Requests          |
| Architecture Pattern | ETL Pipeline      |

---

## Installation Guide

### 1. Clone Repository

```bash id="cl2m9a"
git clone https://github.com/imroshan18/WeatherPulse-Analytics.git
cd WeatherPulse-Analytics
```

---

### 2. Create Virtual Environment

```bash id="mk8v1x"
python -m venv .venv
```

Activate environment:

**Windows**

```bash id="wq7e21"
.venv\Scripts\activate
```

**macOS/Linux**

```bash id="lj3rfa"
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash id="qe4tr1"
pip install -r requirements.txt
```

---

### 4. Configure API Key

Open:

```id="pj2kfs"
pipeline.py
```

Replace the placeholder value with your Weatherstack API key.

---

## Running the Application

Launch the dashboard:

```bash id="df8sma"
streamlit run app.py
```

The interface will be available at:

```id="lx9m3v"
http://localhost:8501
```

The dashboard refreshes automatically every 30 seconds.

---

## Project Structure

```id="u72nsp"
WeatherPulse-Analytics/
│
├── app.py              # Streamlit dashboard
├── pipeline.py         # ETL and analytics logic
├── data/               # Local database storage
├── requirements.txt
├── .streamlit/         # Streamlit configuration
└── README.md
```

---

## Analytical Capabilities

The system computes:

* Mean temperature
* Median temperature
* Standard deviation
* Mode
* Rolling average trends
* Temperature anomaly flags

This enables near real-time environmental monitoring.

---

## Design Principles

* Modular ETL separation
* Lightweight local database usage
* Automated refresh cycle
* Statistical anomaly detection
* Clean visualization architecture

---

## Potential Enhancements

* Add multi-city monitoring
* Integrate PostgreSQL instead of SQLite
* Add alert notification system (email/SMS)
* Deploy to cloud (AWS / Azure)
* Docker containerization
* Historical trend export (CSV / PDF reports)
* Integrate time-series forecasting model

---

## Professional Positioning

This project demonstrates proficiency in:

* Real-time data pipelines
* API integration
* Data transformation workflows
* Statistical anomaly detection
* Interactive data dashboards
* Lightweight database systems

