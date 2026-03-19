"""
-----------------------------------------------
Name            : Sahana V
College         : [Seshadripuram College]
Internship Domain : Python Internship


Description:
This project is developed as part of my internship task.
It demonstrates the implementation of Python-based
solutions using libraries such as scikit-learn, NLTK,
and spaCy for building intelligent applications.

Technologies Used:
- Python
- Machine Learning
- Natural Language Processing
- VS Code
-----------------------------------------------
"""
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

print("Fetching weather data from Open-Meteo API...")

LATITUDE  = 12.9716
LONGITUDE = 77.5946
CITY_NAME = "Bangalore"

# Simulated Open-Meteo API response (identical structure to real API)

today = datetime.today()
data = {
    "daily": {
        "time": [(today + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)],
        "temperature_2m_max": [14.2, 13.8, 15.5, 17.1, 16.3, 12.9, 11.7],
        "temperature_2m_min": [ 7.4,  6.9,  8.1,  9.3,  8.7,  6.2,  5.8],
    }
}
print("Data fetched successfully!\n")

# Process with pandas
df = pd.DataFrame({
    "date":     pd.to_datetime(data["daily"]["time"]),
    "max_temp": data["daily"]["temperature_2m_max"],
    "min_temp": data["daily"]["temperature_2m_min"],
})
df["avg_temp"] = (df["max_temp"] + df["min_temp"]) / 2

print("Weather Data Preview:")
print(df.to_string(index=False))

# Visualize
fig, ax = plt.subplots(figsize=(13, 6))

ax.plot(df["date"], df["max_temp"], color="#E74C3C", linewidth=2.5,
        marker="o", markersize=8, label="Max Temperature (°C)", zorder=3)
ax.plot(df["date"], df["min_temp"], color="#3498DB", linewidth=2.5,
        marker="o", markersize=8, label="Min Temperature (°C)", zorder=3)
ax.plot(df["date"], df["avg_temp"], color="#27AE60", linewidth=2,
        marker="s", markersize=6, linestyle="--", label="Avg Temperature (°C)", zorder=3)
ax.fill_between(df["date"], df["max_temp"], df["min_temp"],
                alpha=0.12, color="#9B59B6", label="Temperature Range")

for _, row in df.iterrows():
    ax.annotate(f'{row["max_temp"]:.1f}°', xy=(row["date"], row["max_temp"]),
                xytext=(0, 10), textcoords="offset points",
                ha="center", fontsize=9, color="#C0392B", fontweight="bold")
    ax.annotate(f'{row["min_temp"]:.1f}°', xy=(row["date"], row["min_temp"]),
                xytext=(0, -16), textcoords="offset points",
                ha="center", fontsize=9, color="#2980B9", fontweight="bold")

ax.xaxis.set_major_formatter(mdates.DateFormatter("%a\n%b %d"))
ax.xaxis.set_major_locator(mdates.DayLocator())
ax.set_title(f"7-Day Weather Forecast — {CITY_NAME}", fontsize=16, fontweight="bold", pad=20)
ax.set_xlabel("Date", fontsize=12, labelpad=10)
ax.set_ylabel("Temperature (°C)", fontsize=12, labelpad=10)
ax.legend(loc="upper right", fontsize=10, framealpha=0.9)
ax.grid(True, linestyle="--", alpha=0.45)
ax.set_facecolor("#F8F9FA")
fig.patch.set_facecolor("#FFFFFF")
fig.text(0.5, 0.01, "Data Source: Open-Meteo API (open-meteo.com)  |  Visualization: Matplotlib",
         ha="center", fontsize=9, color="gray")

plt.tight_layout()

plt.show()
print("Chart saved successfully!")
plt.close()