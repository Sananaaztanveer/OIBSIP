import urllib.request
import urllib.parse
import json

try:
    city = input("Enter your city name: ")

    # Find city coordinates
    city_url = "https://geocoding-api.open-meteo.com/v1/search?"
    city_params = urllib.parse.urlencode({
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    })

    with urllib.request.urlopen(city_url + city_params) as response:
        city_data = json.loads(response.read().decode())

    if "results" not in city_data:
        print("City not found!")

    else:
        latitude = city_data["results"][0]["latitude"]
        longitude = city_data["results"][0]["longitude"]
        city_name = city_data["results"][0]["name"]

        # Get current weather
        weather_url = "https://api.open-meteo.com/v1/forecast?"
        weather_params = urllib.parse.urlencode({
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m,weather_code"
        })

        with urllib.request.urlopen(weather_url + weather_params) as response:
            weather_data = json.loads(response.read().decode())

        current = weather_data["current"]

        weather_codes = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Foggy",
            48: "Foggy",
            51: "Light drizzle",
            53: "Moderate drizzle",
            55: "Heavy drizzle",
            61: "Light rain",
            63: "Moderate rain",
            65: "Heavy rain",
            80: "Rain showers",
            81: "Moderate rain showers",
            82: "Heavy rain showers",
            95: "Thunderstorm"
        }

        condition = weather_codes.get(
            current["weather_code"], "Other weather condition"
        )

        print("\n----- WEATHER REPORT -----")
        print("City:", city_name)
        print("Temperature:", current["temperature_2m"], "°C")
        print("Feels Like:", current["apparent_temperature"], "°C")
        print("Humidity:", current["relative_humidity_2m"], "%")
        print("Wind Speed:", current["wind_speed_10m"], "km/h")
        print("Weather:", condition)
        print("--------------------------")

except Exception as e:
    print("Unable to get weather information.")
    print("Error:", e)