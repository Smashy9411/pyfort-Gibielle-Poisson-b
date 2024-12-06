import random
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

def est_premier(reponse):
    """
    Parametre : entier
    sortie : Booléen
    role : Cela vérifie que le nombre est premier donc renvoie True si il l'est ou False si il ne l'est pas.
    Cela vérifie également qu'il ne soit pas inférieur ou égal a 1


    """

    if reponse <= 1:
        return False
    for i in range(2, int(reponse ** 0.5) + 1):
        if reponse % i == 0:
            return False
    return True

def premier_plus_proche(n):
    """
    Parametre : entier
    sortie : Booléen
    role : Le but est de trouver l'entier premier le plus proche du nombre .
    en utilisant la fonction précèdente, si elle affiche vrai alors le nombre premier ne change pas (stocké dans la variable proche)
    si la fct est_premier() est False alors on utilise une boucle while tant que est_premier est False on ajoute plus 1
    puis on stocke la réponse à la fin du tant que dans proche.

    """

    if est_premier(n) == True:
        proche = n

    else:
        while est_premier(n) == False:
            n += 1
            est_premier(n)
        proche = n
    return proche

def epreuve_math_premier():
    """
    Paramètre : /
    sortie : Booléen
    role : on utilise les fonctions précèdentes pour vérifier que l'utilisateur a mis la bonne réponse pour lui attribuer une clé ou non

    """
    random = randint(10, 20)
    # choisi un nombre entre 10 et 20
    reponse = int(input("Trouver le nombre premier le proche de : {}".format(str(random))))
    print("Votre réponse:", reponse)
    # Saisie l'affichage pour l'utilisateur
    pi = premier_plus_proche(random)

    if reponse == pi:
        print("Correct! Vous avez gagné une clé.")
        return True
    else:
        print("Dommage! Vous avez perdu, vous n'avez pas gagné de clé.")
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


def epreuve_math():
    """
    Paramètre : /
    sortie : fonction
    role: choisi une fonction aléatoirement parmi celle épreuve maths
    """
    alea = random.choice([epreuve_math_premier, epreuve_math_factorielle, epreuve_roulette_mathematique])

    return alea()



