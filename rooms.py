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

    @abstractmethod
    def copy():
        pass


class Green_Room(Rooms):
    def __init__(self, rarity,doors):
        super().__init__("green", rarity,doors) 
    def create_objects(self) : 
        pass

class Blue_Room(Rooms):
    def __init__(self, name, image, doors, cost, rarity):
        super().__init__(name, image, doors, cost, rarity)

    def create_objects(self) : 
        pass

    def copy(self):
        return Blue_Room(self.name, self.image, self.doors.copy(), self.cost, self.rarity)

class Yellow_Room(Rooms):
    def __init__(self, rarity,doors):
        super().__init__("yellow", rarity,doors)  

    def create_objects(self) : 
        pass

class Purple_Room(Rooms):
    def __init__(self, rarity,doors):
        super().__init__("purple", rarity,doors)  

    def create_objects(self) : 
        pass

class Red_Room(Rooms):
    def __init__(self, rarity,doors):
        super().__init__("red", rarity,doors) 

    def create_objects(self) : 
        pass

class Orange_Room(Rooms):
    def __init__(self, rarity,doors):
        super().__init__("orange", rarity,doors)    
    
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
    Blue_Room("Pantry", "Rooms & Icons\Blue Rooms\Pantry_Icon.webp", {"N":"none","S":"open","E":"none","W":"open"}, 0, 0),
    Blue_Room("Den", "Rooms & Icons\Blue Rooms\Den_Icon.webp", {"N":"none","S":"open","E":"open","W":"open"}, 0, 0),
    Blue_Room("Trophy_room", "Rooms & Icons\Blue Rooms\Trophy_Room_Icon.webp", {"N":"none","S":"open","E":"none","W":"open"},3, 3),
    
    Blue_Room("The Foundation","Rooms & Icons\Blue Rooms\The_Foundation_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"},3, 3),
    Blue_Room("Spare Room","Rooms & Icons\Blue Rooms\Spare_Room_Icon.webp",{"N":"open","S":"open","E":"none","W":"none"},0, 0),
    Blue_Room("Rotunda","Rooms & Icons\Blue Rooms\Rotunda_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"},3, 3),
    Blue_Room("Parlor","Rooms & Icons\Blue Rooms\Parlor_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"},0, 0),
    Blue_Room("Ballroom","Rooms & Icons\Blue Rooms\Ballroom_Icon.webp",{"N":"open","S":"open","E":"none","W":"none"},2, 2),
    Blue_Room("Library","Rooms & Icons\Blue Rooms\Library_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"},2, 2),
    
    Blue_Room("Gallery","Rooms & Icons\Blue Rooms\Gallery_Icon.webp",{"N":"open","S":"open","E":"none","W":"none"},3, 3),
    Blue_Room("Music Room","Rooms & Icons\Blue Rooms\Music_Room_Icon.webp",{"N":"none","S":"open","E":"none","W":"open"},2, 2),
    Blue_Room("Study","Rooms & Icons\Blue Rooms\Study_Icon.webp",{"N":"none","S":"open","E":"open","W":"none"},2, 2),
    Blue_Room("Dining Room","Rooms & Icons\Blue Rooms\Dining_Room_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"},1, 1),
    Blue_Room("Locker Room","Rooms & Icons\Blue Rooms\Locker_Room_Icon.webp",{"N":"open","S":"open","E":"none","W":"none"},3, 3),
    Blue_Room("Drawing Room","Rooms & Icons\Blue Rooms\Drawing_Room_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"},0, 0),
    Blue_Room("Freezer","Rooms & Icons\Blue Rooms\Freezer_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},3, 3),
    Blue_Room("Garage","Rooms & Icons\Blue Rooms\Garage_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},2, 2),
    Blue_Room("Closet","Rooms & Icons\Blue Rooms\Closet_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},0, 0),
    Blue_Room("Sauna","Rooms & Icons\Blue Rooms\Sauna_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},2, 2),
    Blue_Room("Attic","Rooms & Icons\Blue Rooms\Attic_Icon.webp",{"N":"none","S":"open","E":"none","W":"none"},3, 3),
    Blue_Room("Boiler Room","Rooms & Icons\Blue Rooms\Boiler_Room_Icon.webp",{"N":"none","S":"open","E":"open","W":"open"},1, 2)
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