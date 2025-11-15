from abc import ABC, abstractmethod
from inventory import Inventory
import random

class Rooms(ABC) :
    possible_door_states = {"open","locked","dlocked","none"}
    possible_door_locations = {"N","S","E","W"}
    possible_colors = {"blue","yellow","purple","red","orange","green"}

    def __init__(self, name : str, image : str, doors : dict, cost : int, rarity : int):
        """Create a room

        Args:
            name (str): name of the room
            image (str): relative path to the image
            doors (dict): example = {"N":"open","S":"open","E":"open","W":"open"}
            cost (int): cost in gems
            rarity (int): rarity from 0 to 3
        """
        self.name = name
        self.image = image
        self.cost = cost
        self.objects = []
        self.doors = doors
        self.__rarity = rarity
        self.orientation = 0
        

    """@doors.setter
    def doors(self,portes : dict):
        if not isinstance(portes,dict):
            raise TypeError("These are not dictionaries")
        
        for direction, state in portes.items():
            if direction not in self.possible_door_locations:
                raise ValueError("Direction is not N,S,E,W")
            if state not in self.possible_door_states:
                raise ValueError("State of the door is wrong")
            
        self.__doors = portes


    @rarity.setter
    def rarity(self,nbr):
        if not isinstance(nbr,int):
            raise TypeError("rarity is not an integer")
        if not (0 <= nbr <=3):
            raise ValueError("rarity level is not acceptable")
        self.__rarity = nbr
    
    """ 
    @property
    def rarity(self):
        return self.__rarity 
    """
    
    @probability.setter
    def probability(self,prob):
        if not isinstance(prob,float):
            raise TypeError("Probability is not a float dog")
        self.__probability = prob/(3**self.rarity)

    """

    @abstractmethod
    def create_objects(self) : 
        pass


class Green_Room(Rooms):
    def __init__(self, name, image, doors, cost, rarity):
        super().__init__(name, image, doors, cost, rarity)
    def create_objects(self) : 
        pass

class Blue_Room(Rooms):
    def __init__(self, name, image, doors, cost, rarity):
        super().__init__(name, image, doors, cost, rarity)
    def create_objects(self) : 
        pass

class Yellow_Room(Rooms):
    def __init__(self, name, image, doors, cost, rarity):
        super().__init__(name, image, doors, cost, rarity)
    def create_objects(self) : 
        pass

class Purple_Room(Rooms):
    def __init__(self, name, image, doors, cost, rarity):
        super().__init__(name, image, doors, cost, rarity)
    def create_objects(self) : 
        pass

class Red_Room(Rooms):
    def __init__(self, name, image, doors, cost, rarity):
        super().__init__(name, image, doors, cost, rarity)
    def create_objects(self) : 
        pass

    def create_objects(self) : 
        pass

class Orange_Room(Rooms):
    def __init__(self, name, image, doors, cost, rarity):
        super().__init__(name, image, doors, cost, rarity)
    def create_objects(self) : 
        pass
    

# for rarity 
# commonplace = 0
# standard = 1
# Unusual = 2
# Rare = 3

def create_room(start = False, end = False):
    global start_end_room
    global rooms
    if start : 
        return start_end_room[0]
    elif end : 
        return start_end_room[1]
    else : 
        r = random.randint(0, len(rooms) - 1)
        return rooms.pop(r)

    
start_end_room = [Blue_Room("entrance", "Rooms & Icons\Blue Rooms\Entrance_Hall_Icon.webp", {"N":"open","S":"open","E":"open","W":"open"}, 0, 0),
                  Blue_Room("antechamber", "Rooms & Icons\Blue Rooms\Antechamber_Icon.webp", {"N":"open","S":"open","E":"open","W":"open"}, 0, 0)

]
rooms = [
    # Blue Rooms 🟦
    Blue_Room("Pantry", "Rooms & Icons\Blue Rooms\Pantry_Icon.webp", {"N":"none","S":"open","E":"none","W":"open"}, 0, 0),
    Blue_Room("Den", "Rooms & Icons\Blue Rooms\Den_Icon.webp", {"N":"none","S":"open","E":"open","W":"open"}, 0, 0),
    Blue_Room("Trophy_room", "Rooms & Icons\Blue Rooms\Trophy_Room_Icon.webp", {"N":"none","S":"open","E":"none","W":"open"},0, 3),
    
    Blue_Room("The Foundation","Rooms & Icons\Blue Rooms\The_Foundation_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"},0, 3),
    Blue_Room("Spare Room","Rooms & Icons\Blue Rooms\Spare_Room_Icon.webp",{"N":"open","S":"open","E":"none","W":"none"},0, 0),
    Blue_Room("Rotunda","Rooms & Icons\Blue Rooms\Rotunda_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"},0, 3),
    Blue_Room("Parlor","Rooms & Icons\Blue Rooms\Parlor_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"},0, 0),
    Blue_Room("Ballroom","Rooms & Icons\Blue Rooms\Ballroom_Icon.webp",{"N":"open","S":"open","E":"none","W":"none"},0, 2),
    Blue_Room("Library","Rooms & Icons\Blue Rooms\Library_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"},0, 2),
    
    Blue_Room("Gallery","Rooms & Icons\Blue Rooms\Gallery_Icon.webp",{"N":"open","S":"open","E":"none","W":"none"},0, 3),
    Blue_Room("Music Room","Rooms & Icons\Blue Rooms\Music_Room_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"},0, 2),
    Blue_Room("Study","Rooms & Icons\Blue Rooms\Study_Icon.webp",{"N":"none","S":"open","E":"open","W":"none"},0, 2),
    Blue_Room("Dining Room","Rooms & Icons\Blue Rooms\Dining_Room_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"},0, 1),
    Blue_Room("Locker Room","Rooms & Icons\Blue Rooms\Locker_Room_Icon.webp",{"N":"open","S":"open","E":"none","W":"none"},0, 3),
    Blue_Room("Drawing Room","Rooms & Icons\Blue Rooms\Drawing_Room_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"},0, 0),
    Blue_Room("Freezer","Rooms & Icons\Blue Rooms\Freezer_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},0, 3),
    Blue_Room("Garage","Rooms & Icons\Blue Rooms\Garage_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},0, 2),
    Blue_Room("Closet","Rooms & Icons\Blue Rooms\Closet_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},0, 0),
    Blue_Room("Sauna","Rooms & Icons\Blue Rooms\Sauna_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},0, 2),
    Blue_Room("Attic","Rooms & Icons\Blue Rooms\Attic_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},0, 3),
    Blue_Room("Boiler Room","Rooms & Icons\Blue Rooms\Boiler_Room_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"},1, 2),
    # Green Rooms 🟩
    Green_Room("Cloister", "Rooms & Icons\Green Rooms\Cloister_Icon.webp", {"N":"open","S":"open","E":"open","W":"open"}, 3, 0),
    Green_Room("Courtyard", "Rooms & Icons\Green Rooms\Courtyard_Icon.webp", {"N":"none","S":"open","E":"open","W":"open"}, 1, 0),
    Green_Room("Greenhouse", "Rooms & Icons\Green Rooms\Greenhouse_Icon.webp", {"N":"none","S":"open","E":"none","W":"none"}, 1, 0),
    Green_Room("Morning Room", "Rooms & Icons\Green Rooms\Morning_Room_Icon.webp", {"N":"none","S":"open","E":"none","W":"open"}, 0, 0),
    Green_Room("Patio", "Rooms & Icons\Green Rooms\Patio_Icon.webp", {"N":"none","S":"open","E":"none","W":"open"}, 1, 0),
    Green_Room("Secret Garden", "Rooms & Icons\Green Rooms\Secret_Garden_Icon.webp", {"N":"none","S":"open","E":"open","W":"open"}, 0, 0),
    Green_Room("Terrace", "Rooms & Icons\Green Rooms\Terrace_Icon.webp", {"N":"none","S":"open","E":"none","W":"none"}, -2, 0),
    Green_Room("Veranda", "Rooms & Icons\Green Rooms\Veranda_Icon.webp", {"N":"open","S":"open","E":"none","W":"none"}, 2, 0),
    # Orange Rooms 🟧
    Orange_Room("Corridor", "Rooms & Icons\Orange Rooms\Corridor_Icon.webp", {"N":"open","S":"open","E":"none","W":"none"}, 0, 0),
    Orange_Room("East Wing Hall", "Rooms & Icons\Orange Rooms\East_Wing_Hall_Icon.webp", {"N":"none","S":"open","E":"open","W":"open"}, 0, 0),
    Orange_Room("Foyer", "Rooms & Icons\Orange Rooms\Foyer_Icon.webp", {"N":"open","S":"open","E":"none","W":"none"}, 0, 0),
    Orange_Room("Great Hall", "Rooms & Icons\Orange Rooms\Great_Hall_Icon.webp", {"N":"open","S":"open","E":"open","W":"open"}, 0, 0),
    Orange_Room("Hallway", "Rooms & Icons\Orange Rooms\Hallway_Icon.webp", {"N":"none","S":"open","E":"open","W":"open"}, 0, 0),
    Orange_Room("Passageway", "Rooms & Icons\Orange Rooms\Passageway_Icon.webp", {"N":"open","S":"open","E":"open","W":"open"}, 0, 0),
    Orange_Room("Secret Passage", "Rooms & Icons\Orange Rooms\Secret_Passage_Icon.webp", {"N":"open","S":"open","E":"none","W":"none"}, 0, 0),
    Orange_Room("West Wing Hall", "Rooms & Icons\Orange Rooms\West_Wing_Hall_Icon.webp", {"N":"none","S":"open","E":"open","W":"open"}, 0, 0),
    # Purple Rooms 🟪
    Purple_Room("Bedroom", "Rooms & Icons\Purple Rooms\Bedroom_Icon.webp", {"N":"none","S":"open","E":"none","W":"open"}, 0, 0),
    Purple_Room("Boudoir", "Rooms & Icons\Purple Rooms\Boudoir_Icon.webp", {"N":"none","S":"open","E":"none","W":"open"}, 0, 0),
    Purple_Room("Bunk Room", "Rooms & Icons\Purple Rooms\Bunk_Room_Icon.webp", {"N":"none","S":"open","E":"none","W":"none"}, 0, 0),
    Purple_Room("Guest Bedroom", "Rooms & Icons\Purple Rooms\Guest_Bedroom_Icon.webp", {"N":"none","S":"open","E":"none","W":"none"}, 0, 0),
    Purple_Room("Her Ladyship's Chamber", "Rooms & Icons\Purple Rooms\Her_Ladyship's_Chamber_Icon.webp", {"N":"none","S":"open","E":"none","W":"none"}, 0, 0),
    Purple_Room("Master Bedroom", "Rooms & Icons\Purple Rooms\Master_Bedroom_Icon.webp", {"N":"none","S":"open","E":"none","W":"none"}, 0, 0),
    Purple_Room("Nursery", r"Rooms & Icons\Purple Rooms\Nursery_Icon.webp", {"N":"none","S":"open","E":"none","W":"none"}, 0, 0),
    Purple_Room("Servant's Quarters", "Rooms & Icons\Purple Rooms\Servant's_Quarters_Icon.webp", {"N":"none","S":"open","E":"none","W":"none"}, 0, 0),
    # Red Rooms 🟥
    Red_Room("Archives", "Rooms & Icons\Red Rooms\Archives_Icon.webp", {"N":"open","S":"open","E":"open","W":"open"}, 0, 0),
    Red_Room("Chapel", "Rooms & Icons\Red Rooms\Chapel_Icon.webp", {"N":"none","S":"open","E":"open","W":"open"}, 0, 0),
    Red_Room("Darkroom", "Rooms & Icons\Red Rooms\Darkroom_Icon.webp", {"N":"none","S":"open","E":"open","W":"open"}, 0, 0),
    Red_Room("Furnace", "Rooms & Icons\Red Rooms\Furnace_Icon.webp", {"N":"none","S":"open","E":"none","W":"none"}, 0, 0),
    Red_Room("Gymnasium", "Rooms & Icons\Red Rooms\Gymnasium_Icon.webp", {"N":"none","S":"open","E":"open","W":"open"}, 0, 0),
    Red_Room("Lavatory", "Rooms & Icons\Red Rooms\Lavatory_Icon.webp", {"N":"none","S":"open","E":"none","W":"none"}, 0, 0),
    Red_Room("Maid's Chamber", "Rooms & Icons\Red Rooms\Maid's_Chamber_Icon.webp", {"N":"none","S":"open","E":"none","W":"open"}, 0, 0),
    Red_Room("Weight Room", "Rooms & Icons\Red Rooms\Weight_Room_Icon.webp", {"N":"open","S":"open","E":"open","W":"open"}, 0, 0),
    # Yellow Rooms 🟨
    Yellow_Room("Bookshop", "Rooms & Icons\Yellow Rooms\Bookshop_Icon.webp", {"N":"none","S":"open","E":"none","W":"open"}, 0, 0),
    Yellow_Room("Commissary", "Rooms & Icons\Yellow Rooms\Commissary_Icon.webp", {"N":"none","S":"open","E":"none","W":"open"}, 0, 0),
    Yellow_Room("Kitchen", "Rooms & Icons\Yellow Rooms\Kitchen_Icon.webp", {"N":"none","S":"open","E":"none","W":"open"}, 0, 0),
    Yellow_Room("Laundry Room", "Rooms & Icons\Yellow Rooms\Laundry_Room_Icon.webp", {"N":"none","S":"open","E":"none","W":"none"}, 0, 0),
    Yellow_Room("Locksmith", "Rooms & Icons\Yellow Rooms\Locksmith_Icon.webp", {"N":"none","S":"open","E":"none","W":"none"}, 0, 0),
    Yellow_Room("Mount Holly Gift Shop", "Rooms & Icons\Yellow Rooms\Mount_Holly_Gift_Shop_Icon.webp", {"N":"none","S":"open","E":"open","W":"open"}, 0, 0),
    Yellow_Room("Showroom", "Rooms & Icons\Yellow Rooms\Showroom_Icon.webp", {"N":"open","S":"open","E":"none","W":"none"}, 0, 0),
    Yellow_Room("The Armory", "Rooms & Icons\Yellow Rooms\The_Armory_Icon.webp", {"N":"none","S":"open","E":"none","W":"open"}, 0, 0)
]




"""
All_Green_Rooms = {
    "cloister": Green_Room(2,{"N":"open","S":"open","E":"open","W":"open"}),
    "courtyard": Green_Room(1,{"N":"none","S":"open","E":"open","W":"open"}),
    "greenhouse": Green_Room(1,{"N":"none","S":"open","E":"none","W":"none"}),
    "morning room": Green_Room(3,{"N":"none","S":"open","E":"none","W":"open"}),
    "patio": Green_Room(1,{"N":"none","S":"open","E":"none","W":"open"}),
    "secret garden": Green_Room(3,{"N":"none","S":"open","E":"open","W":"open"}),
    "terrace": Green_Room(1,{"N":"none","S":"open","E":"none","W":"none"}),
    "veranda": Green_Room(2,{"N":"open","S":"open","E":"none","W":"none"})
}"""