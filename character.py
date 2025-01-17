# Define the Character class.
"""
Module to create characters 
"""
import random
from config import DEBUG

class Character:
    """
    class used for the purpose of creating NPCs around the map
    """
    def __init__(self,name,description,current_room,msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
        self.list_msgs = []
        self.alive = True

    def __str__(self):
        return self.name + " : " + self.description

    def move(self):
        """
        class method to make NPCs move around the map
        """
        l=["move", "stay"]
        condition = random.choice(l)
        if DEBUG:
            print(f"{condition}\n")
        if condition == "stay":
            return False

        salles_adj = []
        for salle in self.current_room.exits.values():
            if salle is not None:
                salles_adj.append(salle)
        next_room = random.choice(salles_adj)
        del self.current_room.characters[self.name]
        self.current_room = next_room
        self.current_room.characters[self.name]=self
        if DEBUG:
            print(f"{self.name} went to {self.current_room.name}\n")
        return True

    def get_msg(self):
        """
        prints what the NPC has to say
        """
        if self.alive is False :
            print("...")
            return
        if self.msgs:
            if not self.list_msgs:
                for i in self.msgs:
                    self.list_msgs.append(i)
            print(self.list_msgs.pop(0))
        else:
            print(f"{self.name} n'a rien à dire.")
