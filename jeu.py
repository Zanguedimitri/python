print("JEU DE PIERRE PAPIER CISEAU TAPER FIN POUR ARRETER LE JEU")
from random import *
machine,joueur=0,0
while True:
    moi = input("c'est à vous de joueur:")
    moi=moi.lower()
    if moi == "fin":
        break
    else:
        while moi not in ("feuille", "ciseau", "pierre"):
            moi = input("vous devez rejoueur:")
        resultat =choice(['papier','ciseau','pierre'])
        if moi == "pierre" and resultat == "ciseau" or moi == "ciseau" and resultat == "papier" or moi == "papier" and resultat == "pierre":
                print("machine:", resultat)
                print("joueur:", moi)
                print("vous remportez le tour")
                joueur +=1
        elif moi == resultat:
                print("machine:",resultat)
                print("joueur:",moi)
                print("personne n'a remporté")
                joueur += 1
                machine += 1
        else:
                print("machine:", resultat)
                print("joueur:", moi)
                print("la machine l'emporte sur vous")
                machine += 1
if joueur < machine:
    print("le vainqueur de la partie est la machine avec ", machine, "victoire")
elif joueur > machine:
    print("vous êtes le vainqueur de la partie avec ", joueur, "victoire")
else:
    print("nous avons un macth nul")