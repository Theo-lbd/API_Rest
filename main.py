import requests
from datetime import datetime, timezone


def fetch_iss_position():
    """
    Récupère la position actuelle de la Station Spatiale Internationale (ISS).

    Cette fonction utilise l'API Open Notify pour obtenir les informations suivantes :
    - Latitude de l'ISS
    - Longitude de l'ISS
    - Horodatage UTC de la position

    Retour :
        dict : Un dictionnaire contenant la latitude, la longitude et l'horodatage de la position de l'ISS.

    Lève :
        Exception : Si la requête API échoue ou si le statut HTTP n'est pas 200.
    """
    url = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        timestamp = datetime.fromtimestamp(data["timestamp"], tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
        position = data["iss_position"]
        return {
            "timestamp": timestamp,
            "latitude": position["latitude"],
            "longitude": position["longitude"]
        }
    else:
        raise Exception(f"Impossible de récupérer la position de l'ISS : {response.status_code}")


def fetch_iss_crew():
    """
    Récupère les informations sur l'équipage actuel de l'ISS.

    Cette fonction utilise l'API Open Notify pour obtenir :
    - Le nombre total d'occupants de l'ISS
    - Les noms des membres d'équipage présents à bord

    Retour :
        dict : Un dictionnaire contenant le nombre total d'occupants et une liste des membres d'équipage.

    Lève :
        Exception : Si la requête API échoue ou si le statut HTTP n'est pas 200.
    """
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        crew = data["people"]
        return {
            "number": data["number"],
            "crew": [{"name": person["name"], "craft": person["craft"]} for person in crew if person["craft"] == "ISS"]
        }
    else:
        raise Exception(f"Impossible de récupérer les informations sur l'équipage de l'ISS : {response.status_code}")


if __name__ == "__main__":
    """
    Point d'entrée principal du programme.

    Ce script affiche :
    - La position actuelle (latitude, longitude et horodatage) de l'ISS.
    - Le nombre d'occupants actuels de l'ISS et leurs noms.

    En cas d'erreur, un message expliquant la cause est affiché.
    """
    try:
        # Récupération de la position de l'ISS
        position = fetch_iss_position()
        print(f"Position actuelle de l'ISS :")
        print(f"- Latitude : {position['latitude']}")
        print(f"- Longitude : {position['longitude']}")
        print(f"- Horodatage : {position['timestamp']}")

        # Récupération des informations sur l'équipage de l'ISS
        crew_info = fetch_iss_crew()
        print(f"\nNombre d'occupants à bord : {crew_info['number']}")
        print("Liste des occupants :")
        for crew_member in crew_info["crew"]:
            print(f"- {crew_member['name']}")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
