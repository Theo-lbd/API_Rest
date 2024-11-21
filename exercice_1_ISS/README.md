
# **Station Spatiale Internationale (ISS) Tracker**

Ce projet est un programme Python qui interagit avec l'API publique d'[Open Notify](http://open-notify.org/) pour récupérer des informations en temps réel sur la position de la Station Spatiale Internationale (ISS) et sur son équipage actuel.

## **Fonctionnalités**
- Récupération de la position actuelle de l'ISS (latitude, longitude) avec horodatage.
- Affichage du nombre total d'occupants de l'ISS et de leurs noms.

---

## **Prérequis**
1. Python 3.7 ou supérieur.
2. Le module `requests` installé dans votre environnement Python.

---

## **Installation**
1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone <URL_DU_DEPOT>
   cd <NOM_DU_DOSSIER>
   ```

2. Activez l'environnement virtuel (s'il est partagé) ou créez-en un nouveau :
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Sur Linux/Mac
   .venv\Scripts\activate     # Sur Windows
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

---

## **Utilisation**
1. Exécutez le script dans un terminal :
   ```bash
   python main.py
   ```

2. Le programme affichera :
   - La position actuelle de l'ISS (latitude, longitude, horodatage).
   - Le nombre d'occupants à bord et leurs noms.

---

## **Exemple de sortie**
```
Position actuelle de l'ISS :
- Latitude : -13.3233
- Longitude : 67.0281
- Horodatage : 2024-11-21 07:52:51

Nombre d'occupants à bord : 12
Liste des occupants :
- Oleg Kononenko
- Nikolai Chub
- Tracy Caldwell Dyson
...
```

---

## **Structure du projet**
```
Exercice_1_ISS/
│
├── main.py           # Script principal
├── requirements.txt  # Liste des dépendances nécessaires
└── README.md         # Documentation du projet
```

---

## **API utilisée**
1. **Position de l'ISS** : [http://api.open-notify.org/iss-now.json](http://api.open-notify.org/iss-now.json)
   - Fournit la latitude, la longitude et l'horodatage.
2. **Liste des occupants de l'ISS** : [http://api.open-notify.org/astros.json](http://api.open-notify.org/astros.json)
   - Fournit le nombre d'occupants et leurs noms.

---
