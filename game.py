# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.directions = None
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        history = Command("history"," : aficher l'historique des pièces visitées", Actions.history, 0)
        self.commands["history"] = history
        back = Command("back"," : retourner à la pièce précédente", Actions.back, 0)
        self.commands["back"] = back
        check = Command("check"," : afficher l'inventaire", Actions.check, 0)
        self.commands["check"] = check
        look = Command("look", ": voir les items dans la pièce", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take","prendre un objet de la pièce", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", "poser un objet de l'inventaire dans la pièce", Actions.drop,1)
        self.commands["drop"] = drop
        self.talk = Command("talk", "parler à un personnage", Actions.talk, 1)
        self.commands["talk"] = self.talk
        # Setup rooms

        aeroport = Room("Aeroport", "Le grand aéroport d'Italie, vous observez un individu qui étrangement vous intéresse")
        self.rooms.append(aeroport)
        tramway = Room("Tramway", "un tramway tout a fait banal")
        self.rooms.append(tramway)
        prison = Room("Prison", "la prison où réside Polpo, le chef local de l'association mafieuse Passione")
        self.rooms.append(prison)
        maison = Room("Maison", "un simple appartement, c'est là que vous vivez")
        self.rooms.append(maison)
        QG = Room("QG de l'unité", "un café partenaire de l'organisation, c'est là que vous vous réunissez")
        self.rooms.append(QG)
        centre_ville = Room("Centre Ville", "le coeur de la ville de Naples")
        self.rooms.append(centre_ville)
        eglise_abandonnee = Room("Eglise abandonnée", "TODO")   #TODO
        self.rooms.append(eglise_abandonnee)
        port_naples = Room("Port de Naples", "TODO") #TODO
        self.rooms.append(port_naples)

        # Create exits for rooms

        aeroport.exits = {"N" : tramway, "E" : None, "S" : None, "O" : None , "U" : None , "D" : tramway}
        tramway.exits = {"N" : prison, "E" : QG, "S" : aeroport, "O" : None ,"U" : aeroport , "D" : None}
        prison.exits = {"N" : None, "E" : None, "S" : tramway, "O" : None, "U" : None , "D" : None}
        QG.exits = {"N" : None, "E" : None , "S" :None , "O" : tramway, "U" : None , "D" : None}
        maison.exits = {"N" : None, "E" : None , "S" :None , "O" : None , "U" : None , "D" : None}
        centre_ville.exits = {"N" : None, "E" : None , "S" :None , "O" : None, "U" : None , "D" : None}
        eglise_abandonnee.exits = {"N" : None, "E" : None , "S" :None , "O" : None, "U" : port_naples , "D" : None}
        port_naples.exits = {"N" : None, "E" : None , "S" :None , "O" : None, "U" : None , "D" : eglise_abandonnee}
 
        self.directions = set(["N" , "NORD" , "E" , "EST" , "S" , "SUD" , "O" , "OUEST" , "U" , "UP" , "D" , "DOWN" ])
        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = aeroport

        #setup inventory
        self.player.inventory["sword"]=Item("sword", "epee",4)
        self.player.inventory["bow"] = Item("bow", "arc", 4)
        aeroport.inventory.add(Item("shield", "bouclier", 4))

        #Setup player stat
        self.player.max_weight = 10

        #setup PNJ
        aeroport.characters["Gandalf"] = Character("Gandalf","sorcerer", aeroport, ["tkt"])
        



    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

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
