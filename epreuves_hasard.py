import random
from random import randint

def bonneteau():
    """
    Parametres : /
    sortie : Booléen
    rôle : le joeueur va choisir aléatoirement un des trois bonneteau pour essayer de découvrir la clé et il posède 2 tentatives.
    Si le joueur trouve le clé la fonction retourne True sinon elle retourne False.
    """
    liste_element=["A","B","C"]
    tentative = 2
    print("Bienvenue à l'épreuve des Bonneteaux !")
    print("Les règles sont simples. Vous avez 2 tentatives pour trouver la clé située sous un des trois Bonneteaux que nous allons vous montrer.")
    print("Voici les Bonneteaux :")
    print("      ", end="")
    print("---       " * len(liste_element))
    print("     " + "|   |     |   |     |   |     ")
    print("    "+ "|  A  |   |  B  |   |  C  |   ")
    print("   "+ "|       | |       | |       | ")

    bonneteau_cle=randint(0,2)
    bonneteau_cle = liste_element[bonneteau_cle]
    print("Sous quel bonneteau pensez-vous que la clé se trouve ?")
    reponse = str(input("Votre réponse :"))
    reponse_maj = reponse.upper()
    while reponse_maj not in liste_element:
        print("Veuillez entrer une lettre présente sur les bonneteaux.")
        reponse = str(input("Votre réponse :"))
        reponse_maj = reponse.upper()

    if reponse_maj == bonneteau_cle:
        print("Vous avez trouvé du premier coup ! Bravo vous gagnez une clé.")
        return True
    else:
        if reponse_maj == "A":
            liste_element=["B","C"]
            print("Mauvaise réponse ! il vous reste une tentative.")
            print("     " + " ---       ---       ")
            print("     " + "|   |     |   |     ")
            print("    " + "|  B  |   |  C  |   ")
            print("   " + "|       | |       | ")
            reponse = str(input("Votre réponse :"))
            reponse_maj = reponse.upper()
            while reponse_maj not in liste_element:
                print("Veuillez entrer une lettre présente sur les bonneteaux restants.")
                reponse = str(input("Votre réponse :"))
                reponse_maj = reponse.upper()
            if reponse_maj == bonneteau_cle:
                print("Vous avez trouvé en 2 essais ! Bravo vous gagnez une clé.")
                return True
            else:
                print("Mauvaise réponse, la bonne réponse était le bonneteau", bonneteau_cle)
                return False
        elif reponse_maj == "B":
            liste_element=["A","C"]
            print("Mauvaise réponse ! il vous reste une tentative.")
            print("     " + " ---       ---       ")
            print("     " + "|   |     |   |     ")
            print("    " + "|  A  |   |  C  |   ")
            print("   " + "|       | |       | ")
            reponse = str(input("Votre réponse :"))
            reponse_maj = reponse.upper()
            while reponse_maj not in liste_element:
                reponse = str(input("Votre réponse :"))
                reponse_maj = reponse.upper()
            if reponse_maj == bonneteau_cle:
                print("Vous avez trouvé en 2 essais ! Bravo vous gagnez une clé.")
                return True
            else:
                print("Mauvaise réponse, la bonne réponse était le bonneteau", bonneteau_cle)
                return False
        elif reponse_maj == "C":
            liste_element=["A","B"]
            print("Mauvaise réponse ! il vous reste une tentative.")
            print("     " + " ---       ---       ")
            print("     " + "|   |     |   |     ")
            print("    " + "|  A  |   |  B  |   ")
            print("   " + "|       | |       | ")
            reponse = str(input("Votre réponse :"))
            reponse_maj = reponse.upper()
            while reponse_maj not in liste_element:
                print("Veuillez entrer une lettre présente sur les bonneteaux restants.")
                reponse = str(input("Votre réponse :"))
                reponse_maj = reponse.upper()
            if reponse_maj == bonneteau_cle:
                print("Vous avez trouvé en 2 essais ! Bravo vous gagnez une clé.")
                return True
            else:
                print("Mauvaise réponse, la bonne réponse était le bonneteau", bonneteau_cle)
                return False


def affiche_de(face):
    if face == 1:
        print("-----")
        print("|   |")
        print("| 0 |")
        print("|   |")
        print("-----")
    elif face == 2:
        print("-----")
        print("|  0|")
        print("|   |")
        print("|0  |")
        print("-----")
    elif face == 3:
        print("-----")
        print("|  0|")
        print("| 0 |")
        print("|0  |")
        print("-----")
    elif face == 4:
        print("-----")
        print("|0 0|")
        print("|   |")
        print("|0 0|")
        print("-----")
    elif face == 5:
        print("-----")
        print("|0 0|")
        print("| 0 |")
        print("|0 0|")
        print("-----")
    elif face == 6:
        print("-----")
        print("|0 0|")
        print("|0 0|")
        print("|0 0|")
        print("-----")

def jeu_lance_des():
    essais = 3
    while essais > 0:
        print("Il vous reste", str(essais),"essai(s)")
        input(print("Appuyer sur la touche 'Entrer' pour jouer"))
        de = (randint(1,6), randint(1,6))
        print("Le dé que vous avez lancé est le suivant: ")
        affiche_de(de[0])
        print("Le dé de votre adversaire est le suivant: ")
        affiche_de(de[1])

        if de[0] == 6:
            print("Bravo ! Vous avez battu votre adversaire.")
            print("Vous gagnez une clé !")
            return True
        if de[1] == 6:
            print("Dommage, vous avez perdu.")
            return False
        if de[0]!=6 and de[1]!=6:
            print("Personne n'a obtenu de 6.")
            if essais == 0:
                print("Vous n'avez plus d'essais possible ! Match nul.")
                return False
            essais -= 1
            print("C'est reparti pour un nouvel essai !")

def epreuve_hasard():
    """
    Paramètre : /
    sortie : fonction
    role: choisi une fonction aléatoirement parmi les épreuves de hasard
    """
    alea = random.choice([bonneteau, jeu_lance_des])
    return alea()






