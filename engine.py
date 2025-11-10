from inventory import Inventory
from rooms import Rooms, create_room, rooms
import numpy as np

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
                 "cursor" : None,
                 "room_option" : None,
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

        #if we are still running the game
        if current_input["running"] :

            # if we are in the process of creating a room
            if current_input["ask_Create_room"] : 

                new_input = Engine.__askCreateRoom(current_input)


            else : 
                new_input = Engine.__move_player(current_input)

            
            if new_input["player_pos"] == [2, 0] : 
                new_input["win"] = True

            if new_input["inventory"].steps == 0 : 
                new_input["lose"] = True

        return new_input
    
    def __move_player(current_input : dict) : 
        """
        Update the position of the player

        Args:
            player_pos (list): current position of the player
            key (str): which key was pressed
            map (list): map of the rooms
            inventory (Inventory) : current inventory

        Returns:
            dict : new input
        """
        new_input = current_input.copy()

        player_pos = current_input["player_pos"]
        player_orient = current_input["player_orient"]
        key = current_input["key_pressed"]
        map = current_input["map"]
        inventory = current_input["inventory"]



        if key != None : 
            new_orient = player_orient

            new_player_pos = player_pos.copy()
            if key == "UP" and player_orient == "N":
                if map[new_player_pos[1]][new_player_pos[0]].doors["N"] != "none":
                    new_player_pos[1] -= 1

            elif key == "DOWN" and player_orient == "S":
                if map[new_player_pos[1]][new_player_pos[0]].doors["S"] != "none":
                    new_player_pos[1] += 1

            elif key == "LEFT" and player_orient == "W":
                if map[new_player_pos[1]][new_player_pos[0]].doors["W"] != "none":
                    new_player_pos[0] -= 1

            elif key == "RIGHT" and player_orient == "E":
                if map[new_player_pos[1]][new_player_pos[0]].doors["E"] != "none":
                    new_player_pos[0] += 1
            
            else :  
            
                if key == "RIGHT": 
                    new_orient = "E"
                if key == "LEFT": 
                    new_orient = "W"
                if key == "UP": 
                    new_orient = "N"
                if key == "DOWN": 
                    new_orient = "S"
            

            if (0 <= new_player_pos[0]) and (new_player_pos[0] <= 4) and (0 <= new_player_pos[1]) and (new_player_pos[1] <= 8) : 
                
                # if the room exists and there are steps
                if map[new_player_pos[1]][new_player_pos[0]] != None and (inventory.steps != 0): 
                    
                    opposite = {"N":"S","S":"N","W":"E","E":"W"}
                    current_door = map[player_pos[1]][player_pos[0]].doors[player_orient]
                    next_door = map[new_player_pos[1]][new_player_pos[0]].doors[opposite[player_orient]]

                    if ( current_door != "none")  and (next_door != "none"):
                        if new_player_pos != player_pos : 
                            inventory.steps -= 1
                            new_input["player_pos"] = new_player_pos
                            new_input["inventory"] = inventory
                    
                    
                    
                #if the room dosn't exist => ask to create one
                elif map[new_player_pos[1]][new_player_pos[0]] == None: 
                    
                    new_input["ask_Create_room"] = True
                    new_input["cursor"] = 0
                    new_input["room_option"] = Engine.__three_rooms()
                    
                new_input["player_orient"] = new_orient   

        return new_input
    

    def __create_room(input : dict, new_room : Rooms) :
        """
        Create a new room based on the player's current position and orientation.
        Args:
            input (dict): current input 
        Returns:
            list: new map
        """
        new_room = new_room.copy()
        col,row = input["player_pos"]
        map = input["map"].copy()
        match input["player_orient"]:
            case "N":
                new_room.orientation = 0
                Engine.__spin(new_room.doors,new_room.orientation)
                map[row-1][col] = new_room
            case "S":
                new_room.orientation = 180
                Engine.__spin(new_room.doors,new_room.orientation)
                map[row+1][col] = new_room
            case "W":
                new_room.orientation = 90
                Engine.__spin(new_room.doors,new_room.orientation)
                map[row][col-1] = new_room
            case "E":
                new_room.orientation = -90
                Engine.__spin(new_room.doors,new_room.orientation)
                map[row][col+1] = new_room
        return map

    def __spin(doors : dict, orientation : int):
        """
        orients the rooms according to the player's orientation
        Args:
            doors (dict): doors of the room
            orientation (int): orientation of the room
        
        """
        temp = doors.copy()
        match orientation:
            case 0:
                doors = temp
            case 90:
                doors["N"] = temp["E"]
                doors["S"] = temp["W"]
                doors["W"] = temp["N"]
                doors["E"] = temp["S"]
            case 180:
                doors["N"] = temp["S"]
                doors["S"] = temp["N"]
                doors["W"] = temp["E"]
                doors["E"] = temp["W"]
            case -90:
                doors["N"] = temp["W"]
                doors["S"] = temp["E"]
                doors["W"] = temp["S"]
                doors["E"] = temp["N"]

    def __askCreateRoom(current_input : dict) :
        cursor = current_input["cursor"]
        key = current_input["key_pressed"]
        room_option = current_input["room_option"]
        new_input = current_input.copy()

        if key == "RIGHT" : 
            cursor = min(cursor + 1, 2)
        elif key == "LEFT" : 
            cursor = max(cursor - 1, 0)
        elif key == "RETURN" or key == "SPACE" : 
            new_input["ask_Create_room"] = False
            new_input["cursor"] = None
            new_input["room_option"] = None

            new_input["map"] = Engine.__create_room(current_input, room_option[cursor])
        new_input["cursor"] = cursor
        return new_input


    def __three_rooms():
        """
        Selects three rooms based on their rarity.

        Returns:
            list: list of the three room 
        """
        total_prob = 0
        current_prob = []
        for R in rooms:
            if R.rarity == 0:
                total_prob += 1
                current_prob.append(1)
            else:
                total_prob += 1/(3**R.rarity)
                current_prob.append(1/(3**R.rarity))
        final_prob = np.array(current_prob)/total_prob
        flag = True
        while flag: 
            room_options = np.random.choice(a=rooms,size=3,replace=False,p=final_prob)
            room1, room2, room3 = room_options
            flag = not(room1.cost == 0 or  room2.cost == 0 or room3.cost == 0)

        return room_options.tolist()

        
        