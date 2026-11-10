
import requests

# Function to convert weather codes into descriptions
def get_weather_description(code):

    weather_conditions = {
        0: "Clear Sky",
        1: "Mainly Clear",
        2: "Partly Cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing Rime Fog",
        51: "Light Drizzle",
        53: "Moderate Drizzle",
        55: "Dense Drizzle",
        61: "Slight Rain",
        63: "Moderate Rain",
        65: "Heavy Rain",
        71: "Slight Snow",
        73: "Moderate Snow",
        75: "Heavy Snow",
        80: "Rain Showers",
        81: "Moderate Rain Showers",
        82: "Violent Rain Showers",
        95: "Thunderstorm",
        96: "Thunderstorm with Hail",
        99: "Heavy Thunderstorm with Hail"
    }

    return weather_conditions.get(code, "Unknown Weather Condition")


# Main function
def get_weather():

    print("\n================================")
    print("       BASIC WEATHER APP")
    print("================================")

    # Ask user for city
    city = input("Enter city name: ").strip()

    # Validate input
    if not city:
        print("Error: City name cannot be empty.")
        return

    try:
        # Step 1: Find city location
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        geo_response = requests.get(
            geo_url,
            params=geo_params,
            timeout=10
        )

        geo_response.raise_for_status()
        geo_data = geo_response.json()

        # Check whether city exists
        if not geo_data.get("results"):
            print("Error: City not found. Please enter a valid city.")
            return

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]
        country = location.get("country", "Unknown")

        # Step 2: Get current weather
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,"
                "relative_humidity_2m,"
                "apparent_temperature,"
                "weather_code,"
                "wind_speed_10m"
            ),
            "timezone": "auto"
        }

        weather_response = requests.get(
            weather_url,
            params=weather_params,
            timeout=10
        )

        weather_response.raise_for_status()
        weather_data = weather_response.json()

        # Step 3: Extract weather details
        current = weather_data["current"]

        temperature = current["temperature_2m"]
        feels_like = current["apparent_temperature"]
        humidity = current["relative_humidity_2m"]
        wind_speed = current["wind_speed_10m"]
        weather_code = current["weather_code"]

        # Step 4: Convert Celsius to Fahrenheit
        fahrenheit = (temperature * 9 / 5) + 32

        # Step 5: Get weather description
        description = get_weather_description(weather_code)

        # Step 6: Display weather report
        print("\n================================")
        print("          WEATHER REPORT")
        print("================================")

        print("City:", city_name)
        print("Country:", country)

        print("--------------------------------")
        print("Temperature:", round(temperature, 1), "°C")
        print("Temperature:", round(fahrenheit, 1), "°F")
        print("Feels Like:", round(feels_like, 1), "°C")
        print("Humidity:", humidity, "%")
        print("Wind Speed:", wind_speed, "km/h")
        print("Weather Condition:", description)

        print("================================")
        print("       Thank you for using")
        print("          WEATHER APP")
        print("================================")

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Error: Please check your internet connection.")

    except requests.exceptions.HTTPError:
        print("Error: Unable to retrieve weather information.")

    except requests.exceptions.RequestException:
        print("Error: Something went wrong while connecting to the API.")

    except (KeyError, TypeError, ValueError):
        print("Error: Weather data could not be processed.")


# Run the application
get_weather()
