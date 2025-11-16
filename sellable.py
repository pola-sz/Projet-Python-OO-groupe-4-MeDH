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
        list_object = [inventory.object_list.shovel, 
                       inventory.object_list.hammer,
                       inventory.object_list.crochet_kit,
                       inventory.object_list.metal_detector,
                       inventory.object_list.rabbit_foot,
                       inventory.object_list.apple,
                       inventory.object_list.banana,
                       inventory.object_list.cake,
                       inventory.object_list.sandwich,
                       inventory.object_list.dinner,
                       inventory.keys]
        
        if self.index <= 5 : 
            list_object[self.index] = True
        else : 
            list_object[self.index] += 1
        
sellable_list = [Sellable(0), Sellable(1), Sellable(2), Sellable(3), Sellable(4), Sellable(5), Sellable(6), Sellable(7),
                 Sellable(8), Sellable(9), Sellable(10)]

def three_objects():
    global sellable_list
    list =  np.random.choice(sellable_list, 3)
    return list.tolist()
