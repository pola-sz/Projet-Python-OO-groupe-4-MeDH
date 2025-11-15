class Object : 
    def __init__(self):
        self.shovel = False
        self.shovel_chance = 0
        self.hammer = False
        self.hammer_chance = 0
        self.crochet_kit = False
        self.crochet_kit_chance = 0
        self.metal_detector = False
        self.metal_detector_chance = 0
        self.rabbit_foot = False
        self.rabbit_foot_chance = 0
        self.apple = 0
        self.banana = 0
        self.cake = 0
        self.sandwich = 0
        self.dinner = 0
    
    def __str__(self):
        items = []
        if self.shovel:
            items.append("shovel")
        if self.hammer:
            items.append("hammer")
        if self.crochet_kit:
            items.append("crochet kit")
        if self.metal_detector:
            items.append("metal detector")
        if self.rabbit_foot:
            items.append("rabbit foot")
        return "".join(items) if items else "empty"
