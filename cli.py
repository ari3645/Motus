# -*- coding: utf-8 -*-
from engine import MotusEngine
from utils import met_en_forme
import os

def choisir_longueur():
    while True:
        choix = input("Choisissez la longueur du mot (2-15) [défaut 7] : ")
        if choix == "":
            return 7
        if choix.isdigit():
            n = int(choix)
            if 2 <= n <= 15:
                return n
        print("Veuillez entrer un nombre entre 2 et 15.")

def trouver_dictionnaire(longueur):
    # Liste des chemins potentiels
    chemins = [
        f"data/dico{longueur}lettre.txt",
        f"Motus/dicolettres/dico{longueur}lettre.txt",
        f"dico{longueur}lettre.txt"
    ]
    for chemin in chemins:
        if os.path.exists(chemin):
            return chemin
    return None

def jouer():
    print("\n=== MOTUS TERMINAL ===")
    
    longueur = choisir_longueur()
    chemin_dico = trouver_dictionnaire(longueur)
    
    if not chemin_dico:
        print(f"Erreur : Aucun dictionnaire trouvé pour {longueur} lettres.")
        return

    try:
        # On donne 6 essais par défaut, ou longueur-1 ? Restons sur 7 pour l'instant.
        jeu = MotusEngine(chemin_dico, tentatives_max=longueur)
    except ValueError as e:
        print(f"Erreur lors du chargement : {e}")
        return

    while True:
        etat = jeu.obtenir_etat()
        print(f"\nIndices : {met_en_forme(etat['indices_decouverts'])}")
        print(f"Essais restants : {etat['tentatives_restantes']}")
        
        prop = input(f"Votre mot ({longueur} lettres) : ").upper()
        res = jeu.proposer_mot(prop)
        
        if res == "WRONG_SIZE":
            print(f"Attention ! Le mot doit faire exactement {longueur} lettres.")
            continue
        elif res == "NOT_IN_DICT":
            print(f"Erreur : Le mot '{prop}' n'existe pas dans le dictionnaire.")
            continue
        elif res:
            print(f"Résultat : {met_en_forme(res)}")
        else:
            print("Action impossible.")
            
        etat = jeu.obtenir_etat()
        if etat["termine"]:
            if etat["gagne"]:
                print(f"\nBRAVO ! Le mot était {etat['secret']}")
            else:
                print(f"\nPERDU... Le mot était {etat['secret']}")
            break

if __name__ == "__main__":
    jouer()
