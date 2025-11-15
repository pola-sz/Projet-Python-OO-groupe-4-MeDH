from rooms import Rooms

class Purple_Room(Rooms):
    def __init__(self, name, image, doors, cost, rarity):
        super().__init__(name, image, doors, cost, rarity)

class Bedroom(Purple_Room) : 
    def __init__(self) : 
        super().__init__("Bedroom","Rooms & Icons\Purple Rooms\Bedroom_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"},2, 1)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        inventory.steps += 2
        if self.initialisation :
            self.initialisation = False
        return new_input

class Boudoir(Purple_Room) : 
    def __init__(self) : 
        super().__init__("Boudoir","Rooms & Icons\Purple Rooms\Boudoir_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"},1, 0)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input

class Guest_Bedroom(Purple_Room) : 
    def __init__(self) : 
        super().__init__("Guest Bedroom","Rooms & Icons\Purple Rooms\Guest_Bedroom_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},1, 1)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        inventory.steps += 2
        if self.initialisation :
            self.initialisation = False
        return new_input
    
class Bunk_room(Purple_Room) : 
    def __init__(self) : 
        super().__init__("Bunk room","Rooms & Icons\Purple Rooms\Bunk_Room_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},0, 1)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            new_input["nb_rooms"] += 1
            self.initialisation = False
        return new_input

class Master_Bedroom(Purple_Room) : 
    def __init__(self) : 
        super().__init__("Guest Bedroom","Rooms & Icons\Purple Rooms\Guest_Bedroom_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},1, 2)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            nb_rooms = new_input["nb_rooms"]
            inventory = new_input["inventory"]
            inventory.steps += nb_rooms
            self.initialisation = False
        return new_input
    


class Servants_Quarters(Purple_Room) : 
    def __init__(self) : 
        super().__init__("Servants Quarters","Rooms & Icons\Purple Rooms\Servant's_Quarters_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},2, 2)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            map = new_input["map"]

            nb_bedrooms = 0
            for i in map : 
                for j in i : 
                    if isinstance(j, Purple_Room) :
                        if isinstance(j, Bunk_room) :
                            nb_bedrooms += 2
                        else : 
                            nb_bedrooms += 1


            inventory = new_input["inventory"]
            inventory.keys += nb_bedrooms
            self.initialisation = False
        return new_input
       
purple_rooms = [Bedroom(),
                Boudoir(),
                Guest_Bedroom(),
                Bunk_room(),
                Master_Bedroom(),
                Servants_Quarters()]