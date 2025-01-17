# Description: Game class
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from config import *

win_room = "Port de Naples"
class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.directions = None
        self.weakness_fight = dict()
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)",
                      Actions.go, 1)
        self.commands["go"] = go
        history = Command("history"," : afficher l'historique des pièces visitées",
                           Actions.history, 0)
        self.commands["history"] = history
        back = Command("back"," : retourner à la pièce précédente", Actions.back, 0)
        self.commands["back"] = back
        check = Command("check"," : afficher l'inventaire", Actions.check, 0)
        self.commands["check"] = check
        look = Command("look", " : voir les items présent dans la pièce", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take"," : prendre un objet présent dans la pièce", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " : poser un objet de l'inventaire dans la pièce", Actions.drop,1)
        self.commands["drop"] = drop
        self.talk = Command("talk", " : parler à un personnage", Actions.talk, 1)
        self.commands["talk"] = self.talk
        fight = Command("fight"," : engager un combat avec le PNJ/ennemi choisit", Actions.fight , 1)
        self.commands["fight"] = fight
        # Setup rooms

        aeroport = Room("Aéroport de Naples",
                        "Un lieu de passage, où l'agitation des voyageurs"\
                        " se mêle à l'ombre du Vésuve.")
        self.rooms.append(aeroport)
        tramway = Room("Tramway de Naples",
                        "Un serpent d'acier qui serpente à travers les rues animées,"\
                        " un mélange chaotique de klaxons et de conversations.")
        self.rooms.append(tramway)
        prison = Room("Prison de Naples",
                    "Un bâtiment massif et sombre, chargé de l'odeur de la"\
                    " désolation et de la tristesse.")
        self.rooms.append(prison)
        maison = Room("Maison",
                       "Un petit appartement modeste, avec des murs jaunes "\
                        "et une cour intérieure verdoyante.")
        self.rooms.append(maison)
        QG = Room("QG de l'unité",
                   "Un café discret et élégant, avec un air de mystère. "\
                    "Derrière son ambiance chaleureuse se cache une organisation puissante.")
        self.rooms.append(QG)
        centre_ville = Room("Centre-ville de Naples",
                            "Un labyrinthe de ruelles étroites et colorées, "\
                            "avec des boutiques artisanales et des restaurants traditionnels.")
        self.rooms.append(centre_ville)
        eglise_abandonnee = Room("Église abandonnée",
                                "Un bâtiment religieux délabré, sombre et poussiéreux,"\
                                " avec des bancs en bois pourris et des statues brisées.")
        self.rooms.append(eglise_abandonnee)
        port_naples = Room("Port de Naples",
                            "Un havre de paix pour les pêcheurs, où le parfum de "\
                            "la mer se mêle à l'odeur du poisson frais.") 
        self.rooms.append(port_naples)
        sous_sol = Room("Sous sol de l'église",
                         "description")
        self.rooms.append(sous_sol)
        etage_un = Room("1er etage",
                         "description")
        self.rooms.append(etage_un)
        etage_boss = Room("Etage Boss",
                           "description")
        self.rooms.append(etage_boss)

        # Create exits for rooms

        aeroport.exits = {"N" : None, "E" : None, "S" : tramway, "O" : None ,
                           "U" : None , "D" : None}
        tramway.exits = {"N" : None, "E" : prison, "S" : centre_ville, "O" : None ,
                         "U" : None , "D" : None}
        prison.exits = {"N" : None, "E" : None, "S" : eglise_abandonnee, "O" : tramway ,
                        "U" : None , "D" : None}
        QG.exits = {"N" : None, "E" : port_naples, "S" : None, "O" : None ,
                    "U" : None , "D" : None}
        maison.exits = {"N" : None, "E" : centre_ville, "S" : None, "O" : None ,
                        "U" : None , "D" : None}
        centre_ville.exits = {"N" : tramway, "E" : eglise_abandonnee, "S" : port_naples,
                               "O" : maison ,"U" : None , "D" : None}
        eglise_abandonnee.exits = {"N" : prison, "E" : None, "S" : None, 
                                   "O" : centre_ville ,"U" : etage_un , "D" : sous_sol}
        port_naples.exits = {"N" : centre_ville, "E" : None, "S" : None, 
                             "O" : QG ,"U" : None , "D" : None}
        sous_sol.exits = {"N" : None, "E" : None, "S" : None, "O" : None ,
                          "U" : eglise_abandonnee , "D" : None}
        etage_un.exits = {"N" : None, "E" : None, "S" : None, "O" : None ,
                          "U" : etage_boss , "D" : eglise_abandonnee}
        etage_boss.exits = {"N" : None, "E" : None, "S" : None, "O" : None ,
                            "U" : None , "D" : etage_un}
        
 
        self.directions = set(["N" , "NORD" , "E" , "EST" , "S" , "SUD" , "O" , "OUEST" , "U" , "UP" , "D" , "DOWN" ])
        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = aeroport

        #setup inventory
        fleuret = Item("Fleuret", "Fleuret élégant, idéal pour les duels.", 1)
        port_naples.inventory.add(fleuret)
        pistolet = Item("Pistolet", "Pistolet fiable pour affronter vos adversaires.", 2)
        centre_ville.inventory.add(pistolet)
        arc = Item("Arc", "Arc puissant pour tirer des flèches.", 3)
        eglise_abandonnee.inventory.add(arc)

        #Setup player stat
        self.player.max_weight = 10

        #setup PNJ
        etage_boss.characters["Diavolo"] = Character("Diavolo","Boss", 
                                                    etage_boss, ["Je suis le Boss de Passione !"
                                                    ,"Viens te battre !","Je suis invincible."])
        sous_sol.characters["Doppio"] = Character("Doppio", "Sbire du Boss",
                                                   sous_sol, ["Tu ne peux pas me battre !",
                                                    "Tu ne toucheras pas au Boss.","Pars !"])
        centre_ville.characters["Polnareff"] = Character("Polnareff", "Allie",
                                              centre_ville, ["Je suis ton allie.",
                                                 "Je suis là pour t'aider.",
                                                "Tu dois trouver le mystérieux fleuret pour vaincre le Boss de Passione.",
                                                "Tu trouveras un objet utile au port de Naples."])
        #pnj weakness
        self.weakness_fight["Diavolo"] = fleuret
        self.weakness_fight["Doppio"] = pistolet
        self.weakness_fight["Polnareff"] = pistolet #remettre arc

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    def win(self):
        for elem in self.rooms : 
            if elem.name == "Etage Boss":
                etage_boss = elem
        if etage_boss.characters["Diavolo"].alive == False:
            self.finished = True
            print("bravo, tu as gagné")
    def loss(self):
        if self.player.alive == False:
            self.finished = True
            print("you lost... try again later") 
    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        self.win()
        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            #print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
            print('>')
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
