from fonctions_pour_motus import*
from tkinter import*

fen = Tk()
fen.title("Motus")
fen.geometry("500x600")

Affichage = Label(fen,text='Bienvenue sur le jeu Motus!')
Affichage.place(x=175,y=10)

Affichage = Label(fen,text='Entrez un mot?')
Affichage.place(x=205,y=50)

sais1 = Entry(fen)
sais1.place(x=180,y=70)

mot_fin = mot_aleatoire_dans_liste("rep7.txt")
mot_random_liste = mot_en_liste(mot_fin)
lettres_trouvees = mot_random_liste[0],"","","","","",mot_random_liste[6]

Affichage = Label(fen,text = lettres_trouvees)
Affichage.place(x=210,y=30)

def reponse ():
    mot_prop = sais1.get()
    affichage2 = Label(fen,text = "lettres présentes :" + lettres_presentes(mot_prop,mot_random_liste))
    affichage2.place(x=210,y=90)
        
boutonrep = Button(fen, text='Entrez', command=reponse)
boutonrep.place(x=310,y=65)




fen.mainloop()