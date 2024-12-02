# This file contains the Item class.

class Item:
    """
    This class represents an item. An item is composed of a name, a description and a weight.

    Attributes:
        name (str): The name of the item.
        description (str): The description of the item.
        weight (int): The weight of the item.

    Methods:
        __init__(self, name, description) : The constructor.
        __str__(self) : The string representation of the item.

    Examples:

    >>> sword = Item("sword", "une épée au fil tranchant comme un rasoir", 2)
    >>> print(sword)
    sword : une épée au fil tranchant comme un rasoir (2 kg)
    
    """

    # The constructor.
    def __init__(self, name, description,weight):
        self.name = name
        self.description = description
        self.weight = weight
    
    def __str__(self):
        return self.name + " : " + self.description + " (" + str(self.weight) + " kg)"
    
    