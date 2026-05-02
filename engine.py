# -*- coding: utf-8 -*-
import random
from utils import charger_mots, mot_en_liste, comparer_mots
from api_utils import fetch_random_word, validate_word_online, get_definition

class MotusEngine:
    def __init__(self, dictionnaire_path=None, longueur=7, tentatives_max=7, use_api=False, mode_difficulte="Moyen"):
        self.use_api = use_api
        self.taille = longueur
        self.tentatives_max = tentatives_max
        self.tentatives_faites = 0
        self.historique = []
        self.gagne = False
        self.termine = False
        self.dictionnaire_local = set()
        self.definition = None
        self.mode_difficulte = mode_difficulte

        if dictionnaire_path:
            self.dictionnaire_local = set(charger_mots(dictionnaire_path))

        if use_api:
            self.secret = fetch_random_word(longueur)
            if not self.secret:
                self.use_api = False
        
        if not use_api or not self.secret:
            if not self.dictionnaire_local:
                raise ValueError("Aucun dictionnaire disponible.")
            self.secret = random.choice(list(self.dictionnaire_local))
            self.taille = len(self.secret)
        
        self.secret_liste = mot_en_liste(self.secret)
        self.indices_decouverts = ["_"] * self.taille
        if mode_difficulte == "Facile":
            self.indices_decouverts[0] = self.secret[0].upper()
            self.indices_decouverts[-1] = self.secret[-1].upper()
        elif mode_difficulte == "Moyen":
            self.indices_decouverts[0] = self.secret[0].upper()

    def proposer_mot(self, proposition):
        proposition = proposition.upper()
        if len(proposition) != self.taille:
            return "WRONG_SIZE"
            
        # Validation : On accepte si c'est dans le dico local OU si l'API le valide
        est_valide = (proposition in self.dictionnaire_local)
        
        if not est_valide and self.use_api:
            est_valide = validate_word_online(proposition)
        
        if not est_valide:
            return "NOT_IN_DICT"
            
        if self.termine:
            return None
        
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
            if self.use_api: self.definition = get_definition(self.secret)
        elif self.tentatives_faites >= self.tentatives_max:
            self.termine = True
            if self.use_api: self.definition = get_definition(self.secret)
            
        return resultat

    def obtenir_etat(self):
        return {
            "taille": self.taille,
            "tentatives_restantes": self.tentatives_max - self.tentatives_faites,
            "indices_decouverts": self.indices_decouverts,
            "gagne": self.gagne,
            "termine": self.termine,
            "secret": self.secret if self.termine else None,
            "definition": self.definition if self.termine else None
        }
