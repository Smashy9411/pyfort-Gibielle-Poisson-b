import random
import json

def charger_enigmes(fichier):
    """
    Charge les énigmes depuis un fichier JSON.

    :param fichier: Chemin du fichier contenant les énigmes.
    :return: Liste de dictionnaires représentant les énigmes.
    """
    with open(fichier, 'r', encoding='utf-8') as f:
        enigmes = json.load(f)
    return enigmes


def enigme_pere_fouras(fichier='enigmesPF.json'):
    """
    Simule une rencontre avec le Père Fouras où le joueur doit répondre à une énigme.

    :param fichier: Chemin du fichier contenant les énigmes.
    :return: True si le joueur trouve la bonne réponse, False sinon.
    """
    liste_enigmes = charger_enigmes(fichier)

    if not liste_enigmes:
        print("Aucune énigme n'a été chargée.")
        return False

    enigme = random.choice(liste_enigmes)  # Choisir une énigme aléatoire
    question = enigme["question"]
    reponse_attendue = enigme["reponse"].lower()

    print("Le Père Fouras vous pose une énigme")
    print("")
    print(question)
    print("")

    essais_restants = 3

    while essais_restants > 0:
        reponse = input("Votre réponse : ").strip().lower()

        if reponse == reponse_attendue:
            print("")
            print("Bravo ! Vous avez trouvé la bonne réponse et gagné la clé !")
            return True
        else:
            essais_restants -= 1
            if essais_restants > 0:
                print("")
                print(f"Réponse incorrecte. Il vous reste {essais_restants} essai(s).")
            else:
                print("")
                print(f"Vous avez échoué. La réponse correcte était : {enigme['reponse']}")
                return False
