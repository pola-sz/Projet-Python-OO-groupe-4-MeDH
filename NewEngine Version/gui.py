import pygame
from inventory import Inventory
from rooms import Rooms, create_room, rooms

WIDTH = 80 # Width of a room
HEIGHT = 8 #Height of the player

class GUI : 
    def __init__(self) : 
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 720))
        self.screen.fill((65, 105, 225))
        self.clock = pygame.time.Clock()
        self.previous = False
        self.previous_key = None
        # Load small inventory icons (use forward-slash paths)
        def load_icon(path, size=(24,24)):
            try:
                img = pygame.image.load(path)
                img = pygame.transform.scale(img, size)
                return img
            except Exception:
                return None

        self.icon_paths = {
            'steps': 'Rooms & Icons/Steps.png',
            'coins': 'Rooms & Icons/Gold.webp',
            'gems': 'Rooms & Icons/Gems.webp',
            'keys': 'Rooms & Icons/Keys.png',
            'dices': 'Rooms & Icons/Dices.png'
        }
        self.icons = {k: load_icon(p) for k, p in self.icon_paths.items()}

        # item icons (from object.py)
        self.item_icon_paths = {
            'shovel': 'Rooms & Icons/Shovel.webp',
            'hammer': 'Rooms & Icons/Hammer.webp',
            'lockpick': 'Rooms & Icons/Lockpick.webp',
            'metal_detector': 'Rooms & Icons/Metal_detector.png',
            'rabbit_foot': 'Rooms & Icons/Rabbit_foot.webp'
        }
        self.item_icons = {k: load_icon(p, size=(32,32)) for k, p in self.item_icon_paths.items()}

        # small mapping of room descriptions for the three-room chooser
        self.room_descriptions = {
            # Blue rooms
            'Pantry': '+4 Gold',
            'Den': '+1 Gem',
            'Trophy_room': '-1 Gem, +8 Gems, +5 Gold, Has Locked door',
            'Parlor': 'Has Locked door',
            'Ballroom': 'Sets Gems to 2',
            'Gallery': 'Has Locked door',
            'Music Room': '+1 Key',
            'Locker Room': '+1 Key',
            'Freezer': 'Locks certain room effects',
            'Garage': '+3 Keys',
            'Closet': '+2 random items, +2 Gold',
            'Sauna': '+20 Steps',
            'Attic': '+2 random items',
            # Green rooms
            'Cloister': '-3 Gems',
            'Courtyard': '-1 Gem',
            'Greenhouse': '-1 Gems',
            'Morning Room': '+2 Gems',
            'Patio': '-1 Gem, +4 Gems',
            'Secret Garden': '+8 Steps, +1 Gold',
            'Terrace': 'All Green Rooms cost 0 Gems',
            'Veranda': '-2 Gems, +1 random item, Has Locked door',
            # Orange
            'Great Hall': '-3 Gems, Has Locked doors',
            'Corridor': '-1 Gem',
            'East Wing Hall': '-1 Gem, Has Locked door',
            'Foyer': '-1 Gem',
            'Passageway': 'Has Locked doors',
            'Secret Passage': 'Has Locked doors',
            'West Wing Hall': 'Has Locked door',
            # Purple
            'Bedroom': '+10 Steps, +2 Gold',
            'Bunk Room': '-1 Gem, +20 Steps, +4 Gold',
            'Guest Bedroom': '+10 Steps',
            "Her Ladyship's Chamber": '+10 Steps, +3 Gems, +2 Gold',
            'Master Bedroom': '+10 Steps',
            'Nursery': '+5 Steps, -2 Gold',
            "Servant's Quarters": '+2 Keys',
            # Red
            'Archives': '-3 Gems, Has Locked doors',
            'Chapel': '-5 Gold, Has Locked door',
            'Dark Room': 'Has Locked doors',
            'Gymnasium': '-1 Gem, -10 Steps',
            'Furnace': '-10 Steps',
            'Weight Room': 'Divide your Steps by 2, Has Locked doors',
            # Yellow
            'Bookshop': 'Has Locked door',
            'Commissary': 'Has Locked door',
            'Laundry Room': '-5 Gold',
            'Kitchen': '-1 Gem',
            'Mount Holly Gift Shop': 'Has Locked doors',
            'Locksmith': '-2 Gems',
            'Showroom': '-2 Gems',
            'The Armory': 'Has Locked door'
        }

    def __wrap_text(self, text: str, max_width: int, font: pygame.font.Font) -> list:
        """Wrap text to fit within max_width pixels. Returns list of lines."""
        if not text:
            return []
        words = text.split()
        lines = []
        current_line = ""
        for word in words:
            test_line = current_line + (" " if current_line else "") + word
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
        return lines

    
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
            self.screen.fill((65, 105, 225))
            pygame.draw.rect(self.screen, (225, 225, 225), pygame.Rect((50, 50), (900, 620)), border_radius = 20)

            font = pygame.font.Font('freesansbold.ttf', 100)
            message = "You won !" if input["win"] else "You lost !"
            text = font.render(message, True, "black")
            textRect = text.get_rect()
            textRect.center = (500, 360)
            self.screen.blit(text, textRect)


        else:

            self.screen.fill((65, 105, 225))
            pygame.draw.rect(self.screen, (31, 31, 31), pygame.Rect((0, 0), (400, 720)), border_top_right_radius = 20, border_bottom_right_radius = 20)

            player_orient = input["player_orient"]
            map = input["map"]
            self.__update_map(map)

            player_pos = input["player_pos"]
            
            self.__update_pos(player_pos, player_orient,map)

            inventory = input["inventory"]
            self.__update_inventory(inventory)

            # slightly lower top margin for the right-hand panel
            pygame.draw.rect(self.screen, (31, 31, 31), pygame.Rect((450,395), (500, 285)),border_radius = 20)
            pygame.draw.rect(self.screen, (35, 75, 225), pygame.Rect((450,395), (500, 285)), width = 5, border_radius = 20)

            if input["ask_Create_room"] : 
                room_option = input["room_option"]
                cursor = input["cursor"]
                blocked_rooms = input.get("blocked_rooms", [])
                self.__update_ask_room(room_option, cursor, blocked_rooms)
            if input.get("ask_unlock"):
                # show unlock prompt over the right-hand panel
                self.__update_ask_unlock(input.get("unlock_cursor", 0), input.get("unlock_cursor_color", "white"))
            



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
                    elif current_door_north == "locked":
                        pygame.draw.rect(self.screen, (255,165,0), pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (WIDTH, HEIGHT)))
                    elif current_door_north == "none":
                        pygame.draw.rect(self.screen, "red", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (WIDTH, HEIGHT)))
                else :
                    if current_door_north == "open" and next_door_north == "open":
                        pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (WIDTH, HEIGHT)))
                    elif current_door_north == "locked" or next_door_north == "locked":
                        pygame.draw.rect(self.screen, (255,165,0), pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (WIDTH, HEIGHT)))
                    elif current_door_north == "none" or next_door_north == "none":
                        pygame.draw.rect(self.screen, "red", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (WIDTH, HEIGHT)))
            
            case "W" : 
                if next_room_west == None:
                    if current_door_west == "open":
                        pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
                    elif current_door_west == "locked":
                        pygame.draw.rect(self.screen, (255,165,0), pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
                    elif current_door_west == "none":
                        pygame.draw.rect(self.screen, "red", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
                else :
                    if current_door_west == "open" and next_door_west == "open":
                        pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
                    elif current_door_west == "locked" or next_door_west == "locked":
                        pygame.draw.rect(self.screen, (255,165,0), pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
                    elif current_door_west == "none" or next_door_west == "none":
                        pygame.draw.rect(self.screen, "red", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
            
            case "S":
                if next_room_south == None:
                    if current_door_south == "open":
                        pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH + (WIDTH - HEIGHT)), (WIDTH, HEIGHT)))
                    elif current_door_south == "locked":
                        pygame.draw.rect(self.screen, (255,165,0), pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH + (WIDTH - HEIGHT)), (WIDTH, HEIGHT)))
                    elif current_door_south == "none":
                        pygame.draw.rect(self.screen, "red", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH + (WIDTH - HEIGHT)), (WIDTH, HEIGHT)))
                else :
                    if current_door_south == "open" and next_door_south == "open":
                        pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH + (WIDTH - HEIGHT)), (WIDTH, HEIGHT)))
                    elif current_door_south == "locked" or next_door_south == "locked":
                        pygame.draw.rect(self.screen, (255,165,0), pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH + (WIDTH - HEIGHT)), (WIDTH, HEIGHT)))
                    elif current_door_south == "none" or next_door_south == "none":
                        pygame.draw.rect(self.screen, "red", pygame.Rect((player_pos[0] * WIDTH, player_pos[1] * WIDTH + (WIDTH - HEIGHT)), (WIDTH, HEIGHT)))
            
            case "E" : 
                if next_room_east == None:
                    if current_door_east == "open":
                        pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH + (WIDTH - HEIGHT), player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
                    elif current_door_east == "locked":
                        pygame.draw.rect(self.screen, (255,165,0), pygame.Rect((player_pos[0] * WIDTH + (WIDTH - HEIGHT), player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
                    elif current_door_east == "none":
                        pygame.draw.rect(self.screen, "red", pygame.Rect((player_pos[0] * WIDTH + (WIDTH - HEIGHT), player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
                else :
                    if current_door_east == "open" and next_door_east == "open":
                        pygame.draw.rect(self.screen, "white", pygame.Rect((player_pos[0] * WIDTH + (WIDTH - HEIGHT), player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
                    elif current_door_east == "locked" or next_door_east == "locked":
                        pygame.draw.rect(self.screen, (255,165,0), pygame.Rect((player_pos[0] * WIDTH + (WIDTH - HEIGHT), player_pos[1] * WIDTH), (HEIGHT, WIDTH)))
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
        pygame.draw.rect(self.screen, (225, 225, 225), pygame.Rect((450,50), (500, 285)), border_radius = 20)
        pygame.draw.rect(self.screen, (31, 31, 31), pygame.Rect((450,50), (500, 285)), width = 5, border_radius = 20)


        names = ("steps", "coins", "gems", "keys", "dices")
        numbers = (inventory.steps, inventory.coins, inventory.gems, inventory.keys, inventory.dices)

        for i in range(5) : 
            font = pygame.font.Font('freesansbold.ttf', 20)
            cX = 575 + (i % 3) * 125
            cY = 100 + (i // 3) * 40
            # draw number
            text = font.render(str(numbers[i]), True, "black")
            textRect = text.get_rect()
            textRect.midleft = (cX - 10, cY)
            self.screen.blit(text, textRect)
            # draw icon if available
            icon = self.icons.get(names[i])
            if icon:
                icon_rect = icon.get_rect()
                icon_rect.midleft = (cX + 30, cY)
                self.screen.blit(icon, icon_rect)
            else:
                # fallback: draw name
                text2 = font.render(names[i], True, "black")
                t2r = text2.get_rect()
                t2r.midleft = (cX + 30, cY)
                self.screen.blit(text2, t2r)

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
        # show found item icons
        i = 0
        for key, value in inventory.object_list.__dict__.items(): 
            if value:
                icon = self.item_icons.get(key)
                cX = 575 + (i % 3) * 150
                cY = 200 + (i // 3) * 40
                if icon:
                    rect = icon.get_rect()
                    rect.center = (cX, cY)
                    self.screen.blit(icon, rect)
                else:
                    font = pygame.font.Font('freesansbold.ttf', 18)
                    text = font.render(str(key), True, "black")
                    textRect = text.get_rect()
                    textRect.center = (cX, cY )
                    self.screen.blit(text, textRect)
                i += 1
    
    def __update_ask_room(self, room_option : list, cursor : int, blocked_rooms: list = None):
        if blocked_rooms is None:
            blocked_rooms = []

        top_y = 410  # 10 pixels lower than before (was 400)
        for i, room in enumerate(room_option) : 
            image = pygame.image.load(room.image)
            image = pygame.transform.scale(image, (150, 150))
            # dim image if blocked
            if i in blocked_rooms:
                image.set_alpha(100)
            self.screen.blit(image, (463 + (i * 162), top_y))
            # draw description text under each room
            desc = self.room_descriptions.get(room.name, "")
            if desc:
                font = pygame.font.Font('freesansbold.ttf', 14)
                # wrap text to fit within box (150px width, with some padding)
                lines = self.__wrap_text(desc, 140, font)
                # text color: red if blocked, light gray if not
                text_color = (255, 100, 100) if i in blocked_rooms else (225, 225, 225)
                for li, line in enumerate(lines[:3]):
                    text = font.render(line, True, text_color)
                    tr = text.get_rect()
                    tr.center = (463 + (i * 162) + 75, top_y + 150 + 22 + (li * 18))  # 22 instead of 12 (10 pixels lower)
                    self.screen.blit(text, tr)
        pygame.draw.rect(self.screen, "white", pygame.Rect((463 + (cursor * 162), top_y), (150, HEIGHT)))
        pygame.draw.rect(self.screen, "white", pygame.Rect((463 + (cursor * 162), top_y), (HEIGHT, 150)))
        pygame.draw.rect(self.screen, "white", pygame.Rect((463 + (cursor * 162), top_y + (150 - HEIGHT)), (150, HEIGHT)))
        pygame.draw.rect(self.screen, "white", pygame.Rect((463 + (cursor * 162) + (150 - HEIGHT), top_y), (HEIGHT, 150)))

    def __update_ask_unlock(self, cursor: int, cursor_color: str):
        # simple centered unlock confirmation on the right-hand panel
        font = pygame.font.Font('freesansbold.ttf', 28)
        text = "Do you want to unlock this door ?"
        rendered = font.render(text, True, (225, 225, 225))
        rect = rendered.get_rect()
        rect.center = (700, 450)
        self.screen.blit(rendered, rect)

        # yes/no options
        opt_font = pygame.font.Font('freesansbold.ttf', 22)
        no_text = opt_font.render("No", True, (225, 225, 225))
        yes_text = opt_font.render("Yes", True, (225, 225, 225))
        no_r = no_text.get_rect()
        yes_r = yes_text.get_rect()
        no_r.center = (575, 520)
        yes_r.center = (825, 520)
        self.screen.blit(no_text, no_r)
        self.screen.blit(yes_text, yes_r)

        # draw cursor box around selection
        pygame.draw.rect(self.screen, cursor_color, pygame.Rect((535 + (cursor * 250), 480 + (80 - HEIGHT)), (80, HEIGHT)))
  
    def quit() : 
        """
        quit the pygame  window
        """
        pygame.quit()
