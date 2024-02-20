from random import * #importation de la librairie random
from fonctions_pour_motus import* #importation des fonctions d'un autre programme

"""esthétique de début du jeu"""
print("\n","                                ~~Bienvenue sur le jeu Motus!~~")
a=input("Voulez-vous jouez ? ")
if a == "non":
    print("Au revoir")
elif a == "oui" or a == "OUI": #choisis un mot au hasard dans une liste de mot
    mot_fin = mot_aleatoire_dans_liste("rep7.txt")
    mot_random_liste = mot_en_liste(mot_fin)
    
    print("")
    lettres_trouvees = mot_random_liste[0],"","","","","",mot_random_liste[6]
    #affiche le mot random en liste avec la première et deuxième lettres
    print(lettres_trouvees)
    print("")
    
    mot_proposé_liste = []

    """intérieur du jeu"""
    while mot_proposé_liste != mot_random_liste: #s'arrête quand le joueur trouve le mot
        mot_proposé_liste = mot_en_liste(input("Ecrivez un mot en 7 lettres : "))
        
        if len(mot_proposé_liste)< 7:
            print("Il faut un mot de 7 lettres!")
        elif len(mot_proposé_liste)>7 :
            print("Il faut un mot de 7 lettres!")
            print("")
            
        print(lettres_presentes(mot_proposé_liste,mot_random_liste))
        #trouve les lettres présentes dans les deux listes

        mot_proposé_liste  = lettres_presentes(mot_proposé_liste,mot_random_liste)
        lettres_trouvees = union_liste(lettres_presentes(mot_proposé_liste,mot_random_liste), inter_liste(mot_proposé_liste,mot_random_liste))
        #affiche les lettres trouvées au bon endroit
        
        print(lettres_trouvees)
    print("")
    print("Bravo! Vous avez trouvé le mot!")
    print("Le mot était ''",mot_fin,"''")