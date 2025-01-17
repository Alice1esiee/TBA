# Define the Player class.
class Player():
    """
    This class represents the player in our TBA game.
    
    Attributes:
        name (str): the name that the player chose
        current_room (room): The room that the player is in at the time

    Methods:    
        __init__(self, name): The constructor.
        move(self, direction): Makes the move of the player from a room to an other and return True if this room exists or is available
    
        Examples:
        
    >>> joueur = player('joueur')
    >>> joueur.move('N')
    True
    """

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}
        self.max_weight = 10
        self.alive = True # pour condition de fin
        
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.history.append(self.current_room)
        self.current_room = next_room
        print(self.current_room.get_long_description())
        #self.get_history()
        return True

    def get_history(self):
        print("Vous avez visité :\n")
        if len(self.history) == 0:
            print("pas de pièce précédente \n")
            return
        for i in range (len(self.history)):
            print("\t- "+ self.history[i].description)
        return
    
    def get_inventory(self):
        
        if len(self.inventory)==0:
            print("Votre inventaire est vide.")
            return
        else:
            print("Vous disposez des items suivants :")
            for cle,valeur in self.inventory.items():
                print("\t-", valeur)
            return

    