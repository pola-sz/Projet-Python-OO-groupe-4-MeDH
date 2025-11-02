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
        
        
        if input["ask_Create_room"] : 
            input["ask_Create_room"] = False 

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
        if not(input["ask_Create_room"]):

            self.screen.fill("blue")
            pygame.draw.rect(self.screen, "black", pygame.Rect((0, 0), (400, 720)))

            map = input["map"]
            self.__update_map(map)

            player_pos = input["player_pos"]
            self.__update_pos(player_pos)

            inventory = input["inventory"]
            self.__update_inventory(inventory)

            pygame.display.flip()

    def __update_pos(self, player_pos : list) : 
        """
        Update the position of the player on the screen

        Args:
            player_pos (list): list with the player's position [x, y]
        """

        pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (WIDTH, HEIGHT)))
        pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH + (WIDTH - HEIGHT)), (WIDTH, HEIGHT)))
        pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
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
                    pygame.draw.rect(self.screen, map[i][j], pygame.Rect((j * WIDTH, i * WIDTH), (WIDTH, WIDTH)))
        

    def __update_inventory(self, inventory : Inventory) : 
        """
        Update on the screen the contents of the inventory

        Args:
            inventory (Inventory)
        """
        pass

        
    
        
    def quit() : 
        """
        quit the pygame  window
        """
        pygame.quit()
