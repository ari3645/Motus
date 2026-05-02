# -*- coding: utf-8 -*-
import requests
import random

def fetch_random_word(length):
    """Récupère un mot aléatoire de la longueur donnée via l'API."""
    url = f"https://random-word-api.herokuapp.com/word?lang=fr&length={length}&number=1"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            words = response.json()
            return words[0].upper() if words else None
    except Exception:
        pass
    return None

def validate_word_online(word):
    """Vérifie si le mot existe via la Dictionary API."""
    url = f"https://api.dictionaryapi.dev/api/v2/entries/fr/{word.lower()}"
    try:
        response = requests.get(url, timeout=3)
        # 200 = trouvé, 404 = pas trouvé
        return response.status_code == 200
    except Exception:
        # En cas d'erreur réseau, on peut choisir d'être permissif 
        # ou de renvoyer False. Ici, on renvoie True pour ne pas bloquer le jeu.
        return True

def get_definition(word):
    """Récupère la définition du mot si disponible."""
    url = f"https://api.dictionaryapi.dev/api/v2/entries/fr/{word.lower()}"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            data = response.json()
            # Structure simplifiée pour l'exemple
            definition = data[0]['meanings'][0]['definitions'][0]['definition']
            return definition
    except Exception:
        pass
    return "Définition non disponible."
