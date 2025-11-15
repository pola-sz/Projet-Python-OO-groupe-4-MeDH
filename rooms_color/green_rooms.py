from rooms import Rooms

class Green_Room(Rooms):
    def __init__(self, name, image, doors, cost, rarity):
        super().__init__(name, image, doors, cost, rarity)

class Terrace(Green_Room):
    def __init__(self):
        super().__init__("Terrace", "images/green_rooms/Terrace_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"}, 0, 1)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input
        
class Patio(Green_Room):
    def __init__(self):
        super().__init__("Patio", "images/green_rooms/Patio_Icon.webp",{"N":"open","S":"open","E":"none","W":"open"}, 1, 1)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input

class Courtyard(Green_Room):
    def __init__(self):
        super().__init__("Courtyard", "images/green_rooms/Courtyard_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"}, 1, 1)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input
    
class Coister(Green_Room):
    def __init__(self):
        super().__init__("Coister", "images/green_rooms/Coister_Icon.webp",{"N":"open","S":"open","E":"open","W":"open"}, 3, 2)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input

class Veranda(Green_Room):
    def __init__(self):
        super().__init__("Veranda", "images/green_rooms/Veranda_Icon.webp",{"N":"open","S":"open","E":"none","W":"none"}, 2, 2)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input

class Greenhouse(Green_Room):
    def __init__(self):
        super().__init__("Greenhouse", "images/green_rooms/Greenhouse_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"}, 2, 2)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input

class Morning_Room(Green_Room):
    def __init__(self):
        super().__init__("Morning Room", "images/green_rooms/Morning_Room_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"}, 0, 3)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            inventory.gems += 2
            self.initialisation = False
        return new_input

class Secret_Garden(Green_Room):
    def __init__(self):
        super().__init__("Secret Garden", "images/green_rooms/Secret_Garden_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"}, 0, 3)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input
    
green_rooms = [Terrace(), Patio(), Courtyard(), Coister(), Veranda(), Greenhouse(), Morning_Room(), Secret_Garden()]