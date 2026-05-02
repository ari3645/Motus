# -*- coding: utf-8 -*-
import random

def charger_mots(chemin_dico):
    """Charge tous les mots d'un fichier dans une liste."""
    try:
        with open(chemin_dico, "r", encoding="utf-8") as f:
            return [ligne.strip().upper() for ligne in f if ligne.strip()]
    except Exception:
        return []

def mot_aleatoire_dans_liste(chemin_dico):
    """Choisit un mot aléatoirement dans le dictionnaire."""
    mots = charger_mots(chemin_dico)
    return random.choice(mots) if mots else None

def mot_en_liste(mot):
    return list(mot.upper())

def comparer_mots(tentative, secret):
    """Logique de comparaison Motus."""
    taille = len(secret)
    resultat = ["_"] * taille
    secret_disponible = list(secret)
    
    for i in range(taille):
        if tentative[i] == secret[i]:
            resultat[i] = tentative[i]
            secret_disponible[i] = None
            
    for i in range(taille):
        if resultat[i] == "_" :
            if tentative[i] in secret_disponible:
                resultat[i] = tentative[i].lower()
                index_secret = secret_disponible.index(tentative[i])
                secret_disponible[index_secret] = None
    return resultat

def met_en_forme(liste):
    return " ".join(liste)
