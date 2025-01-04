from fonctions_utiles import *
from epreuves_mathematiques import epreuve_math
from epreuves_hasard import epreuve_hasard
from epreuve_finale import salle_De_Tresor
from epreuves_logiques import jeu_bataille_navale
from enigme_pere_fouras import *
from enregistrement import *

###introduction()
equipe = composer_equipe()


equipe['Clé remportée'] = 0
while equipe['Clé remportée'] !=3:
    print("-" * 50)
    print("        Vous possédez actuellement " + str(equipe['Clé remportée']) + " Clé(s)     ")
    print("-" * 50)
    choix = menu_epreuves()
    numero_joueur = choisir_joueur(equipe)
    if choix == 1:
        epreuve_math()
        if epreuve_math() == True:
            equipe[numero_joueur]['Clé récupérée(s)'] =+ 1
            equipe['Clé remportée(s)'] =+ 1
    if choix == 2:
        jeu_bataille_navale()
        if jeu_bataille_navale() == True:
            equipe[numero_joueur]['Clé récupérée(s)'] =+ 1
            equipe['Clé remportée(s)'] =+ 1
    if choix == 3:
        epreuve_hasard()
        if epreuve_hasard() == True:
            equipe[numero_joueur]['Clé récupérée(s)'] =+ 1
            equipe['Clé remportée(s)'] =+ 1



