from random import randint

def factorielle(n):
    """
    Parametres : n(entier)
    sortie : factorielle de n (entier)
    rôle : Calcul la factorielle de n
    """
    facto = 1
    for i in range(1, n+1):
        facto *= i
    return facto

def epreuve_math_factorielle():
    """
    Parametres : /
    sortie : Booléen
    rôle : Demande au joueur de calculer la factorielle d'un entier n
    entre 1 et 10 et sort Vrai si le joueur a raison et Faux si il n'a pas la bonne réponse
    """
    factorielle_aleatoire = randint(1, 10)
    print("Épreuve de Mathématiques:")
    print("Calculer la factorielle de ",factorielle_aleatoire,".")
    n = int(input("Votre réponse: "))
    bonne_reponse = factorielle(factorielle_aleatoire)
    if n == bonne_reponse:
        print("Correct ! Vous gagnez une clé.")
        return True
    else:
        print("Incorrect ! La bonne réponse était", bonne_reponse,".")
        return False

