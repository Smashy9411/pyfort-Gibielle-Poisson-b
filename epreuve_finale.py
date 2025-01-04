import json
from random import randint

def chargee_donnees():
    """
            Paramètre : /
            sortie : jeu_tv
            role : charge les données du fichier json dans une variable jeu_tv

            """
    with open("data/indicesSalle.json", 'r', encoding='utf-8') as f:
        donnees = json.load(f)
    jeu_tv= []
    for annee in donnees["Fort Boyard"]:
        for mot in donnees["Fort Boyard"][annee]:
            jeu_tv.append(
                {"indices":donnees["Fort Boyard"][annee][mot]["Indices"],
                 "MOT-CODE":donnees["Fort Boyard"][annee][mot]["MOT-CODE"]
                 })
    return jeu_tv

def salle_De_Tresor():
    """
            Paramètre : /
            sortie : booléen
            role : vérifie les réponses du joueur en lui donnant un mot en plus à chaque faute en 3 essais

            """
    liste_mots = chargee_donnees()
    emission = randint(0, len(liste_mots)-1)
    bon_mot = liste_mots[emission]

    essai = 3
    for i in range(3):
        print(bon_mot["indices"][i])
    reponse_correcte = False
    while essai > 0 and reponse_correcte == False:
        print("")
        reponse = input("Quel est le mot à trouver ?")
        reponse = reponse.upper()
        print("")
        if reponse.lower() == bon_mot["MOT-CODE"].lower():
            reponse_correcte = True
        else:
            essai -= 1
            if essai > 0:
                if essai == 2:
                    print("")
                    print("Mauvaise réponse, il te reste", str(essai), "essai(s) ! Voici un indice en plus pour t'aider !")
                    print("")
                    print(bon_mot["indices"][4])
                elif essai == 1:
                    print("")
                    print("Mauvaise réponse, il te reste", str(essai), "essai(s) ! Voici un indice en plus pour t'aider à nouveau !")
                    print("")
                    print(bon_mot["indices"][5])
    if reponse_correcte:
        print("Bravo ! Tu as trouvé le bon mot.")
        print("")
    else:
        print("Dommage ! Tu n'as pas trouvé le bon mot. Le message codé était ", bon_mot["MOT-CODE"], ".")
        print("")
    return reponse_correcte


