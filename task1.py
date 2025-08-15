import requests
import matplotlib.pyplot as plt

LAT, LON = 13.0827, 80.2707  # Chennai
URL = ("https://api.open-meteo.com/v1/forecast"
       f"?latitude={LAT}&longitude={LON}"
       "&daily=temperature_2m_max,temperature_2m_min"
       "&timezone=auto")

r = requests.get(URL, timeout=20)
r.raise_for_status()
daily = r.json()["daily"]

dates = daily["time"]
tmax = daily["temperature_2m_max"]
tmin = daily["temperature_2m_min"]

plt.figure(figsize=(10,5))
plt.plot(dates, tmax, marker="o", label="Max °C")
plt.plot(dates, tmin, marker="o", label="Min °C")
plt.title("Chennai — 7-Day Temperature Forecast")
plt.xlabel("Date"); plt.ylabel("Temperature (°C)")
plt.grid(True, alpha=0.3); plt.legend(); plt.tight_layout()
plt.savefig("chennai_forecast.png", dpi=140)
plt.show()
