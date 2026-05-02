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
            return "".join(c for c in unicodedata.normalize('NFD', word) if unicodedata.category(c) != 'Mn')
    except Exception:
        pass
    return None

def validate_word_online(word):
    """
    Vérifie si le mot existe via Wiktionary avec une méthode ultra-fiable.
    """
    word = word.lower().strip()
    
    # On utilise 'list=search' car c'est la méthode la plus souple de MediaWiki
    # Elle trouve les mots même avec des variations de casse ou d'accents.
    url = f"https://fr.wiktionary.org/w/api.php?action=query&list=search&srsearch=intitle:{word}&srlimit=1&format=json"
    
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            data = response.json()
            search_results = data.get("query", {}).get("search", [])
            
            # Si on a au moins un résultat dont le titre correspond exactement au mot
            # (insensible à la casse car on compare en .lower())
            for result in search_results:
                if result['title'].lower() == word:
                    return True
        
        # Fallback de secours si la recherche intitle échoue (cas rares)
        url_fallback = f"https://fr.wiktionary.org/w/api.php?action=query&titles={word}&redirects=1&format=json"
        resp_fb = requests.get(url_fallback, timeout=2).json()
        if "-1" not in resp_fb.get("query", {}).get("pages", {}):
            return True

    except Exception:
        return True # On autorise si le serveur Wiktionary est en panne
        
    return False

def get_definition(word):
    """Récupère une définition simplifiée via Dictionary API."""
    url = f"https://api.dictionaryapi.dev/api/v2/entries/fr/{word.lower()}"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            data = response.json()
            return data[0]['meanings'][0]['definitions'][0]['definition']
    except Exception:
        pass
    return "Définition disponible sur fr.wiktionary.org"
