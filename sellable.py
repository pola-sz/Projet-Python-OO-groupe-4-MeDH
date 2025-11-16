from inventory import Inventory
from rooms import Rooms
import numpy as np

class Sellable():
    
    def __init__(self, index : int) : 
        object_name = ["Shovel", "Hammer", "Crochet kit", "Metal detector", "Rabbit_foot", "Apple", "Banana", "Cake", 
                       "Sandwich", "Dinner", "One key"]
        price = [10, 10, 10, 10, 10, 1, 2, 5, 8, 10, 5]
        self.index = index
        self.name = object_name[index]
        self.price = price[index]

    def use_object(self, inventory : Inventory) : 
        match self.index : 
            case 0 : 
                inventory.object_list.shovel = True
            case 1 : 
                inventory.object_list.hammer = True
            case 2 : 
                inventory.object_list.crochet_kit = True
            case 3 : 
                inventory.object_list.metal_detector = True
            case 4 : 
                inventory.object_list.rabbit_foot = True
            case 5 : 
                inventory.object_list.apple += 1
            case 6 : 
                inventory.object_list.banana += 1
            case 7 : 
                inventory.object_list.cake += 1
            case 8 : 
                inventory.object_list.sandwich += 1
            case 9 : 
                inventory.object_list.dinner += 1
            case 10 : 
                inventory.keys += 1

        return inventory
        
sellable_list = [Sellable(0), Sellable(1), Sellable(2), Sellable(3), Sellable(4), Sellable(5), Sellable(6), Sellable(7),
                 Sellable(8), Sellable(9), Sellable(10)]


def three_objects():
    global sellable_list
    list =  np.random.choice(sellable_list, 3, replace = False)
    return list.tolist()
