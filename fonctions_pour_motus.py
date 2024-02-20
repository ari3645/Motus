# -*- coding: utf-8 -*-

def mot_aleatoire_dans_liste(dico):
    """
    cette fonction prend un fichier de mots en paramètre 
    et retourne un mot pris aléatoirement
    """
    from random import randint
    dicomot = open(dico,"r")
    compteur=0
    for i in dicomot:
        compteur=compteur+1
    dicomot.close()
    nombre = randint(1,compteur)
    dicomot = open(dico,"r")
    compteur=0
    for i in dicomot:
        compteur=compteur+1
        if compteur == nombre:
            mot = i.replace("\n","")
            break
    dicomot.close()
    return(mot)

def mot_en_liste(mot):
    """cette fonction prend une chaine de caractères en paramètre
    et retourne une liste de toutes les lettres du mot en majuscule
    """
    liste = []
    for i in mot:
        liste.append(i.upper())
    return(liste)

def liste_en_mot(liste):
    """cette fonction prend une liste de caractères en paramètre
    et retourne un mot fait des lettres de la liste"""
    mot = ""
    for i in liste:
        mot = mot + i
    return(mot)

def inter_liste(liste1,liste2):
    """cette fonction prend 2 listes en paramètres
    et retourne une liste avec les lettres communes.
    Les deux listes doivent être de même taille
    exemple: ['e', 'm', 'p', 'r', 'u', 'n', 't'] 
    et       ['e', 'n', 't', 'r', 'a', 'n', 't']
    donnent: ['e', '', '', 'r', '', 'n', 't'] """
    liste = []
    for i in range(len(liste1)):
        if liste1[i]==liste2[i]:
            liste.append(liste1[i])
        else:
            liste.append("")
    return(liste)

def union_liste(liste1,liste2):
    """cette fonction prend 2 listes en paramètres
    et retourne une liste avec toutes les lettres des deux listes
    exemple:['p', 'a', ' ', ' ', ' ', ' ', ' ']
    et      ['p', ' ', ' ', ' ', 'i', ' ', ' ']
    donnent ['p', 'a', ' ', ' ', 'i', ' ', ' ']
        """
    liste = []
    for i in range(len(liste1)):
        if liste1[i]==liste2[i]:
            liste.append(liste1[i])
        else:
            liste.append(liste1[i]+liste2[i])
    return(liste)

def met_en_forme_lettres_trouvees(liste):
    """cette fonction prend en paramètre une liste
    et retourne une chaine de caractère 
    en remplaçant les "" par des "_"
    et en remettant les lettres présentes"""
    chaine = " "
    for i in liste:
        if i =="":
            chaine = chaine + "_ "
        else:
            chaine = chaine + i +" "
    return(chaine)
        
def lettres_presentes(liste1,liste2):
    """cette fonction prend deux listes en paramètre
    et retourne une liste avec toutes les lettres de la liste1
    présentes dans la liste2
    les lettres bien placées sont en majuscule
    et les lettres mal placées sont en minuscule"""
    liste1_aro= [] 
    liste2_aro= []
    liste = [] 
    for i in range(len(liste1)):
        if liste1[i]==liste2[i]:
            liste.append(liste1[i]) #liste des lettres biens placées
            liste2_aro.append("@") #liste2 avec des @ à la place des lettres biens placées
            liste1_aro.append("#") #liste2 avec des # à la place des lettres biens placées
        else:
            liste2_aro.append(liste2[i])
            liste1_aro.append(liste1[i])
            liste.append("")    
    for i in range(len(liste2)):
        for j in range(len(liste2)):
            if liste1_aro[i]==liste2_aro[j]:
                liste[i]=liste1_aro[i].lower()
    return(liste)




