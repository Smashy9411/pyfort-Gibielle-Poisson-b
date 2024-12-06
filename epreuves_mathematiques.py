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

def epreuve_roulette_mathematique():
    """
    Parametres : /
    sortie : Booléen
    rôle : Demande au joueur de réaliser un calcul de 5 entier aléatoire, avec une opération choisie
    aléatoirement entre la soustraction, la multiplication et l'addition. Si le résultat est bon, retourne Vrai sinon retourne Faux.
    """
    print("Epreuve de la Roulette")
    n1 = randint(0, 20)
    n2 = randint(0, 20)
    n3 = randint(0, 20)
    n4 = randint(0, 20)
    n5 = randint(0, 20)
    operation = ["+","-","*"]
    type_op = randint(0, 2)
    print("Nombres sur la roulette : ["+str(n1)+","+str(n2)+","+str(n3)+","+str(n4)+","+str(n5)+"]")
    if operation[type_op] == "+":
        print("Calculez le résultat en combinant ces nombres avec une addition")
        resultat1 = n1+n2+n3+n4+n5
        rep1 = int(input("Votre réponse: "))
        if rep1 == resultat1:
            print("Bonne réponse ! Vous avez gagné une clé.")
            return True
        else:
            print("Mauvaise réponse ! La bonne réponse était", resultat1,".")
            return False
    if operation[type_op] == "-":
        print("Calculez le résultat en combinant ces nombres avec une soustraction")
        resultat2 = n1-n2-n3-n4-n5
        rep2 = int(input("Votre réponse: "))
        if rep2 == resultat2:
            print("Bonne réponse ! Vous avez gagné une clé.")
            return True
        else:
            print("Mauvaise réponse ! la bonne réponse était", resultat2,".")
            return False
    if operation[type_op] == "*":
        print("Calculez le résultat en combinant ces nombres avec une multiplication")
        resultat3 = n1*n2*n3*n4*n5
        rep3 = int(input("Votre réponse: "))
        if rep3 == resultat3:
            print("Bonne réponse ! Vous avez gagné une clé.")
            return True
        else:
            print("Mauvaise réponse ! la bonne réponse était", resultat3,".")
            return False