from rooms import Rooms

class Orange_Room(Rooms):
    def __init__(self, name, image, doors, cost, rarity):
        super().__init__(name, image, doors, cost, rarity)
    
class Hallway(Orange_Room) : 
    def __init__(self) : 
        super().__init__("Hallway","Rooms & Icons\Orange Rooms\Hallway_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"},0, 0)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input
    
class West_Wing_Hall(Orange_Room) : 
    def __init__(self) : 
        super().__init__("West Wing Hall","Rooms & Icons\Orange Rooms\West_Wing_Hall_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"},0, 1)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input
    
class East_Wing_Hall(Orange_Room) : 
    def __init__(self) : 
        super().__init__("East Wing Hall","Rooms & Icons\Orange Rooms\East_Wing_Hall_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"},0, 2)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input
    
class Corridor(Orange_Room) : 
    def __init__(self) : 
        super().__init__("Corridor","Rooms & Icons\Orange Rooms\Corridor_Icon.webp",{"N":"open","S":"open","E":"none","W":"none"},0, 0)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            map = new_input["map"]
            pos = new_input["player_pos"]
            doors = map[pos[1]][pos[0]].doors
            for i in ["N", "S", "W", "E"]:
                if doors[i] == "locked" or doors[i] == "dlocked" : 
                    doors[i] = "open"
            self.initialisation = False
        return new_input
    
class Passageway(Orange_Room) : 
    def __init__(self) : 
        super().__init__("Passageway","Rooms & Icons\Orange Rooms\Passageway_Icon.webp",{"N":"open","S":"open","E":"open","W":"open"},2, 0)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input

class Secret_Passage(Orange_Room) : 
    def __init__(self) : 
        super().__init__("Secret Passage","Rooms & Icons\Orange Rooms\Secret_Passage_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},1, 2)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input
    
class Foyer(Orange_Room) : 
    def __init__(self) : 
        super().__init__("Foyer","Rooms & Icons\Orange Rooms\Foyer_Icon.webp",{"N":"open","S":"open","E":"none","W":"none"},2, 2)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            map = new_input["map"]
            pos = new_input["player_pos"]
            doors = map[pos[1]][pos[0]].doors
            for i in ["N", "S", "W", "E"]:
                if doors[i] == "locked" or doors[i] == "dlocked" : 
                    doors[i] = "open"
            self.initialisation = False
        return new_input

class Great_Hall(Orange_Room) : 
    def __init__(self) : 
        super().__init__("Great Hall","Rooms & Icons\Orange Rooms\Great_Hall_Icon.webp",{"N":"open","S":"open","E":"open","W":"open"},0, 2)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input
    
orange_rooms = [Hallway(), West_Wing_Hall(), East_Wing_Hall(), Corridor(), Passageway(), Secret_Passage(), Foyer(), Great_Hall()]