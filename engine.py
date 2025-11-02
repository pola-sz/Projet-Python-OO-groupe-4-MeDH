from inventory import Inventory

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
                 "running" : True, 
                 "map" : [[None, None, "blue", None, None],
                          [None, None, None, None, None],
                          [None, None, None, None, None],
                          [None, None, None, None, None],
                          [None, None, None, None, None],
                          [None, None, None, "yellow", None],
                          [None, None, None, "green", None],
                          ["yellow", "green", "red", "red", None],
                          [None, "red", "blue", "yellow", None]],
                 "key_pressed" : None,
                 "inventory" : Inventory(),
                 "ask_Create_room" : False,
                 "create_room" : False}
        return input

    def interpret_input(current_input : dict) : 
        """
        Update the input in regards to the keys pressed by the user

        Args:
            current_input (dict): Current input

        Returns:
            dict: New input
        """
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
                new_input["player_pos"], new_input["ask_Create_room"], new_input["inventory"] = Engine.__move_player(player_pos, key_pressed, map, inventory)

        return new_input





    def __move_player(player_pos : list, key : str,  map : list, inventory : Inventory) : 
        """
        Update the position of the player

        Args:
            player_pos (list): current position of the player
            key (str): which key was pressed
            map (list): map of the rooms

        Returns:
            list: new position of the player
            bool: flag indicating if we ask the player to create a room or not
        """
        
        if key != None : 
            new_player_pos = player_pos.copy()
            if key == "UP":
                new_player_pos[1] -= 1
                new_player_pos[1] = max(0, new_player_pos[1])
                new_player_pos[1] = min(new_player_pos[1], 8)
            elif key == "DOWN":
                new_player_pos[1] += 1
                new_player_pos[1] = max(0, new_player_pos[1])
                new_player_pos[1] = min(new_player_pos[1], 8)
            elif key == "LEFT":
                new_player_pos[0] -= 1
                new_player_pos[0] = max(0, new_player_pos[0])
                new_player_pos[0] = min(new_player_pos[0], 4)
            elif key == "RIGHT":
                new_player_pos[0] += 1
                new_player_pos[0] = max(0, new_player_pos[0])
                new_player_pos[0] = min(new_player_pos[0], 4)

            if map[new_player_pos[1]][new_player_pos[0]] != None and (inventory.steps != 0): 
                # if the room exists
                inventory.steps -= 1
                return new_player_pos, False, inventory
            else : 
                #if it doesn't
                return player_pos, True, inventory
            
        return player_pos, False, inventory
    

    def __create_room() :
        pass

    