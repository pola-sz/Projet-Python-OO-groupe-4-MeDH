from inventory import Inventory
from rooms import Rooms, create_room
class Engine : 

    def __init__(self) : 
        pass

    def input_initialize() : 
        """
        Initialize the input dictionnary

        Returns:
            dict: input dictionnary
        """
        input = {"player_pos" : [2, 8],
                 "player_orient" : "N",
                 "running" : True, 
                 "map" : Engine.initialize_map(),
                 "key_pressed" : None,
                 "inventory" : Inventory(),
                 "ask_Create_room" : False,
                 "create_room" : False,
                 "win" : False,
                 "lose" : False}
        return input
    
    def initialize_map():
        start = create_room(start=True)
        end = create_room(end=True)
        return [[None, None, end , None, None],
                [None, None,None , None, None],
                [None, None,None , None, None],
                [None, None,None , None, None],
                [None, None,None , None, None],
                [None, None,None , None, None],
                [None, None,None , None, None],
                [None, None,None , None, None],
                [None, None, start , None, None]]
    
    def interpret_input(current_input : dict) : 
        """
        Update the input in regards to the keys pressed by the user

        Args:
            current_input (dict): Current input

        Returns:
            dict: New input
        """

        if current_input["win"] or current_input["lose"] : 
            return current_input

        new_input = current_input.copy()

        #if we are still running the game and not in the process of creating a room
        if current_input["running"]  and not(current_input["ask_Create_room"]) :

            if current_input["create_room"] : 
                Engine.__create_room()

            else : 
                player_pos = current_input["player_pos"]
                map = current_input["map"]
                key_pressed = current_input["key_pressed"]
                inventory = current_input["inventory"]
                player_orient = current_input["player_orient"]
                new_input["player_pos"], new_input["player_orient"], new_input["ask_Create_room"], new_input["inventory"] = Engine.__move_player(player_pos, player_orient, key_pressed, map, inventory)
            
            if player_pos == [2, 0] : 
                new_input["win"] = True

            if inventory.steps == 0 : 
                new_input["lose"] = True
        return new_input





    def __move_player(player_pos : list, player_orient : str, key : str,  map : list, inventory : Inventory) : 
        """
        Update the position of the player

        Args:
            player_pos (list): current position of the player
            key (str): which key was pressed
            map (list): map of the rooms
            inventory (Inventory) : current inventory

        Returns:
            list: new position of the player
            bool: flag indicating if we ask the player to create a room or not
        """
        new_orient = player_orient # default value

        if key != None : 
            new_player_pos = player_pos.copy()
            if key == "UP" and player_orient == "N":
                new_player_pos[1] -= 1

            elif key == "DOWN" and player_orient == "S":
                new_player_pos[1] += 1

            elif key == "LEFT" and player_orient == "W":
                new_player_pos[0] -= 1

            elif key == "RIGHT" and player_orient == "E":
                new_player_pos[0] += 1
            
            else :  
                match player_orient : 
                    case "N": 
                        if key == "RIGHT": 
                            new_orient = "E" 
                        elif  key == "LEFT":
                            new_orient = "W"
                    case "S":
                        if key == "RIGHT": 
                            new_orient = "E" 
                        elif  key == "LEFT":
                            new_orient = "W"
                    case "W":
                        if key == "UP": 
                            new_orient = "N" 
                        elif  key == "DOWN":
                            new_orient = "S"
                    case "E":
                        if key == "UP": 
                            new_orient = "N" 
                        elif  key == "DOWN":
                            new_orient = "S"
            


            if (0 <= new_player_pos[0]) and (new_player_pos[0] <= 4) and (0 <= new_player_pos[1]) and (new_player_pos[1] <= 8) : 

                if map[new_player_pos[1]][new_player_pos[0]] != None and (inventory.steps != 0): 
                    # if the room exists and there are steps
                    if new_player_pos != player_pos : 
                        inventory.steps -= 1
                    return new_player_pos, new_orient, False, inventory
                else : 
                    #if it doesn't
                    return player_pos, new_orient, True, inventory
            
        return player_pos, new_orient, False, inventory
    

    def __create_room() :
        pass