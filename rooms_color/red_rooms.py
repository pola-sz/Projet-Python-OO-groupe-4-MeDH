from rooms import Rooms

class Red_Room(Rooms):
    def __init__(self, name, image, doors, cost, rarity):
        super().__init__(name, image, doors, cost, rarity)

class Lavatory(Red_Room) : 
    def __init__(self) : 
        super().__init__("Lavatory","Rooms & Icons\Red Rooms\Lavatory_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},0, 0)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            self.initialisation = False
        return new_input
    
class Chapel(Red_Room) : 
    def __init__(self) : 
        super().__init__("Chapel","Rooms & Icons\Red Rooms\Chapel_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"},0, 1)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        inventory.coins = max(0, inventory.coins - 1)
        if self.initialisation :
            self.initialisation = False
        return new_input
    
class Gymnasium(Red_Room) : 
    def __init__(self) : 
        super().__init__("Gymnasium","Rooms & Icons\Red Rooms\Gymnasium_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"},0, 1)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        inventory.steps = max(0, inventory.steps - 2)
        if self.initialisation :
            self.initialisation = False
        return new_input

class Weight_Room(Red_Room) : 
    def __init__(self) : 
        super().__init__("Weight Room","Rooms & Icons\Red Rooms\Weight_Room_Icon.webp",{"N":"open","S":"open","E":"open","W":"open"},0, 2)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        if self.initialisation :
            inventory = new_input["inventory"]
            inventory.steps = inventory.steps // 2
            self.initialisation = False
        return new_input
    
red_rooms = [Lavatory(),
             Chapel(),
             Gymnasium(),
             Weight_Room()]