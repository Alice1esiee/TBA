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
        l=["move", "stay"]
        condition = random.choice(l)
        print(f"{condition}\n")
        if (condition == "stay"):
            return False
        else:
            salles_adj = []
            for salle in self.current_room.exits.values():
                if salle is not None:
                    salles_adj.append(salle)
            next_room = random.choice(salles_adj)
            del self.current_room.characters[self.name]
            self.current_room = next_room
            self.current_room.characters[self.name]=self
            print(f"{self.name} went to {self.current_room.name}\n")
        