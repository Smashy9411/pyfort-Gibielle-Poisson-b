from fonctions_utiles import *
from epreuves_mathematiques import epreuve_math
from epreuves_hasard import epreuve_hasard
from epreuve_finale import salle_De_Tresor
from epreuves_logiques import jeu_bataille_navale
from enigme_pere_fouras import enigme_pere_fouras
from enregistrement import *

nb_partie = recuperer_nb_partie()

introduction()
equipe = composer_equipe()

sauvegarder_partie(equipe, nb_partie)

while equipe['Clé remportée(s)'] !=3:
    print("-" * 50)
    print("        Vous possédez actuellement " + str(equipe['Clé remportée(s)']) + " Clé(s)     ")
    print("-" * 50)
    choix = menu_epreuves()
    numero_joueur = choisir_joueur(equipe)
    if choix == 1:
        if epreuve_math():
            equipe[numero_joueur]['Clé récupérée(s)'] += 1
            equipe['Clé remportée(s)'] += 1
            sauvegarder_epreuves(equipe, numero_joueur,"Mathématique", True)
        else:
            sauvegarder_epreuves(equipe, numero_joueur, "Mathématique", False)
    elif choix == 2:
        if jeu_bataille_navale():
            equipe[numero_joueur]['Clé récupérée(s)'] += 1
            equipe['Clé remportée(s)'] += 1
            sauvegarder_epreuves(equipe, numero_joueur, "Logique", True)
        else:
            sauvegarder_epreuves(equipe, numero_joueur, "Logique", False)

    elif choix == 3:
        if epreuve_hasard():
            equipe[numero_joueur]['Clé récupérée(s)'] += 1
            equipe['Clé remportée(s)'] += 1
            sauvegarder_epreuves(equipe, numero_joueur, "Hasard", True)
        else:
            sauvegarder_epreuves(equipe, numero_joueur, "Hasard", False)


    elif choix == 4:
        if enigme_pere_fouras(fichier='data/enigmesPF.json'):
            equipe[numero_joueur]['Clé récupérée(s)'] += 1
            equipe['Clé remportée(s)'] =+ 1
            sauvegarder_epreuves(equipe, numero_joueur, "Père Fouras", True)
        else:
            sauvegarder_epreuves(equipe, numero_joueur, "Père Fouras", False)



print("---------------Épreuve Finale---------------")
print("Bravo tu as réussi à récupérer 3 clés après avoir affronter les différentes épreuves du Fort !!!")
print("")
print("Maintenant, tu vas devoir faire face à la salle du Trésor ! Si tu réussi cette dernière épreuve tu gagneras la partie !!!")
print("")
if salle_De_Tresor():
    print("Bravo !!! Tu as réussi notre épreuve final, tu peux maintenant accéder à l'or de notre Fort !")
    sauvegarder_partie_fini(equipe, nb_partie, True)
else:
    print("Quelle déception... Tu étais si proche du but ! Malheureusement tu t'es planté...")
    sauvegarder_partie_fini(equipe, nb_partie, False)
    print("Si tu veux t'emparer de notre or, tu devras retenter l'expérience et revenir défier le Fort car cette fois il a eu raison de ton équipe...")




