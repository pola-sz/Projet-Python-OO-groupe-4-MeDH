from rooms import Rooms

class Green_Room(Rooms):
    def __init__(self, name, image, doors, cost, rarity):
        super().__init__(name, image, doors, cost, rarity)

class Terrace(Green_Room):
    def __init__(self):
        super().__init__("Terrace", "Rooms & Icons\Green Rooms\Terrace_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"}, 0, 1)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input
        
class Patio(Green_Room):
    def __init__(self):
        super().__init__("Patio", "Rooms & Icons\Green Rooms\Patio_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"}, 1, 1)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input

class Courtyard(Green_Room):
    def __init__(self):
        super().__init__("Courtyard", "Rooms & Icons\Green Rooms\Courtyard_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"}, 1, 1)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input
    
class Cloister(Green_Room):
    def __init__(self):
        super().__init__("Cloister", "Rooms & Icons\Green Rooms\Cloister_Icon.webp",{"N":"open","S":"open","E":"open","W":"open"}, 3, 2)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input

class Veranda(Green_Room):
    def __init__(self):
        super().__init__("Veranda", "Rooms & Icons\Green Rooms\Veranda_Icon.webp",{"N":"open","S":"open","E":"none","W":"none"}, 2, 2)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input

class Greenhouse(Green_Room):
    def __init__(self):
        super().__init__("Greenhouse", "Rooms & Icons\Green Rooms\Greenhouse_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"}, 2, 2)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input

class Morning_Room(Green_Room):
    def __init__(self):
        super().__init__("Morning Room", "Rooms & Icons\Green Rooms\Morning_Room_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"}, 0, 3)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            inventory.gems += 2
            self.initialisation = False
        return new_input

class Secret_Garden(Green_Room):
    def __init__(self):
        super().__init__("Secret Garden", "Rooms & Icons\Green Rooms\Secret_Garden_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"}, 0, 3)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input
    
green_rooms = [Terrace(), Patio(), Courtyard(), Cloister(), Veranda(), Greenhouse(), Morning_Room(), Secret_Garden()]