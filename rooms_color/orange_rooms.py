from rooms import Rooms

class Orange_Room(Rooms):
    def __init__(self, name, image, doors, cost, rarity):
        super().__init__(name, image, doors, cost, rarity)
    
orange_rooms = []