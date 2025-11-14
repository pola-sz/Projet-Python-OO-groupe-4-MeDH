import pygame
from inventory import Inventory
from rooms import Rooms, create_room, rooms

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

            pygame.draw.rect(self.screen, "black", pygame.Rect((450,385), (500, 285)))

            if input["ask_Create_room"] : 
                room_option = input["room_option"]
                cursor = input["cursor"]
                cursor_color = input["cursor_color"]
                self.__update_ask_room(room_option, cursor, cursor_color)

            elif input["locked"] != None : 
                cursor = input["cursor"]
                cursor_color = input["cursor_color"]
                locked = input["locked"]
                self.__update_ask_unlock(cursor, cursor_color, locked)
            



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
        pygame.draw.rect(self.screen, "white", pygame.Rect((450,50), (500, 285)))


        names = ("steps", "coins", "gems", "keys", "dices")
        numbers = (inventory.steps, inventory.coins, inventory.gems, inventory.keys, inventory.dices)

        for i in range(5) : 
            
            to_print = str(numbers[i]) + " " + names[i]
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render(to_print, True, "black")
            textRect = text.get_rect()
            cX = 575 + (i % 3) * 125
            cY = 100 + (i // 3) * 40
            textRect.center = (cX, cY )
            self.screen.blit(text, textRect)

        #print objects

        """ for i, el in enumerate(inventory.object_list): 
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render(str(el), True, "black")
            textRect = text.get_rect()
            cX = 575 + (i % 3) * 125
            cY = 200 + (i // 3) * 40

            textRect.center = (cX, cY )
            self.screen.blit(text, textRect) """
        
        """ if inventory.object_list != "empty":
            pass
            print(inventory.object_list)
        else:
            print(inventory.object_list)
            i= 1
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render("goulash", True, "black")
            textRect = text.get_rect()
            cX = 575 + (i % 3) * 125
            cY = 200 + (i // 3) * 40

            textRect.center = (cX, cY )
            self.screen.blit(text, textRect) """
        i=0
        for key, value in inventory.object_list.__dict__.items(): 
            if value == True:
                font = pygame.font.Font('freesansbold.ttf', 20)
                text = font.render(str(key), True, "black")
                textRect = text.get_rect()
                cX = 575 + (i % 3) * 150
                cY = 200 + (i // 3) * 40

                textRect.center = (cX, cY )
                self.screen.blit(text, textRect)
                i+=1
    
    def __update_ask_room(self, room_option : list, cursor : int, cursor_color : str):

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
        


    def quit() : 
        """
        quit the pygame  window
        """
        pygame.quit()
