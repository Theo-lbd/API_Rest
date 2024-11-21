
# **Prévisions Météo : Toulouse et Saint-Geours-de-Maremne**

Ce projet est un programme Python qui interagit avec l'API d'[OpenWeatherMap](https://openweathermap.org/api) pour récupérer les prévisions météorologiques des 5 jours à venir pour les villes de **Toulouse** et **Saint-Geours-de-Maremne**.

## **Fonctionnalités**
- Récupération des températures minimales et maximales par jour sur une période de 5 jours.
- Support de plusieurs villes en utilisant leur nom et leur pays (exemple : "Toulouse,FR").

---

## **Prérequis**
1. Python 3.7 ou supérieur.
2. Une clé API valide pour OpenWeatherMap.
3. Le module `requests` installé dans votre environnement Python.

---

## **Installation**
1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone <URL_DU_DEPOT>
   cd <NOM_DU_DOSSIER>
   ```

2. Activez l'environnement virtuel ou utilisez-en un existant :
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Sur Linux/Mac
   .venv\Scripts\activate     # Sur Windows
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Ajoutez votre clé API OpenWeatherMap dans le fichier `main.py` :
   ```python
   API_KEY = "votre_clé_api"
   ```

---

## **Utilisation**
1. Exécutez le script dans un terminal :
   ```bash
   python main.py
   ```

2. Le programme affichera les prévisions météo pour Toulouse et Saint-Geours-de-Maremne sur 5 jours :
   - Température minimale
   - Température maximale

---

## **Exemple de sortie**
```
Prévisions météo pour Toulouse :
- 2024-11-21 : Min = 9.95°C, Max = 15.72°C
- 2024-11-22 : Min = 4.19°C, Max = 8.63°C
- 2024-11-23 : Min = 2.42°C, Max = 10.61°C
...

Prévisions météo pour Saint-Geours-de-Maremne :
- 2024-11-21 : Min = 10.09°C, Max = 14.59°C
- 2024-11-22 : Min = 5.41°C, Max = 10.41°C
...
```

---

## **Structure du projet**
```
Exercice_2_Meteo/
│
├── main.py           # Script principal
└── README.md         # Documentation du projet
```

---

## **API utilisée**
- [OpenWeatherMap - Forecast 5 jours](https://openweathermap.org/forecast5)
  - Fournit les prévisions météo toutes les 3 heures pour une période de 5 jours.

---
