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
    
    # Define the move method.
    def move(self, direction,history):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        self.history.append(self.current_room)
        print(self.current_room.get_long_description())
        for i in range(len(history)):
            print(history[i.get_long_description()])
        print("")
        return True
