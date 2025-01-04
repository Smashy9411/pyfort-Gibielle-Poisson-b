def sauvegarder_partie(equipe, nb_partie, fichier='historique.txt'):
    """
            Paramètre : equipe, noombre de parties et le fichier
            sortie : aucune sortie
            role : créer le tableau de début de partie

            """
    with open(fichier, 'a', encoding="utf-8") as f:
        nb_partie = nb_partie
        f.write("=" * 50+ "\n")
        f.write(f"🏆 Résumé de la partie {nb_partie} 🏆\n")
        f.write("=" * 50 + "\n")
        f.write("Joueur(s) dans l'équipe\n")
        f.write("-" * 50 + "\n")
        f.write(f"{' N°':<8}{'Nom':<13}{'Profession':<23}{'Leader':<0}\n")
        f.write("-" * 50 +"\n")

        for id_joueur in equipe:
            joueur = equipe[id_joueur]
            if isinstance(joueur, dict):
                leader = joueur['Leader']
                f.write(f" {"Id":<6}{joueur['Nom']:<15}{joueur['Profession']:<23}{leader:<0}\n")


def sauvegarder_epreuves(equipe, id_joueur, type_epreuve, resultat, fichier='historique.txt'):
    """
            Paramètre : equipe, id du joueur, type d'épreuve, résultat de l'épreuve et le fichier
            sortie : aucune sortie
            role : créer le tableau pour chaque épreuve

            """
    with open(fichier, 'a', encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write(f"Épreuve de {type_epreuve}\n")
        f.write(f"Joueur : {equipe[id_joueur]['Nom']}\n")
        if resultat:
            f.write(f"Résultat : Gagné\n")
        else:
            f.write(f"Résultat : Perdu\n")
        f.write("=" * 50 + "\n")

def sauvegarder_partie_fini(equipe, nb_partie, victoire, fichier='historique.txt'):
    """
            Paramètre : equipe, nombre de parties, victoire de la partie et le fichier
            sortie : aucune sortie
            role : créer la fin du tableau

            """
    with open(fichier, 'a', encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write(f"🏆 Résultat de la partie {nb_partie} 🏆\n")
        f.write("=" * 50 + "\n")
        f.write(f"{' N°':<8}{'Nom':<13}{'Profession':<23}{'Clé(s)':<0}\n")
        f.write("=" * 50 + "\n")

        for id_joueur in equipe:
            joueur = equipe[id_joueur]
            if isinstance(joueur, dict):
                cle = joueur["Clé récupérée(s)"]
                f.write(f" {"Id":<6}{joueur['Nom']:<15}{joueur['Profession']:<23}{cle:<0}\n")

        f.write("=" * 50 + "\n")
        if victoire:
            f.write("Partie gagnée\n")
            f.write("=" * 50 + "\n")
        else:
            f.write("Partie perdue\n")
            f.write("=" * 50 + "\n")
            f.write("")


def recuperer_nb_partie(fichier='historique.txt'):
    """
            Paramètre : fichier
            sortie : aucune sortie
            role : compte le nombre de parties deja réalisées et ajuste le compteur pour la nouvelle partie

            """
    try:
        with open(fichier, 'r', encoding="utf-8") as f:
            nb_partie = sum(1 for line in f if line.startswith('🏆 Résumé de la partie'))
        return nb_partie + 1
    except FileNotFoundError:
        # Si le fichier n'existe pas encore, cela commence à la partie 1
        return 1






