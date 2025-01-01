def sauvegarder_partie(equipe, nb_partie, fichier='historique.txt'):
    with open(fichier, 'a', encoding="utf-8") as f:
        f.write("=" * 50+ "\n")
        f.write("🏆 Résumé de la partie {nb_partie} 🏆\n")
        f.write("=" * 50 + "\n")
        f.write("Joueur(s) dans l'équipe\n")
        f.write("-" * 50 + "\n")
        f.write(f"{' N°':<8}{'Nom':<13}{'Profession':<23}{'Leader':<0}\n")
        f.write("-" * 50 +"\n")

        for i, joueur in equipe.items():
            leader = joueur['Leader']
            f.write(f" {i:<6}{joueur['Nom']:<15}{joueur['Profession']:<23}{leader:<0}\n")


def sauvegarder_epreuves(equipe, nb_partie, id_joueur, type_epreuve, resultat, fichier='historique.txt'):
    with open(fichier, 'w', encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write(f"Épreuve de {type_epreuve}\n")
        f.write(f"Joueur : {id_joueur}\n") ### rajouter equipe[id_joueur]['Nom']
        if resultat:
            f.write(f"Résultat : Gagné\n")
        else:
            f.write(f"Résultat : Perdu\n")
        f.write("=" * 50 + "\n")




joueurs_exemple = {
    1: {'Nom': 'Nico', 'Profession': 'gym', 'Leader': 'oui', 'Clé récupérée': 0},
    2: {'Nom': 'Alex', 'Profession': 'judo', 'Leader': 'non', 'Clé récupérée': 0},
    3: {'Nom': 'Théo', 'Profession': 'karaté', 'Leader': 'non', 'Clé récupérée': 0}
}

sauvegarder_epreuves(
    equipe=joueurs_exemple,
    id_joueur=joueurs_exemple[1]['Nom'],
    nb_partie=1,
    type_epreuve='Mathématique',
    resultat=True,
)
