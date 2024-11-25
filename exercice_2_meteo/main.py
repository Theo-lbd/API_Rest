import requests
from datetime import datetime, timezone

API_KEY = "YOUR_KEY"


def fetch_weather_forecast(city):
    """
    Récupère les prévisions météorologiques pour les 5 prochains jours pour une ville donnée.

    Paramètres :
        city (str) : Le nom de la ville (par exemple "Toulouse,FR").

    Retour :
        dict : Un dictionnaire contenant les températures minimales et maximales par jour.

    Lève :
        Exception : Si la requête API échoue ou si le statut HTTP n'est pas 200.
    """
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "units": "metric",
        "appid": API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        daily_temperatures = {}
        for forecast in data["list"]:
            date = datetime.fromtimestamp(forecast["dt"], tz=timezone.utc).strftime('%Y-%m-%d')
            temp_min = forecast["main"]["temp_min"]
            temp_max = forecast["main"]["temp_max"]
            if date not in daily_temperatures:
                daily_temperatures[date] = {"min": temp_min, "max": temp_max}
            else:
                daily_temperatures[date]["min"] = min(daily_temperatures[date]["min"], temp_min)
                daily_temperatures[date]["max"] = max(daily_temperatures[date]["max"], temp_max)
        return daily_temperatures
    else:
        raise Exception(f"Impossible de récupérer les prévisions météo : {response.status_code}")


if __name__ == "__main__":
    """
    Point d'entrée principal du programme.

    Ce script affiche les températures minimales et maximales pour les 5 jours à venir à Toulouse
    et Saint-Geours-de-Maremne.
    """
    try:
        cities = ["Toulouse,FR", "Saint-Geours-de-Maremne,FR"]
        for city in cities:
            print(f"Prévisions météo pour {city.split(',')[0]} :")
            forecast = fetch_weather_forecast(city)
            for date, temps in forecast.items():
                print(f"- {date} : Min = {temps['min']}°C, Max = {temps['max']}°C")
            print("\n")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
