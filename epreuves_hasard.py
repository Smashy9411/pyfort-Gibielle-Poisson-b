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
        reponse = str(input("Votre réponse :"))
        reponse_maj = reponse.upper()

    if reponse_maj == bonneteau_cle:
        print("Trouvé ! Bravo vous gagnez une clé.")
        return True
    else:
        if reponse_maj == "A":
            print("Mauvaise réponse ! il vous reste une tentative.")
            print("     " + "|   |     |   |     ")
            print("    " + "|  B  |   |  C  |   ")
            print("   " + "|       | |       | ")
            reponse = str(input("Votre réponse :"))
            reponse_maj = reponse.upper()
            while reponse_maj not in liste_element:
                reponse = str(input("Votre réponse :"))
        elif reponse_maj == "B":
            print("Mauvaise réponse ! il vous reste une tentative.")
            print("     " + "|   |     |   |     ")
            print("    " + "|  A  |   |  C  |   ")
            print("   " + "|       | |       | ")
            reponse = str(input("Votre réponse :"))
            reponse_maj = reponse.upper()
            while reponse_maj not in liste_element:
                reponse = str(input("Votre réponse :"))
        elif reponse_maj == "C":
            print("Mauvaise réponse ! il vous reste une tentative.")
            print("     " + "|   |     |   |     ")
            print("    " + "|  A  |   |  B  |   ")
            print("   " + "|       | |       | ")
            reponse = str(input("Votre réponse :"))
            reponse_maj = reponse.upper()
            while reponse_maj not in liste_element:
                reponse = str(input("Votre réponse :"))







