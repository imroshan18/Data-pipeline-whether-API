import streamlit as st
import plotly.express as px
from streamlit_autorefresh import st_autorefresh
from pipeline import run_pipeline

st.set_page_config(layout="wide")
st_autorefresh(interval=30000, key="refresh")

st.title("Real-Time Weather Analytics")
st.caption("Auto-refreshing every 30 seconds")

current, df, stats = run_pipeline()

if current is None:
    st.error("Weather API failed. Check API key.")
    st.stop()

if df is None or df.empty:
    st.warning("No data yet.")
    st.stop()

# ---------------- KPI ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Temperature (°C)", current["temperature"])
col2.metric("Humidity (%)", current["humidity"])
col3.metric("Pressure (hPa)", current["pressure"])
col4.metric("Wind Speed (km/h)", current["wind_speed"])

st.divider()

# ---------------- Charts ----------------
st.plotly_chart(
    px.line(df, x="timestamp",
            y=["temperature", "rolling_mean_temp"],
            title="Temperature Trend"),
    use_container_width=True
)

st.plotly_chart(
    px.line(df, x="timestamp",
            y="humidity",
            title="Humidity Trend"),
    use_container_width=True
)

st.plotly_chart(
    px.line(df, x="timestamp",
            y="pressure",
            title="Pressure Trend"),
    use_container_width=True
)

st.divider()

# ---------------- Stats ----------------
st.subheader("Statistical Summary")
st.dataframe(stats)

if "anomaly" in df.columns and df["anomaly"].sum() > 0:
    st.error("Temperature anomaly detected.")
else:
    st.success("No anomalies detected.")

st.subheader("Last 20 Records")
st.dataframe(df.tail(20))
