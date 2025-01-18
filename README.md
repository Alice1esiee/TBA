Matthieu Zozor, Alice Lin 

# TBA

Ce repo contient la version finale du jeu d’aventure TBA.

Les lieux sont au nombre de 11. Il y a trois objets, trois personnages en plus du joueur et des interactions. 


## Structuration

Il y a 7 modules contenant chacun une classe.

- `game.py` / `Game` : description de l'environnement, interface avec le joueur ;
- `room.py` / `Room` : propriétés génériques d'un lieu  ;
- `player.py` / `Player` : le joueur ;
- `command.py` / `Command` : les consignes données par le joueur ;
- `actions.py` / `Action` : les interactions entre le joueur et le jeu ;
- `character` / `Character` : les personnages non joueur ;
- `item` / `Item` : les objets du jeu

Description du contenue:

Le dossier contient 8 fichiers : un Makefile pour compiler plus rapidement les différents programmes, un fichier "arbre_binaires.c" contenant les fonctions destinées à la création des arbres, un fichier "greffe.c" contenant les fonctions liées à la greffe des arbres, et un fichier "saage.c" pour la sauvegarde des données. De plus, le dossier contient les équivalents "greffe.h", "arbre_binaire.h" et "saage.h" pour faire le lien avec les fichiers source (.c) et le Makefile. Enfin, il y a le "main" qui contient le programme principal permettant d'exécuter le projet.


Comment compiler:

Pour compiler, il faut d'abord se rendre dans le dossier contenant toutes les fonctions puis ouvrir un terminal. Ensuite, exécutez la commande "make" pour compiler, et enfin, lancez le programme avec "./main".


Exemple exécution:

./main -E test.saage 
./main -G data/A_1.saage data/B.saage 
./main -G data/A_2.saage data/C.saage 
./main -G data/A_3.saage data/D.saage


Ce qui marche/ce qui marche pas:

L'ensemble des fonctions qui devaient être réalisées pour ce devoir fonctionne correctement. A part expansion qui marche partiellement pour certains arbres greffés.


Problème rencontré :(plus détaillée dans le rapport)

Lors de ce devoir maison, nous avons rencontré quelques problèmes liés au langage de programmation utilisé. Cependant, du point de vue de l'algorithme, la tâche était plus simple.
