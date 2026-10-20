# AI-Weather-App

# 🌦️ AI Weather App

An interactive weather application built with Python and Gradio that retrieves current weather information for cities around the world using the OpenWeatherMap API.

## 📌 Project Overview

The application allows users to enter a city name and view its current weather conditions through a simple, user-friendly interface.

It retrieves real-time weather data from an external API and displays important environmental information in an organized format.

## ✨ Features

- Search for weather by city name
- Display current temperature in Celsius
- Show feels-like temperature
- Display weather descriptions
- Show humidity levels
- Display wind speed
- Handle invalid city names
- Provide informative error messages
- Interactive web interface built with Gradio

## 🛠️ Technologies Used

- Python
- Gradio
- Requests
- OpenWeatherMap Current Weather API

## 📁 Project Structure

```text
AI-Weather-App/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd AI-Weather-App
```

### 3. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure your API key

Set your OpenWeatherMap API key as an environment variable.

**Windows PowerShell:**

```powershell
$env:OPENWEATHER_API_KEY="YOUR_ACTUAL_API_KEY"
```

Replace the placeholder with your own API key.

### 5. Run the application

```bash
python app.py
```

Open the local Gradio URL displayed in the terminal.

## 🔑 API Configuration

This project uses the OpenWeatherMap Current Weather API to retrieve weather information.

An active API key is required. Keep your actual key private and never commit it to a public repository.

## 🚀 Future Enhancements

- Add weather forecasts for upcoming days
- Display weather information using visual charts
- Add weather alerts where supported by the data provider
- Integrate an AI assistant to explain weather conditions
- Provide recommendations based on weather conditions

## 👩‍💻 Author

Lakshmi Manogna

## 📄 License

This project is available for learning and educational purposes.