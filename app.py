
import os
import requests
import gradio as gr

# Get the API key from an environment variable
api_key = os.getenv("OPENWEATHER_API_KEY")

# Function to get weather for a city
def get_weather(city_name):
    if not city_name or not city_name.strip():
        return """
        ## ⚠️ City Name Required
        Please enter a city name to check the weather.
        """

    if not api_key:
        return """
        ## 🔑 API Key Missing
        Please configure your OPENWEATHER_API_KEY environment variable.
        """

    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city_name.strip(),
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(
            base_url,
            params=params,
            timeout=15
        )

        if response.status_code == 200:
            data = response.json()

            city = data["name"]
            country = data["sys"]["country"]
            weather_desc = data["weather"][0]["description"].title()
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            return f"""
# 🌦️ Weather Report

### 📍 {city}, {country}

---

## 🌤️ Current Conditions
**Weather:** {weather_desc}

## 🌡️ Temperature
**{temp} °C**

## 🤗 Feels Like
**{feels_like} °C**

## 💧 Humidity
**{humidity}%**

## 💨 Wind Speed
**{wind_speed} m/s**

---

*Weather information provided by OpenWeatherMap.*
"""

        elif response.status_code == 404:
            return """
            ## ❌ City Not Found
            Check the spelling or try another city name.
            """

        elif response.status_code == 401:
            return """
            ## 🔑 API Authentication Error
            Check whether your API key is correct and activated.
            """

        elif response.status_code == 429:
            return """
            ## ⏳ API Request Limit
            The API request limit may have been reached. Please try again later.
            """

        else:
            return f"""
            ## ❌ Weather Service Error
            The request failed with status code: {response.status_code}
            """

    except requests.exceptions.Timeout:
        return """
        ## ⏳ Request Timed Out
        The weather service took too long to respond. Please try again.
        """

    except requests.exceptions.RequestException:
        return """
        ## 🌐 Connection Error
        Please check your internet connection and try again.
        """

    except (KeyError, IndexError, TypeError, ValueError):
        return """
        ## ⚠️ Unexpected Response
        The weather service returned data in an unexpected format.
        """


# Create the Gradio interface
with gr.Blocks(
    theme=gr.themes.Soft(),
    title="Weather App"
) as demo:

    gr.Markdown("""
    # 🌦️ Weather App
    ### Discover the current weather in cities around the world.

    Enter a city name to explore its current weather conditions.
    """)

    with gr.Row():
        city_input = gr.Textbox(
            label="🏙️ City Name",
            placeholder="Enter a city, e.g. Hyderabad, London, Tokyo",
            scale=4
        )

        search_button = gr.Button(
            "🔍 Get Weather",
            variant="primary",
            scale=1
        )

    weather_output = gr.Markdown(
        label="Weather Information"
    )

    search_button.click(
        fn=get_weather,
        inputs=city_input,
        outputs=weather_output
    )

    city_input.submit(
        fn=get_weather,
        inputs=city_input,
        outputs=weather_output
    )

    gr.Markdown("""
    ---
    **Built with:** Python · Gradio · OpenWeatherMap API

    *This application displays current weather conditions, not a multi-day forecast.*
    """)


if __name__ == "__main__":
    demo.launch()
