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

Ainsi que qu'un fichier `config.py` contenant les configurations du jeu.

## Comment exécuter le programme :

Pour l'exécuter, il faut d'abord ouvrir un terminal, ensuite, exécutez la commande "python game.py" pour pouvoir jouer au jeu.

## Ce qui marche/ce qui marche pas :

L'ensemble des fonctions qui devaient être réalisées pour ce projet fonctionne correctement. 
