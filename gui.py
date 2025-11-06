import pygame
from inventory import Inventory

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
        
        
        """ if input["ask_Create_room"] : 
            input["ask_Create_room"] = False  """

        if len(event_queue) != 0 : 

            if event.type == pygame.KEYDOWN:
                self.previous = True
                self.previous_key = pygame.key.get_pressed()
                input["key_pressed"] = None

            elif (event.type == pygame.KEYUP) and (self.previous) : 
                self.previous = False

                if self.previous_key[pygame.K_UP]:
                    input["key_pressed"] = "UP"

                elif self.previous_key[pygame.K_DOWN]:
                    input["key_pressed"] = "DOWN"

                elif self.previous_key[pygame.K_LEFT]:
                    input["key_pressed"] = "LEFT"

                elif self.previous_key[pygame.K_RIGHT]:
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


        elif not(input["ask_Create_room"]):

            self.screen.fill("blue")
            pygame.draw.rect(self.screen, "black", pygame.Rect((0, 0), (400, 720)))

            player_orient = input["player_orient"]
            map = input["map"]
            self.__update_map(map)

            player_pos = input["player_pos"]
            
            self.__update_pos(player_pos, player_orient)

            inventory = input["inventory"]
            self.__update_inventory(inventory)

            # to modify 
            pygame.draw.rect(self.screen, "black", pygame.Rect((450,385), (500, 285)))

        pygame.display.flip()

    def __update_pos(self, player_pos : list, player_orient : str) : 
        """
        Update the position of the player on the screen

        Args:
            player_pos (list): list with the player's position [x, y]
        """
        match player_orient : 
            case "N" :
                pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (WIDTH, HEIGHT)))
            case "W" : 
                pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
            case "S":
                pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH + (WIDTH - HEIGHT)), (WIDTH, HEIGHT)))
            case "E" : 
                pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH + (WIDTH - HEIGHT), player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
        
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
    
        
    def quit() : 
        """
        quit the pygame  window
        """
        pygame.quit()
