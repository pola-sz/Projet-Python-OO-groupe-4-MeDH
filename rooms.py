from abc import ABC, abstractmethod
from inventory import Inventory
import numpy as np

class Rooms(ABC) :
    possible_door_states = ["open","locked","dlocked","none"]
    possible_door_locations = ["N","S","E","W"]
    possible_colors = ["blue","yellow","purple","red","orange","green"]
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
        self.dig_spot = 0
        self.chest = False
        
    @property
    def rarity(self):
        return self.__rarity 
    
    @rarity.setter
    def rarity(self,nbr):
        if not isinstance(nbr,int):
            raise TypeError("rarity is not an integer")
        if not (0 <= nbr <=3):
            raise ValueError("rarity level is not acceptable")
        self.__rarity = nbr
    
  

    @abstractmethod
    def apply_effects(self, input : dict) : 
        """
        Apply the effects of the room

        Args:
            input (dict): current input

        Returns:
            dict : new input
        """
        pass

    def random_item_spawn(self,inventory : Inventory):
        """
        Generate items in a room when called

        Args:
            inventory (Inventory): _description_
        """
        if np.random.rand() < inventory.coins_chance:
            inventory.coins += 1
        if np.random.rand() < inventory.gems_chance:
            inventory.gems += 1
        if np.random.rand() < inventory.keys_chance:
            inventory.keys += 1
        if np.random.rand() < inventory.dices_chance:
            inventory.dices += 1
        if np.random.rand() < inventory.object_list.shovel_chance and 'shovel' in Rooms.item_options:
            inventory.object_list.shovel = True
            Rooms.item_options.remove('shovel')
        if np.random.rand() < inventory.object_list.hammer_chance and 'hammer' in Rooms.item_options:
            inventory.object_list.hammer = True
            Rooms.item_options.remove('hammer')
        if np.random.rand() < inventory.object_list.crochet_kit_chance and 'crochet_kit' in Rooms.item_options:
            inventory.object_list.crochet_kit = True
            Rooms.item_options.remove('crochet_kit')
        if np.random.rand() < inventory.object_list.metal_detector_chance and 'metal_detector' in Rooms.item_options:
            inventory.object_list.metal_detector = True
            Rooms.item_options.remove('metal_detector')
