class Object : 
    def __init__(self):
        self.shovel = False
        self.hammer = False
        self.lockpick = False
        self.metal_detector = False
        self.rabbit_foot = False
    
    def __str__(self):
        items = []
        if self.shovel:
            items.append("shovel")
        if self.hammer:
            items.append("hammer")
        if self.crochet_kit:
            items.append("lockpick")
        if self.metal_detector:
            items.append("metal detector")
        if self.rabbit_foot:
            items.append("rabbit foot")
        return "".join(items) if items else "empty"


#Please implement an str magic function
# else it's not going to be shown on the screen !!!!