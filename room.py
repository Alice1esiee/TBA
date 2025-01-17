"""
Module used for the creation of rooms in the game
"""

class Room:
    """
    This class represents a room. It is composed by its name, description and its possible exits.

    Attributes:
        name (str): The name of the room.
        descrition (str): The description of what the room contains/looks like.
        exits (dict): The different possible exits that the player can take in the form of key =
         direction (str) and value=room (room)
    
    Methods:
        __init__(self, name, description): The constructor
        get_exit(self, direction): The room in a given direction if it exists
        get_exit_string(self): The string used in the next function to tell the player his 
        possibilities (exits)
        get_long_description(self): Actually builds the string telling the player in which room he 
        is with a descriptipn and what are his possible exits
    Examples:
    """

    # Define the constructor.
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = set()
        self.characters = {}

    # Define the get_exit method.
    def get_exit(self, direction):
        """
        get the exit

        Args 
            self
            direction(str)
        Returns 
            the direction as a str or None
        """

        # Return the room in the given direction if it exists.
        if direction in self.exits:
            return self.exits[direction]
        return None

    # Return a string describing the room's exits.
    def get_exit_string(self):
        """
        returns the exit string for the current place
        Args 
            self
        Returns 
            the exit string
        
        """
        exit_string = "Sorties: "
        for exit in self.exits:
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        """
        Get the long description of the rooms (itself and its exits)
        Args 
            self
        Returns 
            the string for the whole room
        """
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"

    def get_inventory(self):
        """
        Prints the current room's inventory
        Args
            self
        Returns
            nothing, all it does is printing
        """
        pnj = True
        obj = True
        if len(self.inventory)==0:
            obj = False
        if not self.characters:
            pnj = False


        if not( pnj or obj):
            print("Il n'y a rien ici")
        else:
            print("On voit :")
            for objet in self.inventory:
                print("\t-", objet )
            for pnj in self.characters.values():
                if pnj.alive is False:
                    print("\t-", pnj.name,",", "mort")
                else :
                    print("\t-", pnj)
