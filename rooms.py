from abc import ABC, abstractmethod
from inventory import Inventory
import numpy as np

class Rooms(ABC) :
    possible_door_states = {"open","locked","dlocked","none"}
    possible_door_locations = {"N","S","E","W"}
    possible_colors = {"blue","yellow","purple","red","orange","green"}
    item_options = ['shovel', 'hammer', 'crochet_kit', 'metal_detector', 'rabbit_foot', 'coins', 'gems', 'keys', 'dices']
    food_options = ['apple', 'banana', 'cake', 'sandwich', 'dinner']
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
        self.initialisation = True
        

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

    

    @abstractmethod
    def copy():
        pass"""

    @abstractmethod
    def apply_effects(self, input : dict) : 
        pass

    def random_item_spawn(self,inventory):
        if np.random.rand() < inventory.coins_chance:
            inventory.coins += 1
        if np.random.rand() < inventory.gems_chance:
            inventory.gems += 1
        if np.random.rand() < inventory.keys_chance:
            inventory.keys += 1
        if np.random.rand() < inventory.dices_chance:
            inventory.dices += 1
        if np.random.rand() < inventory.object_list.shovel_chance:
            inventory.object_list.shovel = True
            Rooms.item_options.remove('shovel')
        if np.random.rand() < inventory.object_list.hammer_chance:
            inventory.object_list.hammer = True
            Rooms.item_options.remove('hammer')
        if np.random.rand() < inventory.object_list.crochet_kit_chance:
            inventory.object_list.crochet_kit = True
            Rooms.item_options.remove('crochet_kit')
        if np.random.rand() < inventory.object_list.metal_detector_chance:
            inventory.object_list.metal_detector = True
            Rooms.item_options.remove('metal_detector')
