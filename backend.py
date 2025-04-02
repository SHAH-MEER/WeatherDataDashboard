import requests

API_KEY = "e8c4b0e89a3ec8d777065d543bb5dfc1"

def get_data(place,forecast_days=None,option=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url=url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = forecast_days * 8
    filtered_data = filtered_data[:nr_values]
    if option == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if option == "Weather":
        filtered_data = [dict["weather"][0]["main"]for dict in filtered_data]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Tokyo",forecast_days=3,option="Temperature"))