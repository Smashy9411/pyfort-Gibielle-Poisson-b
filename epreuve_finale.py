import json
from random import randint

def chargement_donnees():

    with open("data/indicesSalle.json", 'r', encoding='utf-8') as f:
        donnees = json.load(f)
    liste_mots= []
    for annee in donnees["Fort Boyard"]:
        for mot in donnees["Fort Boyard"][annee]:
            liste_mots.append({"indices":donnees["Fort Boyard"][annee][mot]["Indices"],"MOT-CODE":donnees["Fort Boyard"][annee][mot]["MOT-CODE"]})
    return liste_mots

