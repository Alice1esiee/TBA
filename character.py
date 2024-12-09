# Define the Character class.
import random
class Character:
    
    def __init__(self,name,description,current_room,msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
    
    def __str__(self):
        return self.name + " : " + self.description
    
    def move(self):
        liste = ["aeroport","tramway","prison","QG","maison","centre_ville","eglise_abandonnee","port_naples"]
        room = random.choice(liste)
        if room in self.current_room :
            room.inventory.add(Character)
            room.inventory.remove(Character)
            return True
        else :
            return False
