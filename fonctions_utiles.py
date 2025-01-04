
def introduction():
    print("-------------Bienvenue dans l'incroyable jeu Fort Boyard !!!-------------")
    print("")
    print("Voici les règles du jeu :")
    print("Pour sortir d'ici, une seule solution : récupérer 3 clés dans différentes épreuves et trouver le mot secret pour débloquer le trésor !")
    print("Tu vas pouvoir constituer ton équipe et défier les dangers du Fort !!!")
    print("")
    print("Alors gare à toi, et bonne chance....")
    print("")


def composer_equipe():
    global est_leader
    equipe = {}
    print("Il est temps de décider qui défiera le Fort !!!")
    while True:
        try:
            nb_joueurs = int(input("Choisi le nombre de personnes qui seront présentes dans ton équipe (entre 1 et 3 personnes): "))
            if nb_joueurs >= 1 and nb_joueurs <= 3:
                break
            else:
                print("Le nombre de joueur(s) doit être compris entre 1 et 3. Essayez encore.")
        except ValueError:
            print("Cette réponse n'est pas valide. Merci de rentrer un nombre de joueur(s) entre 1 et 3.")

    leader_existe = False

    for i in range(nb_joueurs):
        print("|||||Joueur numéro :" + str(i + 1) + "|||||")
        prenom = input("Nom du joueur: ")
        profession = input("Profession du joueur: ")
        leader = False
        while not leader:
            est_leader = input("Ce joueur est-il le leader de l'équipe (oui ou non)? :")
            est_leader = est_leader.lower()
            if est_leader == "oui" or est_leader == "non":
                leader = True
        if est_leader == "oui" and leader_existe == True:
            print("Impossible, Une équipe ne peut avoir qu'un seule leader.")
            est_leader = "non"
        if est_leader == "oui":
            leader_existe = True
        if i == 0:
            joueur1 = {"Nom": prenom, "Profession": profession, "Leader": est_leader, "Clé récupérée(s):": 0}
            equipe[1] = joueur1
        if i == 1:
            joueur2 = {"Nom": prenom, "Profession": profession, "Leader": est_leader, "Clé récupérée(s)": 0}
            equipe[2] = joueur2
        if i == 2:
            joueur3 = {"Nom": prenom, "Profession": profession, "Leader": est_leader, "Clé récupérée(s)": 0}
            equipe[3] = joueur3
    if not leader_existe:
        print("Tu n'as pas désigné de Leader pour votre équipe ! Le premier joueur sera donc automatiquement le Leader !")
        equipe[1]["Leader"] = "oui"
    equipe["Clé remportée(s)"] = 0
    return equipe

def menu_epreuves():
    print("Tu dois choisir quelle épreuve tu vas réaliser pour remporter des clés et sortir de cet endroit !")
    print("")
    print("Voici les épreuves disponibles dans le Fort !")
    print("")
    print("--1--Épreuve de Mathématiques-----")
    print("--2--Épreuve de logique-----")
    print("--3--Épreuve de hasard-----")
    print("--4--Énigme du Père Fouras-----")
    while True:
        try:
            choix_epreuve = int(input("Indiquer le numéro de l'épreuve choisie: "))
            if choix_epreuve >= 1 and choix_epreuve <= 4:
                break
            else:
                print("Le chiffre doit être compris entre 1 et 4. Essayez encore.")
        except ValueError:
            print("Cette réponse n'est pas valide. Merci de rentrer un chiffre entre 1 et 4.")
    return choix_epreuve

def choisir_joueur(equipe):
    print("Il te faut maintenant choisir un joueur pour défier le Fort dans cette épreuve !")
    print("----CHOIX DU JOUEUR----")

    if len(equipe) == 2:
        print("Tu es seul dans ton équipe. C'est donc à toi de participer !")
        return 1
    else:
        for i in range(1, len(equipe)):
            if equipe[i]["Leader"] == "oui":
                print(str(i),"-" + str(equipe[i]["Nom"]) + " (" + str(equipe[i]["Profession"]) + ") - Leader")
            else:
                print(str(i),"-" + str(equipe[i]["Nom"]) + " (" + str(equipe[i]["Profession"]) + ") - Membre")
        while True:
            try:
                numero_joueur = int(input("Quel joueur va participer à cette épreuve ? :"))
                if numero_joueur >= 1 and numero_joueur < len(equipe):
                    break
                else:
                    print("Le numero du joueur doit être entre 1 et", len(equipe), "Réessayer.")
            except ValueError:
                print("Cette réponse n'est pas valide. Merci de rentrer un chiffre entre 1 et ", len(equipe),".")
    return numero_joueur


