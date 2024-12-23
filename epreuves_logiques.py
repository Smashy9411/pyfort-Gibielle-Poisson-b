from random import randint

def suivi(joueur):
    suivis = 1
    if suivis == 1:
        print("C'est à votre tour de jouer.")
        suivis = 0
    else:
        print("C'est à votre adversaire de jouer.")
        suivis = 1
    return suivis

def grille_vide():
    grille = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    return grille


def afficher_grille(grille, message):
    if message == "Voici votre grille de jeu avec vos bateaux: ":
        print("Voici votre grille de jeu avec vos bateaux: ")
        print("  +---+---+---+")
        for i, ligne in enumerate(grille):
            ligne_affichee = f"{i+1} |"
            for case in ligne:
                ligne_affichee += f" {case} |"
            print(ligne_affichee)
            print("  +---+---+---+")
        print("    1   2   3")
        print(" ") #laisse un espace antre les lignes d'écriture
    elif message == "Rappel de l'historique des tirs que vous avez effectués : ":
        print("Rappel de l'histoire des tirs que vous avez effectués : ")
        print("  +---+---+---+")
        for i, ligne in enumerate(grille):
            ligne_affichee = f"{i+1} |"
            for case in ligne:
                ligne_affichee += f" {case} |"
            print(ligne_affichee)
            print("  +---+---+---+")
        print("    1   2   3")


def demande_position():
    ligne = int(input("Entrez une ligne entre 1 et 3: "))
    while ligne < 0 or ligne > 3:
        ligne = int(input("Entrez une ligne entre 1 et 3: "))
    colonne = int(input("Entrez une colonne entre 1 et 3: "))
    while colonne < 0 or colonne > 3:
        colonne = int(input("Entrez une colonne entre 1 et 3: "))
    ligne -= 1
    colonne -= 1
    return (ligne, colonne)

def init():
    grille = grille_vide()
    for i in range(2):
        print("Placez votre Bateau", i + 1, "sur la grille: ")
        ligne, colonne = demande_position()
        while grille[ligne][colonne] == "B":
            print("Un bateau est déjà placé ici, veuillez changer de position: ")
            ligne, colonne = demande_position()
        grille[ligne][colonne] = "B"
    afficher_grille(grille, "Voici votre grille de jeu avec vos bateaux: ")
    return grille

def init_adversaire():
    grille = grille_vide()
    for i in range(2):
        ligne2 = randint(0, 2)
        colonne2 = randint(0, 2)
        while grille[ligne2][colonne2] == "B":
            ligne2 = randint(0, 2)
            colonne2 = randint(0, 2)
        grille[ligne2][colonne2] = "B"
    return grille

def tir_aleatoire():
    return (randint(0, 2), randint(0, 2))

grille_tirs_joueur = grille_vide()

grille_adversaire = init_adversaire()

def tour(joueur, grille_tirs_joueur, grille_adversaire):

    if joueur == 0:
        afficher_grille(grille_tirs_joueur, "Rappel de l'historique des tirs que vous avez effectués : ")
        ligne, colonne = demande_position()
    else:
        ligne, colonne = tir_aleatoire()
        print(f"Votre adversaire tire sur la position ({ligne + 1}, {colonne + 1}).")

    while grille_tirs_joueur[ligne][colonne] in ("x", "."):
        if joueur == 0:
            print("Vous avez déjà visé cette position, choisissez une autre.")
            ligne, colonne = demande_position()
        else:
            ligne, colonne = tir_aleatoire()
            print(f"L'adversaire tente une nouvelle position : ({ligne + 1}, {colonne + 1}).")

    if grille_adversaire[ligne][colonne] == "B":
        print("Touché !")
        grille_tirs_joueur[ligne][colonne] = "x"
        grille_adversaire[ligne][colonne] = "x"
    else:
        print("Manqué.")
        grille_tirs_joueur[ligne][colonne] = "."

    if joueur == 0:
        afficher_grille(grille_tirs_joueur, "Voici la grille mise à jour après votre tir : ")



def gagne(grille_tirs_joueur):
    compteur_touches = 0
    for ligne in grille_tirs_joueur:
        compteur_touches += ligne.count('x')

    if compteur_touches == 2:  # Supposons que l'adversaire a 2 bateaux
        return True
    return False




def jeu_bataille_navale():
    print("Bienvenue dans le jeu de Bataille Navale !")
    print("Règles :")
    print("1. Chaque joueur dispose d'une grille 3x3.")
    print("2. Vous devez placer 2 bateaux sur votre grille.")
    print("3. Le but est de toucher les 2 bateaux de l'adversaire avant qu'il ne touche les vôtres.")
    print("Bonne chance !")
    print("-" * 30)

    print("Phase de préparation : Placez vos bateaux !")
    grille_joueur = init()
    print("La grille des bateaux de votre adversaire est en cours de création...")
    grille_adversaire = init_adversaire()

    grille_tirs_joueur = grille_vide()
    grille_tirs_adversaire = grille_vide()

    joueur = 0
    while True:
        if joueur == 0:  # Tour du joueur humain
            print("\nC'est votre tour !")
            afficher_grille(grille_tirs_joueur, "Rappel de l'historique des tirs que vous avez effectués :")
            tour(joueur, grille_tirs_joueur, grille_adversaire)
            if gagne(grille_tirs_joueur):
                print("Félicitations, vous avez coulé tous les bateaux de l'adversaire ! Vous avez gagné !")
                return True
        else:  # Tour du maître du jeu
            print("\nC'est au tour de votre adversaire.")
            tour(joueur, grille_tirs_adversaire, grille_joueur)
            if gagne(grille_tirs_adversaire):
                print("Dommage, votre adversaire a coulé tous vos bateaux. Vous avez perdu !")
                return False

        joueur = 1 - joueur

