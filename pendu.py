import random

def affichage_mot(mot, lettreTrouve):
    
    final = ""
    for i in mot:
        final = final + "*"
        for a in lettreTrouve:
            
            if a == i:
                final = final[:-1]
                final = final + i
                
        
    
    return(final)


rejouer = 1
liste_mot = ["arthur", "chien", "chat", "beau", "moche", "maison", "bouche"]
while rejouer == 1:
    choix = random.randint(0, len(liste_mot))
    motEnCours = ""
    #print(liste_mot[choix])
    lettreTrouve = ["1"]

    while motEnCours != liste_mot[choix]:
        


        #print(liste_mot[choix])


        motEnCours = affichage_mot(str(liste_mot[choix]), lettreTrouve)
        print(motEnCours)
        section = str(input("Dites une lettre: "))
        
        lettreTrouve.append(str(section))
        motEnCours = affichage_mot(str(liste_mot[choix]), lettreTrouve)
    print("bravo vous avez gagné! Encore un partie!")
    rejouer = int(input("1 pour rejouer, 2 pour arreter le programme :"))

#for i in liste_mot[choix]:
  #  if slection == i:

