# -*- coding: utf-8 -*-
import requests
import random
import unicodedata

def fetch_random_word(length):
    """Récupère un mot aléatoire via l'API Heroku et retire les accents."""
    url = f"https://random-word-api.herokuapp.com/word?lang=fr&length={length}&number=1"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            word = response.json()[0].upper()
            # On retire les accents pour que le joueur puisse taper sans accent
            return "".join(c for c in unicodedata.normalize('NFD', word) if unicodedata.category(c) != 'Mn')
    except Exception:
        pass
    return None

def validate_word_online(word):
    """
    Vérifie si le mot existe.
    On combine deux méthodes pour être sûr de ne rien rater.
    """
    word = word.lower()
    
    # Methode 1 : Wiktionary API (La plus rapide)
    # On utilise 'titles' ET 'redirects' pour suivre les formes fléchies
    url_wikt = f"https://fr.wiktionary.org/w/api.php?action=query&titles={word}&redirects=1&format=json"
    
    # Methode 2 : Dictionary API (Fallback pour les définitions)
    url_dict = f"https://api.dictionaryapi.dev/api/v2/entries/fr/{word}"

    try:
        # Test Wiktionary
        resp_wikt = requests.get(url_wikt, timeout=2).json()
        pages = resp_wikt.get("query", {}).get("pages", {})
        if "-1" not in pages:
            return True
            
        # Test Dictionary API (si Wiktionary a raté)
        resp_dict = requests.get(url_dict, timeout=2)
        if resp_dict.status_code == 200:
            return True
            
    except Exception:
        # En cas d'erreur réseau, on autorise le mot pour ne pas bloquer le joueur
        return True
        
    return False

def get_definition(word):
    """Récupère une définition."""
    url = f"https://api.dictionaryapi.dev/api/v2/entries/fr/{word.lower()}"
    try:
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            data = response.json()
            return data[0]['meanings'][0]['definitions'][0]['definition']
    except Exception:
        pass
    return "Définition disponible sur https://fr.wiktionary.org/wiki/" + word.lower()
