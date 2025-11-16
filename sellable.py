from inventory import Inventory
from rooms import Rooms
import numpy as np

class Sellable():
    
    def __init__(self, index : int) : 
        """ object_name = ["Shovel", "Hammer", "Crochet kit", "Metal detector", "Rabbit_foot", "Apple", "Banana", "Cake", 
                       "Sandwich", "Dinner", "One key"] """
        object_options = [item for item in Rooms.item_options+Rooms.food_options if item not in ['keys','coins','gems','dices']]
        object_name = object_options + ["one key"]
        price = [10, 10, 10, 10, 10, 1, 2, 5, 8, 10, 5]
        self.index = index
        self.name = object_name[index]
        self.price = price[index]

    def use_object(self, inventory : Inventory) : 
        """
        Put the bought object into the inventory

        Args:
            inventory (Inventory): current inventory

        Returns:
            Inventory: updated inventory
        """
        match self.index : 
            case 0 : 
                inventory.object_list.shovel = True
                inventory.coins -= self.price
                if 'shovel' in Rooms.item_options:
                    Rooms.item_options.remove('shovel')
            case 1 : 
                inventory.object_list.hammer = True
                inventory.coins -= self.price
                if 'hammer' in Rooms.item_options:
                    Rooms.item_options.remove('hammer')
            case 2 : 
                inventory.object_list.crochet_kit = True
                inventory.coins -= self.price
                if 'crochet_kit' in Rooms.item_options:
                    Rooms.item_options.remove('crochet_kit')
            case 3 : 
                inventory.object_list.metal_detector = True
                inventory.coins -= self.price
                if 'metal_detector' in Rooms.item_options:
                    Rooms.item_options.remove('metal_detector')
            case 4 : 
                inventory.object_list.rabbit_foot = True
                inventory.coins -= self.price
                if 'rabbit_foot' in Rooms.item_options:
                    Rooms.item_options.remove('rabbit_foot')
            case 5 : 
                inventory.object_list.apple += 1
                inventory.coins -= self.price
            case 6 : 
                inventory.object_list.banana += 1
                inventory.coins -= self.price
            case 7 : 
                inventory.object_list.cake += 1
                inventory.coins -= self.price
            case 8 : 
                inventory.object_list.sandwich += 1
                inventory.coins -= self.price
            case 9 : 
                inventory.object_list.dinner += 1
                inventory.coins -= self.price
            case 10 : 
                inventory.keys += 1
                inventory.coins -= self.price

        return inventory
        
sellable_list = [Sellable(0), Sellable(1), Sellable(2), Sellable(3), Sellable(4), Sellable(5), Sellable(6), Sellable(7),
                 Sellable(8), Sellable(9), Sellable(10)]


def three_objects():
    """
    Generate a random list of three sellable items

    Returns:
        list: list of 3 sellables
    """
    global sellable_list
    list =  np.random.choice(sellable_list, 3, replace = False)
    return list.tolist()
