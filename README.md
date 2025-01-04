# **Titre du Projet**

## **1. Présentation Générale**

### **Contributeurs :**
- **Gibielle Nicolas** : Responsable de fonctions diverses.
- **Poisson Mathis** : Responsable de fonctions diverses.

### **Description :**
Ce jeu en python reprend l'émission bien connu de Fort Boyard où les invités doivent participer à différentes éprevues pour y gagner des clés et des indices pour réussir l'épreuve final et débloquer le trésor.

### **Fonctionnalités Principales :**
- **[Main.py]** : Corps du jeu qui contient toutes les fonctions importées.  
- **[fonction_utiles]** : Fonctions les plus importantes comme la création de léquipe ou le choix de l'épreuve.  
- **[épreuve_final]** : Dernière épreuve du Fort, elle permet de savoir si le joueur gagne ka partie ou non.  

### **Technologies Utilisées :**
- **Langage principal** : Python
- **Bibliothèques** : Globalement "Random"
- **Outils** : GitHub, Pycharm

### **Installation :**
1. **Cloner le dépôt Git** :  
   ```bash
   git clone https://github.com/utilisateur/projet.git

2. **Installation necessaire**:
- Installer Pycharm
- installer Git
- Connecter les deux pour récupérer le code.

3. **Utilisation**:
- cliquer sur le fichier "main.py" et l'éxécuter.

## **2. Documentation technique**
1. **Algorithme du Jeu**
- Initialisation : Mise en place des paramètres et des variables du jeu.
- Boucle principales : Gére les interactions avec l'utilisateur et les évènements.
- Gestion des scénarios : Vérifie les conditions de victoire ou de défaites.
- Affichage et résultat : Génére la sortie basée sur l'état du jeu.

2. **Fonctions implémentées**
- Epreuve_final:
     - Fonction 1 : def chargee_donnees():
     - Rôle : charge les données du fichier json fourni sur un dictionnaire.
     - Paramètre : jeu_tv (variable ou sera fourni le dictionnaire)
       
     - Fonction 2 : salle_De_Tresor():
     - Rôle : Donne les indices à l'utilisateur et vérifie si la réponse est bonne ou non.
     - Paramètre : reponse (variable ou sera rentrée la réponse du joueur)
                   essai (nombre d'essais restant pour trouver la bonne réponse)
- Epreuve de mathématique:
     - Fonction 1 : def factorielle():
     - Rôle : Calcul la factorielle d'un entier n fourni.
     - Paramètre : facto (variable ou sera calculé la factorielle de n)
       
     - Fonction 2 : def epreuve_math_factorielle():
     - Rôle : demande au joueur de calculer la factorielle d'un entier inconnu n et vérifie la réponse.
     - Paramètre : factorielle_aleatoire (entier donné au joueur pour calculer sa factorielle)
 
     - Fonction 3 : def est_premier():
     - Rôle : vérifie si le nombre est premier.
     - Paramètre : reponse (variable qui contient le nombre a vérifier)
 
     - Fonction 4 : def premier_plus_proche():
     - Rôle : calcule l'entier premier le plus proche.
     - Paramètre : proche (variable qui contient l'entier le plus proche premier)
 
     - Fonction 5 : def epreuve_roulette_mathematique():
     - Rôle : Donne 5 entier au joueur et lui demande de réaliser un calcul puis vérifie sa réponse.
     - Paramètre : n1 à n5 (tout les entiers fourni)
                   resultat (bonne réponse de chaque calcul)

     - Fonction 6 : def epreuve_math():
     - Rôle : Renvoie aléatoirement une épreuve de math au joueur.
     - Paramètre : alea (variable qui contient une épreuve aléatoirement choisie)
 
- Epreuve de hasard:
     - Fonction 1 : def bonneteau():
     - Rôle : Montre 3 bonneteaux au joueur et vérifie si la réponse est valide.
     - Paramètre : bonneteau_cle (variable qui contient le bonneteau à trouver)
 
     - Fonction 2 : def affiche_de():
     - Rôle : Affiche les différentes face d'un dé au joueur.
     - Paramètre : face (variable qui contient la face à afficher)
 
     - Fonction 3 : def jeu_lance_des():
     - Rôle : Donne les essais restants et renvoie au joueur sa victoire ou non.
     - Paramètre : de (variable qui contient les deux faces du dé aléatoirement lancé)
 
     - Fonction 4 : def epreuve_hasard():
     - Rôle : Renvoie une épreuve aléatoirement au joueur.
     - Paramètre : alea (variable qui contient une épreuve aléatoirement choisie)

- Epreuve de logique:
     - Fonction 1 : def suivi():
     - Rôle : Calcul à qui est le tour entre le joueur et l'adversaire.
     - Paramètre : suivis (variable qui oscille entre 1 et 0 pour connaitre quand il faut jouer)
 
     - Fonction 2 : def grille_vide():
     - Rôle : Définie une grille de bataille navale de 3x3 vide.
     - Paramètre : grille (tableau qui contient la grille vide)
 
     - Fonction 3 : def afficher_grille():
     - Rôle : Affiche la grille avec différentes modifications.
     - Paramètre : message (Contient un message qui définira quelle grille dois être affichée)
 
     - Fonction 4 : def demande_position():
     - Rôle : Demande au joueur une position pour pouvoir identifier la case.
     - Paramètre : ligne, colonne (variables qui contiennent les coordonnées)
 
     - Fonction 5 : def init():
     - Rôle : Demande au joueur où va-t-il placer ses bateaux.
     - Paramètre : grille (tableau avec la grille et les bateaux du joueur)
 
     - Fonction 6 : def init_adversaire():
     - Rôle : Charge une grille avec des bateaux aléatoirement positionné pour ceux de l'adversaire.
     - Paramètre : grille (tableau avec la grille et les bateaux de l'adversaire)
 
     - Fonction 7 : def tir_aleatoire():
     - Rôle : Donne des coordonnés aléatoire pour effectuer un tir.
 
     - Fonction 8 : def tour():
     - Rôle : Donne les informations de la partie au joueur.
     - Paramètre : joueur (variable qui contient le tour du joueur ou de l'adversaire)
 
     - Fonction 9 : def gagne():
     - Rôle : Vérifie si l'un des deux joueurs a gagné la partie en détruisant les deux bateaux de l'autre.
     - Paramètre : compteur_touches (variable qui contient le nombres de bateau coulé)
 
     - Fonction 10 : def jeu_bataille_navale():
     - Rôle : Fonction corps du jeu, indique au joueur si il gane ou perd.
 
- Enigme père fouras :


3. **Entrées et Erreurs**:
- Chaque valeur demandés possède un type, si il n'est pas respecté, il indique au joueur que cette réponse n'est pas valide.
- Ajout de la fonction "while True" avec "try" et "Except ValueError".
- Types de bugs connus :
     - Mauvais type pour une fonction ou variable.
     - SyntaxError (Erreur de Syntaxe)
     - IndentationError (Erreur d'Indentation)
     - IndexError (Index Hors Limites)
 
## **3. Journal de bord**

| **Date**             | **Utilisateur**    | **Comentaire**     |
|----------------------|--------------------|--------------------|
| 4 décembre           | Nicolas            | Premiers tests       |
| 5 décembre           | Nicolas            | Ajout des premières fonction |
| 6 décembre           | Nicolas et Mathis  | Fin de l'épreuve Maths |
| 10 décembre          | Nicolas            | Fin de la fonction Harsard |
| 13 décembre          | Nicolas            | modif sur fonction hasard  |
| 20 décembre          | Nicolas            | modif sur fonction hasard  |
| 23 décembre          | Nicolas            | Fin de l'épreuve bataille navale |
| 27 décembre          | Nicolas            | Fin de l'épreuve Final     |
| 30 décembre          | Nicolas            | Fin des fonctions utiles   |
| 2 janvier            | Nicolas            | début de la fonction historique |
| 4 décembre           | Nicolas            | Fin des dernières modifications |

## **4. Bonus réalisés**
- Si l'équipe ne contient qu'un seul joueur, pour les différentes épreuves, le choix du joueur ne sera pas demandé car il est seul.

- Si aucun leader n'a été sélectionné, le jeu définira le premier joueur comme leader automatiquement.

- Lors d'une demande au joueur, si la réponse n'est pas du bon type, au lieu de renvoyer une erreur, elle précisera que cette forme de réponse c'est pas la bonne.

- Ajout de la fonction d'historique des parties dans un fichier historique.txt avec différents paramètres comme le joueur avec le plus de clés récupérées.

  
