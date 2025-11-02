class Rooms :
    possible_door_states = {"open","locked","dlocked","none"}
    possible_door_locations = {"N","S","E","W"}
    possible_colors = {"blue","yellow","purple","red","orange","green"}

    def __init__(self,color,rarity,doors):
        self.doors = doors
        self.color = color
        self.rarity = rarity
        self.probability = 0
        

    @doors.setter
    def doors(self,portes : dict):
        if not isinstance(portes,dict):
            raise TypeError("These are not dictionaries")
        
        for direction, state in portes.items():
            if direction not in self.possible_door_locations:
                raise ValueError("Direction is not N,S,E,W")
            if state not in self.possible_door_states:
                raise ValueError("State of the door is wrong")
            
        self.__doors = portes

    @color.setter
    def color(self,couleur):
        if not isinstance(couleur,str):
            raise TypeError("Color is not a string")
        if couleur not in self.possible_colors:
            raise ValueError("The color doesn't exist")
        self.__color = couleur

    @rarity.setter
    def rarity(self,nbr):
        if not isinstance(nbr,int):
            raise TypeError("rarity is not an integer")
        if not (0 <= nbr <=3):
            raise ValueError("rarity level is not acceptable")
        self.__rarity = nbr
    
    @property
    def rarity(self):
        return self.__rarity
    
    @probability.setter
    def probability(self,prob):
        if not isinstance(prob,float):
            raise TypeError("Probability is not a float dog")
        self.__probability = prob/(3**self.rarity)


class Green_Room(Rooms):
    def __init__(self, rarity,doors):
        super().__init__("green", rarity,doors)  

class Blue_Room(Rooms):
    def __init__(self, rarity,doors):
        super().__init__("blue", rarity,doors)      

class Yellow_Room(Rooms):
    def __init__(self, rarity,doors):
        super().__init__("yellow", rarity,doors)  

class Purple_Room(Rooms):
    def __init__(self, rarity,doors):
        super().__init__("purple", rarity,doors)  

class Red_Room(Rooms):
    def __init__(self, rarity,doors):
        super().__init__("red", rarity,doors)  

class Orange_Room(Rooms):
    def __init__(self, rarity,doors):
        super().__init__("orange", rarity,doors)    

# for rarity 
# commonplace = 0
# standard = 1
# Unusual = 2
# Rare = 3

All_Green_Rooms = {
    "cloister": Green_Room(2,{"N":"open","S":"open","E":"open","W":"open"}),
    "courtyard": Green_Room(1,{"N":"none","S":"open","E":"open","W":"open"}),
    "greenhouse": Green_Room(1,{"N":"none","S":"open","E":"none","W":"none"}),
    "morning room": Green_Room(3,{"N":"none","S":"open","E":"none","W":"open"}),
    "patio": Green_Room(1,{"N":"none","S":"open","E":"none","W":"open"}),
    "secret garden": Green_Room(3,{"N":"none","S":"open","E":"open","W":"open"}),
    "terrace": Green_Room(1,{"N":"none","S":"open","E":"none","W":"none"}),
    "veranda": Green_Room(2,{"N":"open","S":"open","E":"none","W":"none"})
}