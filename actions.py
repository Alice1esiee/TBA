"""
Module for the actions that the player can perform in the terminal
"""
# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted
# with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"
class Actions:
    """
    This class represents the actions that the player can perform

    Attributes : 
        None
    Methods : 
        go(game, list_of_words, number_of_parameters) = move to a direction
        quit(game, list_of_words, number_of_parameters) = quit the game
        help(game, list_of_words, number_of_parameters) = get help with the
        history(game, list_of_words, number_of_parameters) = get the history of the previous 
        back(game, list_of_words, number_of_parameters) = go back a step
        check(game, list_of_words, number_of_parameters) = check the inventory
        look(game, list_of_words, number_of_parameters) = check the surroundings
        take(game, list_of_words, number_of_parameters) = take an item
        drop(game, list_of_words, number_of_parameters) = drop an item
        talk(game, list_of_words, number_of_parameters) = talk to a npc
        fight(game, list_of_words, number_of_parameters) = fight a npc
    """
    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        liste_pers = [] #liste pleine des persos a deplacer
        for salle in game.rooms:
            if salle.characters:
                for key in salle.characters:
                    liste_pers.append(salle.characters[key])
                    #faire comme en dessous

        for pnj in liste_pers:
            if pnj.name in ("Diavolo", "Polnareff"):
                pass
            elif pnj is not None:
                #pnj.move()
                pass
        #
        #pnj = game.player.current_room.characters.get("Gandalf", None)
        #if pnj is not None :
            #pnj.move()
        #
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1]
        direction = direction.upper()
        if direction not in game.directions :
            print(f"\nDirection {direction} non reconnue")
            return False
        # Move the player in the direction specified by the parameter.
        direction = direction[0]
        player.move(direction)


        return True

    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    @staticmethod
    def history(game, list_of_words, number_of_parameters):
        """
        Prints the player's history

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        game.player.get_history()
        return True

    @staticmethod
    def back(game, list_of_words, number_of_parameters):
        """
        Makes the player go back from 1 step in the rooms he went to
        Args :
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.
        Returns:
            bool: True if the command was executed successfully, False otherwise
        
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        player = game.player
        if len(player.history)==0:
            print("Il n'y a plus de pièce précédente")
            return False
        previous_room=player.history.pop()
        player.current_room = previous_room
        print(player.current_room.get_long_description())
        player.get_history()
        return True

    @staticmethod
    def check(game, list_of_words, number_of_parameters):
        """
        Action function to check the player's inventory
        Args :
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        game.player.get_inventory()
        return True

    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        """
        Action function to check the surroundings of the player
        Args :
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        room = game.player.current_room
        print(room.get_long_description())
        room.get_inventory()
        return True

    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        """
        Action function to take an item of the player's choice in the inventory from the room
        Args :
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        objet = list_of_words[1]
        weight = 0
        for value in game.player.inventory.values():
            weight+=value.weight
        for elem in game.player.current_room.inventory:
            if elem.name.upper() == objet.upper():
                if weight+elem.weight>game.player.max_weight:
                    print(f"L'objet {objet} ne peut être récupéré, la charge est trop élevée.")
                    return False
                game.player.inventory[elem.name] = elem
                game.player.current_room.inventory.remove(elem)
                print(f"L'objet {objet} a été récupéré.")
                return True
        print(f"L'objet {objet} n'est pas présent dans cette salle.")
        return False

    @staticmethod
    def drop(game, list_of_words, number_of_parameters):
        """
        Action function to drop an item from the player's inventory to the room
        Args :
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        objet = list_of_words[1]
        for key in game.player.inventory:
            if key.upper() == objet.upper():
                game.player.current_room.inventory.add(game.player.inventory[key])
                del game.player.inventory[key]
                print(f"L'objet {key} a été retiré de l'iventaire")
                return True
        print(f"L'objet {objet} n'est pas dans votre inventaire")
        return False

    @staticmethod
    def talk(game, list_of_words,number_of_parameters):
        """
        Action function to talk to a NPC chosen by the player
        Args :
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        person = list_of_words[1]
        for key,value in game.player.current_room.characters.items():
            if key.upper() == person.upper():
                value.get_msg()
                return True
        print(f"{person} n'est pas dans la salle")
        return False

    @staticmethod
    def fight(game, list_of_words, number_of_parameters):
        """
        Action to fight a NPC chosen by the player, the outcome depends on weaknesses
        Args :
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        #est ce que le pnj est dans la salle
        ennemy = "dont know yet"
        for nom in game.player.current_room.characters:
            if list_of_words[1].upper() == nom.upper():
                ennemy = nom
        if ennemy == "dont know yet":
            print(f"{list_of_words[1]} n'est pas dans la salle")
            return False

        # verif si le pnj est dans la salle et est vivant
        if game.player.current_room.characters[ennemy].alive is False :
            print(f"{ennemy} est mort")
            return True

        if game.weakness_fight[ennemy] in game.player.inventory.values():
            game.player.current_room.characters[ennemy].alive = False
            print(f"bravo, tu as gagné ton combat contre {ennemy}")
            game.win()
            return True
        print(f"Vous avez perdu, vous n'avez pas l'objet requis pour vaincre {ennemy}")
        game.player.alive = False
        game.loss()
        return False
