import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime

# =========================
# CONFIG
# =========================
API_KEY = "7eac242d2796cba96ade8cb337c68199"
CITY = "Hyderabad"
DB_NAME = "weather_live.db"



# =========================
# DATABASE LAYER
# =========================
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            timestamp TEXT PRIMARY KEY,
            temperature REAL,
            humidity REAL,
            pressure REAL,
            wind_speed REAL
        )
    """)
    conn.commit()
    conn.close()


def store_data(data: dict):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO weather VALUES (?, ?, ?, ?, ?)
        """, (
            data["timestamp"],
            data["temperature"],
            data["humidity"],
            data["pressure"],
            data["wind_speed"]
        ))
    except sqlite3.IntegrityError:
        # Ignore duplicate timestamps
        pass
    conn.commit()
    conn.close()


def load_data() -> pd.DataFrame:
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql("SELECT * FROM weather", conn)
    conn.close()

    if not df.empty:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.sort_values("timestamp")

    return df


# =========================
# INGESTION LAYER
# =========================
def fetch_weather() -> dict | None:
    url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={CITY}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        # API failure handling
        if "success" in data and data["success"] is False:
            return None

        return {
            "timestamp": datetime.utcnow().isoformat(),
            "temperature": data["current"]["temperature"],
            "humidity": data["current"]["humidity"],
            "pressure": data["current"]["pressure"],
            "wind_speed": data["current"]["wind_speed"]
        }

    except requests.exceptions.RequestException:
        return None


# =========================
# TRANSFORMATION LAYER
# =========================
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    df = df.drop_duplicates()
    df = df.dropna()
    return df


def add_rolling_features(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df

    df["rolling_mean_temp"] = df["temperature"].rolling(window=3).mean()
    df["rolling_std_temp"] = df["temperature"].rolling(window=3).std()

    df["anomaly"] = np.where(
        abs(df["temperature"] - df["rolling_mean_temp"]) >
        2 * df["rolling_std_temp"],
        1,
        0
    )

    return df


# =========================
# ANALYTICS LAYER
# =========================
def compute_statistics(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    stats = df[["temperature", "humidity", "pressure", "wind_speed"]].agg(
        ["mean", "median", "std"]
    ).T

    stats["mode"] = df[["temperature", "humidity", "pressure", "wind_speed"]].mode().iloc[0]

    return stats


# =========================
# MASTER PIPELINE FUNCTION
# =========================
def run_pipeline():
    init_db()

    current = fetch_weather()

    if current is None:
        return None, None, None

    store_data(current)

    df = load_data()
    df = clean_data(df)
    df = add_rolling_features(df)

    stats = compute_statistics(df)

    return current, df, stats
