# -*- coding: utf-8 -*-
import random
from utils import charger_mots, mot_en_liste, comparer_mots

class MotusEngine:
    def __init__(self, dictionnaire_path, tentatives_max=6):
        # On charge tous les mots pour la validation et le choix aléatoire
        self.dictionnaire = set(charger_mots(dictionnaire_path))
        if not self.dictionnaire:
            raise ValueError("Erreur de dictionnaire : aucun mot chargé.")
        
        # Choix du mot secret parmi les mots chargés
        self.secret = random.choice(list(self.dictionnaire))
        self.taille = len(self.secret)
        self.secret_liste = mot_en_liste(self.secret)
        
        self.tentatives_max = tentatives_max
        self.tentatives_faites = 0
        self.historique = []
        self.gagne = False
        self.termine = False
        
        self.indices_decouverts = ["_"] * self.taille
        self.indices_decouverts[0] = self.secret[0].upper()

    def proposer_mot(self, proposition):
        proposition = proposition.upper()
        
        # 1. Vérification de la taille
        if len(proposition) != self.taille:
            return "WRONG_SIZE"
            
        # 2. Vérification de l'existence dans le dictionnaire
        if proposition not in self.dictionnaire:
            return "NOT_IN_DICT"
            
        # 3. Vérification si le jeu est fini
        if self.termine:
            return None
        
        # Logique de jeu normale
        self.tentatives_faites += 1
        prop_liste = mot_en_liste(proposition)
        resultat = comparer_mots(prop_liste, self.secret_liste)
        self.historique.append(resultat)
        
        for i in range(self.taille):
            if resultat[i].isupper():
                self.indices_decouverts[i] = resultat[i]
        
        if proposition == self.secret:
            self.gagne = True
            self.termine = True
        elif self.tentatives_faites >= self.tentatives_max:
            self.termine = True
            
        return resultat

    def obtenir_etat(self):
        return {
            "taille": self.taille,
            "tentatives_restantes": self.tentatives_max - self.tentatives_faites,
            "indices_decouverts": self.indices_decouverts,
            "gagne": self.gagne,
            "termine": self.termine,
            "secret": self.secret if self.termine else None
        }
