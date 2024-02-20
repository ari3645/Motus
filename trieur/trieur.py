#Albin RIVIERE 1G4 13/01/2021 17h38

dicotout= open("liste_mot_francais.txt","r")
taille= int(input("Quelle est la taille des mots souhaités?"))
dicolettre= open('dico7lettre.txt','w')
 
n=0
for i in dicotout:
    n = n+1
dicotout.close()

dicotout2= open("moi.txt","r") 
for i in range (n):
    t=dicotout2.readline().replace("\n","")   
    if len(t)==taille:
        verif= True
        
        for j in t:
            
            if ord(j) >122 or ord(j)<97: 
                verif= False
                
        if verif==True:
            dicolettre.write(t+"\n")
                
dicotout2.close() 
dicolettre.close()
