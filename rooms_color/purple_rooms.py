from rooms import Rooms

class Purple_Room(Rooms):
    def __init__(self, name, image, doors, cost, rarity):
        super().__init__(name, image, doors, cost, rarity)
    
purple_rooms = []