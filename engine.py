from inventory import Inventory
from rooms import Rooms
from Pioche import rooms, start_room, end_room
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
                 "cursor_color" : "white",
                 "locked" : None,
                 "room_option" : None,
                 "win" : False,
                 "lose" : False,
                 "nb_rooms" : 2}
        return input

    def initialize_map():
        start = start_room
        end = end_room
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
            Engine.__consume(current_input)
            # if we are in the process of creating a room
            if current_input["ask_Create_room"] : 
                new_input = Engine.__askCreateRoom(current_input)

            elif current_input["locked"] != None : 
                new_input = Engine.__unlock(current_input)

            else : 
                new_input = Engine.__move_player(current_input)
                

            
            if new_input["player_pos"] == [2, 0] : 
                new_input["win"] = True

            if new_input["inventory"].steps == 0  or Engine.__no_more_doors(new_input["map"]): 
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
                            moved_room = map[new_player_pos[1]][new_player_pos[0]]
                            new_input = moved_room.apply_effects(new_input)
                            

                #if the room dosn't exist => ask to create one
                elif map[new_player_pos[1]][new_player_pos[0]] == None: 
                    
                    new_input = Engine.__ask_unlock(current_input)
                    new_input["cursor"] = 0
                    
                    
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
        global rooms
        col,row = input["player_pos"]
        map = input["map"].copy()
        
        current_room = map[row][col]
        current_orient = input["player_orient"]
        current_room.doors[current_orient] = "open"

        match input["player_orient"]:
            case "N":
                new_room.orientation = 0
                Engine.__spin(new_room.doors,new_room.orientation)
                new_room = Engine.__lock_doors(input, new_room)
                map[row-1][col] = new_room
            case "S":
                new_room.orientation = 180
                Engine.__spin(new_room.doors,new_room.orientation)
                new_room = Engine.__lock_doors(input, new_room)
                map[row+1][col] = new_room
            case "W":
                new_room.orientation = 90
                Engine.__spin(new_room.doors,new_room.orientation)
                new_room = Engine.__lock_doors(input, new_room)
                map[row][col-1] = new_room
            case "E":
                new_room.orientation = -90
                Engine.__spin(new_room.doors,new_room.orientation)
                new_room = Engine.__lock_doors(input, new_room)
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
        inventory = current_input["inventory"]
        new_input = current_input.copy()

        cursor_color = "white" if room_option[cursor].cost <= inventory.gems else "red"

        if key == "RIGHT" : 
            cursor = min(cursor + 1, 2)
            
        elif key == "LEFT" : 
            cursor = max(cursor - 1, 0)

        elif key == "RETURN" or key == "SPACE" : 
            if room_option[cursor].cost <= inventory.gems :
                inventory.gems -= room_option[cursor].cost
                new_input["inventory"] = inventory
                new_input["ask_Create_room"] = False
                new_input["cursor"] = None
                new_input["room_option"] = None
                new_input["cursor_color"] = None
                new_input["nb_rooms"] += 1
                new_input["map"] = Engine.__create_room(current_input, room_option[cursor])
                rooms.remove(room_option[cursor])

        elif key == "ESCAPE":
            if inventory.dices != 0:
                new_input["room_option"] = Engine.__three_rooms()
                inventory.dices -= 1

        new_input["cursor"] = cursor
        new_input["cursor_color"] = cursor_color
        return new_input


    def __three_rooms():
        """
        Selects three rooms based on their rarity.

        Returns:
            list: list of the three room 
        """
        total_prob = 0
        current_prob = []
        for r in rooms:
            if r.rarity == 0:
                total_prob += 1
                current_prob.append(1)
            else:
                total_prob += 1/(3**r.rarity)
                current_prob.append(1/(3**r.rarity))
        final_prob = np.array(current_prob)/total_prob
        flag = True
        while flag: 
            room_options = np.random.choice(a=rooms,size=3,replace=False,p=final_prob)
            room1, room2, room3 = room_options
            flag = not(room1.cost == 0 or  room2.cost == 0 or room3.cost == 0)

        return room_options.tolist()
    
    def __no_more_doors(map : list) :
        lost_flag = True
        for i in range(5):
            if i == 2 : 
                previous_state = 0
            else : 
                previous_state = 0 if map[0][i] == None else 1

            for j in range(1, 9) : 

                if (i == 2 and j == 0) :
                    previous_state = 0
                else: 
                    state = 0 if map[j][i] == None else 1

                    if previous_state == 1 and state == 0 : 
                        doors = map[j-1][i].doors
                        lost_flag = lost_flag and doors["S"] == "none"

                    elif previous_state == 0 and state == 1 : 
                        doors = map[j][i].doors
                        lost_flag = lost_flag and doors["N"] == "none"

                    previous_state = state

        for i in range(9):
            previous_state = 0 if map[i][0] == None else 1

            for j in range(1, 5) : 
                if (j == 2 and i == 0) : 
                    previous_state = 0
                else :
                    state = 0 if map[i][j] == None else 1

                    if previous_state == 1 and state == 0 : 
                        doors = map[i][j-1].doors
                        lost_flag = lost_flag and doors["E"] == "none"

                    elif previous_state == 0 and state == 1 : 
                        doors = map[i][j].doors
                        lost_flag = lost_flag and doors["W"] == "none"

                    previous_state = state
        
        return lost_flag
    

    def __ask_unlock(current_input : dict) :
        pos = current_input["player_pos"]
        orient = current_input["player_orient"]
        map = current_input["map"]
        room = map[pos[1]][pos[0]]
        door = room.doors[orient]
        
        new_input = current_input.copy()

        if door == "locked" : 
            new_input["locked"] = 1
            new_input["cursor"] == 0
            print(1)
        elif door == "dlocked":
            new_input["locked"] = 2
            new_input["cursor"] == 0
            print(2)

        elif door == "open" : 
            new_input["cursor"] = 0
            new_input["ask_Create_room" ] = True
            new_input["room_option"] = Engine.__three_rooms()
            
        
        return new_input

        
    def __unlock(current_input : dict):

        inventory = current_input["inventory"]
        new_input = current_input.copy()
        cursor = current_input["cursor"]
        cursor_color = current_input["cursor_color"]
        locked = current_input["locked"]
        key = current_input["key_pressed"]

        if locked == 1 : 
            able_to_open = inventory.object_list.rabbit_foot or inventory.keys >= 1
        else : #locked == 2
            able_to_open = inventory.keys >= 2


        if key == "RIGHT" : 
            new_input["cursor"] = min(1, cursor + 1)
        elif key == "LEFT" : 
            new_input["cursor"] = max(0, cursor - 1)

        elif (key == "SPACE" or key == "RETURN") and cursor_color == "white" : # if the choice is possible

            if cursor == 0 : # no, the player doesn't want to open a room
                new_input["cursor"] = None
                new_input["locked"] = None
                return new_input
            else : #cursor == 1, the player want and can unlock the door
                map = new_input["map"]
                pos = new_input["player_pos"]
                orient = new_input["player_orient"]
                map[pos[1]][pos[0]].doors[orient] = "open"
                new_input["cursor"] = 0
                new_input["ask_Create_room" ] = True
                new_input["inventory"].keys -= locked
                new_input["locked"] = None
                new_input["room_option"] = Engine.__three_rooms()

        
        if new_input["cursor"] == 1 and not(able_to_open): 
            new_input["cursor_color"] = "red"
        else : 
            new_input["cursor_color"] = "white"

        return new_input



    def __lock_doors(input : dict, room : Rooms) :
        map = input["map"]
        nb_rooms = input["nb_rooms"]
        orient = input["player_orient"]

        for i in ["N", "S", "W", "E"] : 
            if (orient != i) and (room.doors[i] == "open") : 
                room.doors[i] = Engine.__is_door_locked(map, nb_rooms)
            
        return room


    def __is_door_locked(map : list, nb_room) : 
        
        list = ["open", "locked", "dlocked"]
        proba = [1 -  (3 * nb_room) / 100, (2 * nb_room) / 100, nb_room / 100]

        choix = np.random.choice(a = list, p = proba)

        return str(choix)
    
    def __consume(input : dict):
        key = input["key_pressed"]
        inv = input["inventory"]
        food = input["inventory"].object_list

        if key == "P" and food.apple > 0:
            inv.steps += 2
            food.apple -= 1
        elif key == "M" and food.banana > 0:
            inv.steps += 3
            food.banana -= 1
        elif key == "O" and food.cake > 0:  
            inv.steps += 10
            food.cake -= 1
        elif key == "L" and food.sandwich > 0:
            inv.steps += 15
            food.sandwich -= 1
        elif key == "K" and food.dinner > 0:
            inv.steps += 25
            food.dinner -= 1

