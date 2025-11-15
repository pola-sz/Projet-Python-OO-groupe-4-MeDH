from rooms import Rooms

class Yellow_Room(Rooms):
    def __init__(self, name, image, doors, cost, rarity):
        super().__init__(name, image, doors, cost, rarity)

class Commissary(Yellow_Room):
    def __init__(self):
        super().__init__("Commissary", "images/yellow_rooms/Commissary_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"}, 1, 1)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input

class Kitchen(Yellow_Room):
    def __init__(self):
        super().__init__("Kitchen", "images/yellow_rooms/Kitchen_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"}, 1, 0)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input

class Locksmith(Yellow_Room):
    def __init__(self):
        super().__init__("Locksmith", "images/yellow_rooms/Locksmith_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"}, 1, 2)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input
    
class Showroom(Yellow_Room):
    def __init__(self):
        super().__init__("Showroom", "images/yellow_rooms/Showroom_Icon.webp",{"N":"open","S":"open","E":"none","W":"none"}, 2, 3)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input

class Laundry_Room(Yellow_Room):
    def __init__(self):
        super().__init__("Laundry Room", "images/yellow_rooms/Laundry_Room_Icon.webp",{"N":"none","S":"none","E":"none","W":"none"}, 1, 3)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input

class Bookshop(Yellow_Room):
    def __init__(self):
        super().__init__("Bookshop", "images/yellow_rooms/Bookshop_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"}, 1, 3)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input
    
class The_Armory(Yellow_Room):
    def __init__(self):
        super().__init__("The Armory", "images/yellow_rooms/The_Armory_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"}, 0, 1)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input

class Mount_Holly_Gift_Shop(Yellow_Room):
    def __init__(self):
        super().__init__("Mount Holly Gift Shop", "images/yellow_rooms/Mount_Holly_Gift_Shop_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"}, 0, 3)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input

yellow_rooms = [Commissary(), Kitchen(), Locksmith(), Showroom(), Laundry_Room(), Bookshop(), The_Armory(), Mount_Holly_Gift_Shop()]