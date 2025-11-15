import pygame
from inventory import Inventory
from rooms import Rooms

WIDTH = 80 # Width of a room
HEIGHT = 8 #Height of the player

class GUI : 
    def __init__(self) : 
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 720))
        self.screen.fill("blue")
        self.clock = pygame.time.Clock()
        self.previous = False
        self.previous_key = None

    
    def update_input(self, input : dict) : 
        """
        Update the input dictionary with the input from the player

        Args:
            input dict: Current input

        Returns:
            dict: updated input
        """
        event_queue = pygame.event.get()
        for event in event_queue:

            if event.type == pygame.QUIT:
                input["running"] = False
                return input
        

        if len(event_queue) != 0:
            for event in event_queue:
                if event.type == pygame.KEYDOWN:
                    input["key_pressed"] = None

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        input["key_pressed"] = "RETURN"
                        
                    elif event.key == pygame.K_SPACE:
                        input["key_pressed"] = "SPACE"
                        
                    elif event.key == pygame.K_ESCAPE:
                        input["key_pressed"] = "ESCAPE"
                        
                    elif event.key == pygame.K_UP:
                        input["key_pressed"] = "UP"
                        
                    elif event.key == pygame.K_DOWN:
                        input["key_pressed"] = "DOWN"
                        
                    elif event.key == pygame.K_LEFT:
                        input["key_pressed"] = "LEFT"
                        
                    elif event.key == pygame.K_RIGHT:
                        input["key_pressed"] = "RIGHT"
                    
                    elif event.key == pygame.K_p:
                        input["key_pressed"] = "P"

                    elif event.key == pygame.K_m:
                        input["key_pressed"] = "M"

                    elif event.key == pygame.K_o:
                        input["key_pressed"] = "O"

                    elif event.key == pygame.K_l:
                        input["key_pressed"] = "L"

                    elif event.key == pygame.K_k:
                        input["key_pressed"] = "K"

            
        else : 
            input["key_pressed"] = None

        return input
    
    
    def update_screen(self,input : dict) :
        """
        """ 
        if input["win"] or input["lose"] :
            self.screen.fill("blue")
            pygame.draw.rect(self.screen, "white", pygame.Rect((50, 50), (900, 620)))

            font = pygame.font.Font('freesansbold.ttf', 100)
            message = "You won !" if input["win"] else "You lost !"
            text = font.render(message, True, "black")
            textRect = text.get_rect()
            textRect.center = (500, 360)
            self.screen.blit(text, textRect)


        else:

            self.screen.fill("blue")
            pygame.draw.rect(self.screen, "black", pygame.Rect((0, 0), (400, 720)))

            player_orient = input["player_orient"]
            map = input["map"]
            self.__update_map(map)

            player_pos = input["player_pos"]
            
            self.__update_pos(player_pos, player_orient, map)

            inventory = input["inventory"]
            self.__update_inventory(inventory)

            if input["ask_Create_room"] : 
                pygame.draw.rect(self.screen, "black", pygame.Rect((450,385), (500, 285)))
                room_option = input["room_option"]
                cursor = input["cursor"]
                cursor_color = input["cursor_color"]
                dice = input["inventory"].dices
                self.__update_ask_room(room_option, cursor, cursor_color,dice)

            elif input["locked"] != None :
                pygame.draw.rect(self.screen, "black", pygame.Rect((450,385), (500, 285))) 
                cursor = input["cursor"]
                cursor_color = input["cursor_color"]
                locked = input["locked"]
                self.__update_ask_unlock(cursor, cursor_color, locked)
            
            elif input["shop"] != None : 
                pygame.draw.rect(self.screen, "black", pygame.Rect((450,385), (500, 285))) 
                cursor = input["cursor"]
                cursor_color = input["cursor_color"]
                shop = input["shop"]
                self.__update_shop(cursor, cursor_color, shop)
                
        
        pygame.display.flip()

    def __update_pos(self, player_pos : list, player_orient : str, map : list[Rooms]) : 
        """
        Update the position of the player on the screen

        Args:
            player_pos (list): list with the player's position [x, y]
        """
        current_room = map[player_pos[1]][player_pos[0]]
        current_door_north = current_room.doors["N"]
        current_door_south = current_room.doors["S"]
        current_door_east = current_room.doors["E"]
        current_door_west = current_room.doors["W"]

        
        if player_pos[1] != 0:
            next_room_north = map[player_pos[1]-1][player_pos[0]]
        else:
            next_room_north = None  
        if player_pos[1] != 8:
            next_room_south = map[player_pos[1]+1][player_pos[0]]
        else:
            next_room_south = None    
        if player_pos[0] != 4:
            next_room_east = map[player_pos[1]][player_pos[0]+1]
        else:
            next_room_east = None
        if player_pos[0] != 0:
            next_room_west = map[player_pos[1]][player_pos[0]-1]
        else:
            next_room_west = None

        if next_room_north != None:
            next_door_north = map[player_pos[1]-1][player_pos[0]].doors["S"]
        if next_room_south != None:
            next_door_south = map[player_pos[1]+1][player_pos[0]].doors["N"]
        if next_room_east != None:
            next_door_east = map[player_pos[1]][player_pos[0]+1].doors["W"]
        if next_room_west != None:
            next_door_west = map[player_pos[1]][player_pos[0]-1].doors["E"]        

        match player_orient : 
            case "N" :
                if next_room_north == None:
                    if current_door_north == "open":
                        pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (WIDTH, HEIGHT)))
                    elif current_door_north == "none":
                        pygame.draw.rect(self.screen, "red", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (WIDTH, HEIGHT)))
                else :
                    if current_door_north == "open" and next_door_north == "open":
                        pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (WIDTH, HEIGHT)))
                    elif current_door_north == "none" or next_door_north == "none":
                        pygame.draw.rect(self.screen, "red", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (WIDTH, HEIGHT)))
            
            case "W" : 
                if next_room_west == None:
                    if current_door_west == "open":
                        pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
                    elif current_door_west == "none":
                        pygame.draw.rect(self.screen, "red", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
                else :
                    if current_door_west == "open" and next_door_west == "open":
                        pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
                    elif current_door_west == "none" or next_door_west == "none":
                        pygame.draw.rect(self.screen, "red", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
            
            case "S":
                if next_room_south == None:
                    if current_door_south == "open":
                        pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH + (WIDTH - HEIGHT)), (WIDTH, HEIGHT)))
                    elif current_door_south == "none":
                        pygame.draw.rect(self.screen, "red", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH + (WIDTH - HEIGHT)), (WIDTH, HEIGHT)))
                else :
                    if current_door_south == "open" and next_door_south == "open":
                        pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH + (WIDTH - HEIGHT)), (WIDTH, HEIGHT)))
                    elif current_door_south == "none" or next_door_south == "none":
                        pygame.draw.rect(self.screen, "red", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH + (WIDTH - HEIGHT)), (WIDTH, HEIGHT)))
            
            case "E" : 
                if next_room_east == None:
                    if current_door_east == "open":
                        pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH + (WIDTH - HEIGHT), player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
                    elif current_door_east == "none":
                        pygame.draw.rect(self.screen, "red", pygame.Rect((player_pos[0] * WIDTH + (WIDTH - HEIGHT), player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
                else :
                    if current_door_east == "open" and next_door_east == "open":
                        pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH + (WIDTH - HEIGHT), player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
                    elif current_door_east == "none" or next_door_east == "none":
                        pygame.draw.rect(self.screen, "red", pygame.Rect((player_pos[0] * WIDTH + (WIDTH - HEIGHT), player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
            
                
                
        
    def __update_map(self, map : list) : 
        """
        Update on the screen the rooms in the map

        Args:
            map (list): list of all the rooms
        """
        for i in range(9) : 
            for j in range(5) : 
                if map[i][j] != None : 
                    room = map[i][j]
                    image = pygame.image.load(room.image)
                    image = pygame.transform.scale(image, (WIDTH, WIDTH))
                    image = pygame.transform.rotate(image,room.orientation)
                    self.screen.blit(image, (j * WIDTH, i * WIDTH))
        

    def __update_inventory(self, inventory : Inventory) : 
        """
        Update on the screen the contents of the inventory

        Args:
            inventory (Inventory)
        """
        #print the white rectangle
        light_grey = (100, 100, 100)
        pygame.draw.rect(self.screen, light_grey, pygame.Rect((450,50), (500, 285)))
        icons = {
            "steps": pygame.image.load("Rooms & Icons\icons\Steps.webp"),
            "coins": pygame.image.load("Rooms & Icons\icons\Gold.webp"),
            "gems": pygame.image.load("Rooms & Icons\icons\Gem.webp"),
            "keys": pygame.image.load("Rooms & Icons\icons\Key.webp"),
            "dices": pygame.image.load("Rooms & Icons\icons\Ivory_Dice.webp")
        }
        numbers = {
            "steps": inventory.steps,
            "coins": inventory.coins,
            "gems": inventory.gems,
            "keys": inventory.keys,
            "dices": inventory.dices
        }
        names = ("steps", "coins", "gems", "keys", "dices")
        #numbers = (inventory.steps, inventory.coins, inventory.gems, inventory.keys, inventory.dices)
        icon_size = (32, 32)
    
        for i, name in enumerate(icons.keys()):
            # Icon
            icon = pygame.transform.scale(icons[name], icon_size)
            cX = 500 + (i % 3) * 125
            cY = 80 + (i // 3) * 50
            self.screen.blit(icon, (cX, cY))

            # Number next to the icon
            font = pygame.font.Font('freesansbold.ttf', 20)
            number_text = font.render(str(numbers[name]), True, "black")
            text_rect = number_text.get_rect()
            text_rect.midleft = (cX + icon_size[0] + 5, cY + icon_size[1] // 2)
            self.screen.blit(number_text, text_rect)

        #print objects

        i=0
        for key, value in inventory.object_list.__dict__.items(): 
            if value == True or (isinstance(value, int) and value > 0):
                font = pygame.font.Font('freesansbold.ttf', 20)
                if key == "crochet_kit":
                    display_key = "crochet kit"
                elif key == "metal_detector":
                    display_key = "metal detector"
                elif key == "rabbit_foot":
                    display_key = "rabbit foot"
                elif key =="apple":
                    display_key = f"apple x{inventory.object_list.apple}"
                elif key =="banana":
                    display_key = f"banana x{inventory.object_list.banana}"
                elif key =="cake":
                    display_key = f"cake x{inventory.object_list.cake}"
                elif key =="sandwich":
                    display_key = f"sandwich x{inventory.object_list.sandwich}"
                elif key =="dinner":
                    display_key = f"dinner x{inventory.object_list.dinner}"
                else:
                    display_key = key
                text = font.render(str(display_key), True, "black")
                textRect = text.get_rect()
                cX = 575 + (i % 3) * 150
                cY = 200 + (i // 3) * 40
                textRect.center = (cX, cY )
                self.screen.blit(text, textRect)
                i+=1
        pygame.draw.rect(self.screen, "black", pygame.Rect((450,385), (500, 285)))
        font = pygame.font.Font('freesansbold.ttf', 20)
        text1 = font.render("P : To eat Apple", True, "white")
        text2 = font.render("M : To eat Banana", True, "white")
        text3 = font.render("O : To eat Cake", True, "white")
        text4 = font.render("L : To eat Sandwich", True, "white")
        text5 = font.render("K : To eat Dinner", True, "white")
        food_exist = inventory.object_list
        if food_exist.apple > 0:
            self.screen.blit(text1, (460, 395))
        if food_exist.banana > 0:
            self.screen.blit(text2, (460, 420))
        if food_exist.cake > 0:
            self.screen.blit(text3, (460, 445))
        if food_exist.sandwich > 0:
            self.screen.blit(text4, (460, 470))
        if food_exist.dinner > 0:
            self.screen.blit(text5, (460, 495))
    
    def __update_ask_room(self, room_option : list, cursor : int, cursor_color : str, dice :int):

        for i, room in enumerate(room_option) : 
            image = pygame.image.load(room.image)
            image = pygame.transform.scale(image, (150, 150))
            self.screen.blit(image, (463 + (i * 162), 400))

            font = pygame.font.Font('freesansbold.ttf', 20)
            text = f"{room.cost} gems"
            text = font.render(text, True, "white")
            textRect = text.get_rect()
            textRect.center = (538 + (i * 162), 590)
            self.screen.blit(text, textRect)
        if dice > 0:
            text_re = font.render("ESC : To Reroll", True, "white")
            self.screen.blit(text_re, (640, 620))
        
        pygame.draw.rect(self.screen, cursor_color, pygame.Rect((463 + (cursor * 162), 400), (150, HEIGHT)))
        pygame.draw.rect(self.screen, cursor_color, pygame.Rect((463 + (cursor * 162), 400), (HEIGHT, 150)))
        pygame.draw.rect(self.screen, cursor_color, pygame.Rect((463 + (cursor * 162), 400 + (150 - HEIGHT)), (150, HEIGHT)))
        pygame.draw.rect(self.screen, cursor_color, pygame.Rect((463 + (cursor * 162) + (150 - HEIGHT), 400), (HEIGHT, 150)))
    
    def __update_ask_unlock(self, cursor : int, cursor_color : str, locked : int) : 

        font = pygame.font.Font('freesansbold.ttf', 30)
        text = "Do you want to open this door ?" 
        text = font.render(text, True, "white")
        textRect = text.get_rect()
        textRect.center = (700, 400)
        self.screen.blit(text, textRect)

        text = f"It requires {locked} key(s)."
        text = font.render(text, True, "white")
        textRect = text.get_rect()
        textRect.center = (700, 500)
        self.screen.blit(text, textRect)

        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("no", True, "white")
        textRect = text.get_rect()
        textRect.center = (575, 600)
        self.screen.blit(text, textRect)

        text = font.render("yes", True, "white")
        textRect = text.get_rect()
        textRect.center = (825, 600)
        self.screen.blit(text, textRect)

    
        pygame.draw.rect(self.screen, cursor_color, pygame.Rect((535 + (cursor * 250), 560 + (80 - HEIGHT)), (80, HEIGHT)))
        
    def __update_shop(self, cursor : int, cursor_color : str, shop : list) : 
        for i, item in enumerate(shop) : 
            font = pygame.font.Font('freesansbold.ttf', 15)
            text = font.render(item.name, True, "white")
            textRect = text.get_rect()
            textRect.center = (538 + (i * 162), 450)
            self.screen.blit(text, textRect)

            font = pygame.font.Font('freesansbold.ttf', 20)
            text = f"{item.price} coins"
            text = font.render(text, True, "white")
            textRect = text.get_rect()
            textRect.center = (538 + (i * 162), 590)
            self.screen.blit(text, textRect)
        
        pygame.draw.rect(self.screen, cursor_color, pygame.Rect((463 + (cursor * 162), 400 + (150 - HEIGHT)), (150, HEIGHT)))



    def quit() : 
        """
        quit the pygame  window
        """
        pygame.quit()
