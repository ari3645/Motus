# -*- coding: utf-8 -*-
from engine import MotusEngine
from utils import met_en_forme
import os

def choisir_mode():
    while True:
        choix = input("Voulez-vous jouer avec l'API en ligne ? (oui/non) : ").lower()
        if choix in ["oui", "o"]: return True
        if choix in ["non", "n"]: return False

def choisir_longueur():
    while True:
        choix = input("Longueur du mot (2-15) [7] : ")
        if choix == "": return 7
        if choix.isdigit() and 2 <= int(choix) <= 15: return int(choix)
        print("Entre 2 et 15 svp.")

def trouver_dictionnaire(longueur):
    chemins = [f"data/dico{longueur}lettre.txt", f"dico{longueur}lettre.txt"]
    for c in chemins:
        if os.path.exists(c): return c
    return None

def jouer():
    print("\n=== MOTUS TERMINAL ELITE (API Edition) ===")
    
    use_api = choisir_mode()
    longueur = choisir_longueur()
    
    chemin_dico = None
    if not use_api:
        chemin_dico = trouver_dictionnaire(longueur)
        if not chemin_dico:
            print("Dictionnaire local introuvable.")
            return

    try:
        jeu = MotusEngine(dictionnaire_path=chemin_dico, longueur=longueur, use_api=use_api)
    except Exception as e:
        print(f"Erreur : {e}")
        return

    while True:
        etat = jeu.obtenir_etat()
        print(f"\nIndices : {met_en_forme(etat['indices_decouverts'])}")
        print(f"Essais : {etat['tentatives_restantes']} restants")
        
        prop = input("> ").upper()
        res = jeu.proposer_mot(prop)
        
        if res == "WRONG_SIZE": print("Taille incorrecte.")
        elif res == "NOT_IN_DICT": print("Mot inconnu.")
        elif res: print(f"Résultat : {met_en_forme(res)}")
        
        etat = jeu.obtenir_etat()
        if etat["termine"]:
            if etat["gagne"]: print(f"\nBRAVO ! Mot : {etat['secret']}")
            else: print(f"\nPERDU... Le mot était {etat['secret']}")
            
            if etat["definition"]:
                print(f"Définition : {etat['definition']}")
            break

if __name__ == "__main__":
    jouer()
