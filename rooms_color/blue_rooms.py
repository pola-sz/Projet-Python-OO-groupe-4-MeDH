from rooms import Rooms
import numpy as np

class Blue_Room(Rooms):
    def __init__(self, name, image, doors, cost, rarity):
        super().__init__(name, image, doors, cost, rarity)

    
"""ROOM_EVENT_EFFECTS = {
        # Blue
        'Closet': {'items': 2, 'coins': 2},
        'Attic': {'items': 2},
    }"""

class Aquarium(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Aquarium","Rooms & Icons\Blue Rooms\Aquarium_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"},1, 2)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
        return new_input

class Attic(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Attic","Rooms & Icons\Blue Rooms\Attic_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},3 , 3)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
            picked_item = np.random.choice(Rooms.item_options,8)
            for item in picked_item:
                match item:
                    case 'shovel':
                        inventory.object_list.shovel = True
                        Rooms.item_options.remove('shovel')
                    case 'hammer':
                        inventory.object_list.hammer = True
                        Rooms.item_options.remove('hammer')
                    case 'crochet_kit':
                        inventory.object_list.crochet_kit = True
                        Rooms.item_options.remove('crochet_kit')
                    case 'metal_detector':
                        inventory.object_list.metal_detector = True
                        Rooms.item_options.remove('metal_detector')
                        inventory.coins_chance += 0.23
                        inventory.keys_chance += 0.07
                    case 'rabbit_foot':
                        inventory.object_list.rabbit_foot = True
                        Rooms.item_options.remove('rabbit_foot')
                        inventory.coins_chance += 0.1
                        inventory.keys_chance += 0.1
                        inventory.gems_chance += 0.1
                        inventory.dices_chance += 0.1
                        inventory.object_list.shovel_chance += 0.1
                        inventory.object_list.hammer_chance += 0.1
                        inventory.object_list.crochet_kit_chance += 0.1
                        inventory.object_list.metal_detector_chance += 0.1
                    case 'coins':
                        inventory.coins += 1
                    case 'gems':
                        inventory.gems += 1
                    case 'keys':
                        inventory.keys += 1
                    case 'dices':
                        inventory.dices += 1
        return new_input
    
class Ballroom(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Ballroom","Rooms & Icons\Blue Rooms\Ballroom_Icon.webp",{"N":"open","S":"open","E":"none","W":"none"},2, 2)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        inventory.gems = 2
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
        return new_input

class Boiler_Room(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Boiler Room","Rooms & Icons\Blue Rooms\Boiler_Room_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"},1, 2)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
        return new_input
    
class Pantry(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Pantry", "Rooms & Icons\Blue Rooms\Pantry_Icon.webp", {"N":"none","S":"open","E":"none","W":"open"}, 0, 0)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
            food_options = ['apple', 'banana']
            choice = np.random.choice(food_options)
            match choice:
                case 'apple':
                    inventory.object_list.apple += 1
                case 'banana':
                    inventory.object_list.banana += 1
            inventory.coins += 4
            inventory.dices += 1
        return new_input
   
class Den(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Den", "Rooms & Icons\Blue Rooms\Den_Icon.webp", {"N":"none","S":"open","E":"open","W":"open"}, 0, 0)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
            inventory.gems += 1
            inventory.dices += 1
        return new_input
    
class Trophy_room(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Trophy room", "Rooms & Icons\Blue Rooms\Trophy_Room_Icon.webp", {"N":"none","S":"open","E":"none","W":"open"},5, 3)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
            inventory.gems += 8
            #inventory.coins += 5
            inventory.dices += 1
        return new_input
    
class The_Foundation(Blue_Room) : 
    def __init__(self) : 
        super().__init__("The Foundation","Rooms & Icons\Blue Rooms\The_Foundation_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"},0, 3)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
        return new_input
    
class Spare_Room(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Spare Room","Rooms & Icons\Blue Rooms\Spare_Room_Icon.webp",{"N":"open","S":"open","E":"none","W":"none"},0, 0)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
        return new_input

class Rotunda(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Rotunda","Rooms & Icons\Blue Rooms\Rotunda_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"},0, 3)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
        return new_input

class Parlor(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Parlor","Rooms & Icons\Blue Rooms\Parlor_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"},0, 0)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
        return new_input

class Library(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Library","Rooms & Icons\Blue Rooms\Library_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"},0, 2)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
        return new_input
    
class Gallery(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Gallery","Rooms & Icons\Blue Rooms\Gallery_Icon.webp",{"N":"open","S":"open","E":"none","W":"none"},0, 3)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
        return new_input
    
class Music_Room(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Music Room","Rooms & Icons\Blue Rooms\Music_Room_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"},2, 2)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
            inventory.keys += 2
        return new_input
    
class Study(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Study","Rooms & Icons\Blue Rooms\Study_Icon.webp",{"N":"none","S":"open","E":"open","W":"none"},0, 2)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
        return new_input

class Dining_Room(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Dining Room","Rooms & Icons\Blue Rooms\Dining_Room_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"},0, 1)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            chosen_meal = np.random.choice(['cake', 'sandwich', 'dinner'],1)
            match chosen_meal:
                case 'cake':
                    inventory.object_list.cake += 1
                case 'sandwich':
                    inventory.object_list.sandwich += 1
                case 'dinner':
                    inventory.object_list.dinner += 1
            self.initialisation = False
        return new_input

class Locker_Room(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Locker Room","Rooms & Icons\Blue Rooms\Locker_Room_Icon.webp",{"N":"open","S":"open","E":"none","W":"none"},1, 3)

    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
            inventory.keys += 1
        return new_input
    
class Drawing_Room(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Drawing Room","Rooms & Icons\Blue Rooms\Drawing_Room_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"},0, 1)
        
    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
        return new_input

class Freezer(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Freezer","Rooms & Icons\Blue Rooms\Freezer_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},0, 3)
        
    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
        return new_input

class Garage(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Garage","Rooms & Icons\Blue Rooms\Garage_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},0, 2)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
            inventory.keys += 3
        return new_input
    
class Closet(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Closet","Rooms & Icons\Blue Rooms\Closet_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},0, 0)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        chosen_item = np.random.choice(Rooms.item_options,2)
        if self.initialisation :
            self.random_item_spawn(inventory)
            for item in chosen_item:
                match item:
                    case 'shovel':
                        inventory.object_list.shovel = True
                        Rooms.item_options.remove('shovel')
                    case 'hammer':
                        inventory.object_list.hammer = True
                        Rooms.item_options.remove('hammer')
                    case 'crochet_kit':
                        inventory.object_list.crochet_kit = True
                        Rooms.item_options.remove('crochet_kit')
                    case 'metal_detector':
                        inventory.object_list.metal_detector = True
                        Rooms.item_options.remove('metal_detector')
                        inventory.coins_chance += 0.23
                        inventory.keys_chance += 0.07
                    case 'rabbit_foot':
                        inventory.object_list.rabbit_foot = True
                        Rooms.item_options.remove('rabbit_foot')
                        inventory.coins_chance += 0.1
                        inventory.keys_chance += 0.1
                        inventory.gems_chance += 0.1
                        inventory.dices_chance += 0.1
                        inventory.object_list.shovel_chance += 0.1
                        inventory.object_list.hammer_chance += 0.1
                        inventory.object_list.crochet_kit_chance += 0.1
                        inventory.object_list.metal_detector_chance += 0.1
                    case 'coins':
                        inventory.coins += 1
                    case 'gems':
                        inventory.gems += 1
                    case 'keys':
                        inventory.keys += 1
                    case 'dices':
                        inventory.dices += 1
            self.initialisation = False
        return new_input

class Sauna(Blue_Room) : 
    def __init__(self) : 
        super().__init__("Sauna","Rooms & Icons\Blue Rooms\Sauna_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},0, 2)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        inventory = new_input["inventory"]
        if self.initialisation :
            self.random_item_spawn(inventory)
            self.initialisation = False
            inventory.steps += 20
        return new_input

class Antechamber(Blue_Room) : 
    def __init__(self) : 
        super().__init__("antechamber", "Rooms & Icons\Blue Rooms\Antechamber_Icon.webp", {"N":"open","S":"open","E":"open","W":"open"}, 0, 0)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        return new_input

class Entrance(Blue_Room) : 
    def __init__(self) : 
        super().__init__("entrance", "Rooms & Icons\Blue Rooms\Entrance_Hall_Icon.webp", {"N":"open","S":"open","E":"open","W":"open"}, 0, 0)
    
    def apply_effects(self, input : dict):
        new_input = input.copy()
        return new_input



start_room = Entrance()
end_room = Antechamber()
blue_rooms = [Aquarium(),
              Attic(),
              Ballroom(), 
              Boiler_Room(),
              Pantry(),
              Den(),
              Trophy_room(),
              The_Foundation(),
              Spare_Room(),
              Rotunda(),
              Parlor(),
              Ballroom(),
              Library(),
              Gallery(),
              Music_Room(),
              Study(),
              Dining_Room(),
              Locker_Room(),
              Drawing_Room(),
              Freezer(),
              Garage(),
              Closet(),
              Sauna()]
