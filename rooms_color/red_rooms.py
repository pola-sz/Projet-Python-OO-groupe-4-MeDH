from rooms import Rooms

class Red_Room(Rooms):
    def __init__(self, name, image, doors, cost, rarity):
        super().__init__(name, image, doors, cost, rarity)
    
red_rooms = []