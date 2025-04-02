# Weather Data Dashboard 🌦️📊🌍

## Overview 🌎✨📉

The Weather Data Dashboard is a Streamlit-based web application that allows users to check the weather forecast for a specified city. Users can select the number of forecast days (1-5) and choose to view either temperature trends or weather conditions. The application utilizes a backend function (`get_data`) to fetch weather data and visualizes it using Plotly and images. 📊🌤️🔍

## Features ⚙️📌🛠️

- **User Input:** ✏️📍🔎
  - 🏙️ Enter a city name to fetch weather data.
  - 📅 Select the number of forecast days (1-5) using a slider.
  - 📊 Choose between temperature trends (line plot) or weather conditions (images).
- **Data Visualization:** 📈🌤️📸
  - 📉 Displays temperature trends using a line plot (updated every 3 hours).
  - 🌥️ Shows weather conditions using representative images (Clouds, Clear, Rain, Snow).
- **Error Handling:** ⚠️❗📝
  - ℹ️ Provides an informative message if the city name is incorrect.

## Technologies Used 🖥️🔧📡

- **Frontend:** 🎨🖥️💻 Streamlit (for web UI)
- **Visualization:** 📊📈📉 Plotly (for line plots)
- **Backend:** 🔄📡⚙️ Python function (`get_data`) to fetch weather data
- **Images:** 🖼️🌦️📸 Weather icons for visual representation

## Installation and Setup 📥🛠️💻

### Prerequisites ✅📌📂

Ensure you have Python installed on your system. You also need to install the required dependencies. 🐍📦⚙️

### Installation Steps 🚀📡💽

1. 📂 Clone the repository:
   ```sh
   git clone https://github.com/SHAH-MEER/WeatherDataDashboard.git
   cd weather-dashboard
   ```
2. 🔧 Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. 📦 Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. ▶️ Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## Usage 📊📌👨‍💻

1. 🏙️ Enter a valid city name.
2. 📅 Select the number of forecast days (1-5).
3. 📊 Choose to view either temperature trends (line graph) or weather conditions (image representation).
4. 🌤️ View the visualized weather forecast.

## File Structure 📂📁📜

```
weather-dashboard/
│── main.py              # Main Streamlit app
│── backend.py           # Backend script for fetching weather data
│── requirements.txt     # Dependencies
│── images/              # Folder containing weather condition images
│── README.md            # Project documentation
```

## Future Improvements 🚀💡📈

- 🎨 **Enhance the UI** with better styling.
- ⚠️ **Improve Error Handling** to provide more detailed feedback.
- 📅 **Expand Forecasting Range** to more than 5 days.
- 🌡️ **Integrate Additional Weather Metrics** like humidity, wind speed, etc.

## Contributing 🤝💻📥

Feel free to contribute by submitting issues or pull requests. 🛠️🔄🌍

## Author ✍️👨‍💻📧

[Shahmeer Shahzad] 🚀🎨📝

