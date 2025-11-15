from rooms import Rooms

class Green_Room(Rooms):
    def __init__(self, name, image, doors, cost, rarity):
        super().__init__(name, image, doors, cost, rarity)
    
green_rooms = []