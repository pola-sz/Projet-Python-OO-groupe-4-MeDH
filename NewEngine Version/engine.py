from inventory import Inventory
from rooms import Rooms, create_room, rooms
import copy
import numpy as np
import random

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
                 "lose" : False,
                 "blocked_rooms" : []}
        return input

    def __can_create_room(room: Rooms, inventory: Inventory) -> bool:
        """Check if a room can be created given the current inventory.
        Returns True if player has sufficient resources, False otherwise.
        """
        req = Engine.ROOM_CREATION_REQUIREMENTS.get(room.name)
        if not req:
            return True  # no requirements -> always allowed
        for k, amt in req.items():
            if getattr(inventory, k, 0) < amt:
                return False
        return True

    def __get_blocked_rooms(room_options: list, inventory: Inventory) -> list:
        """Return list of indices (0, 1, 2) that are blocked due to insufficient resources."""
        blocked = []
        for i, room in enumerate(room_options):
            if not Engine.__can_create_room(room, inventory):
                blocked.append(i)
        return blocked

    # Room event effects: mapping room name -> dict of modifications
    # positive numbers increase, negative decrease. 'items' is number of random items to give.
    ROOM_EVENT_EFFECTS = {
        # Blue
        'Pantry': {'coins': 4},
        'Den': {'gems': 1},
        'Trophy_room': {'gems': 8, 'coins': 5},
        'Ballroom': {'gems_set_to': 2},
        'Music Room': {'keys': 1},
        'Locker Room': {'keys': 1},
        'Freezer': {'effects_locked': True},
        'Garage': {'keys': 3},
        'Closet': {'items': 2, 'coins': 2},
        'Sauna': {'steps': 20},
        'Attic': {'items': 2},
        # Green
        'Morning Room': {'gems': 2},
        'Patio': {'gems': 4},
        'Secret Garden': {'steps': 8, 'coins': 1},
        'Terrace': {'green_costs_zero': True},
        'Veranda': {'items': 1},
        # Orange
        'Great Hall': {'keys': -4},
        # Purple
        'Bedroom': {'steps': 10, 'coins': 2},
        'Bunk Room': {'steps': 20, 'coins': 4},
        'Guest Bedroom': {'steps': 10},
        "Her Ladyship's Chamber": {'steps': 10, 'gems': 3, 'coins': 2},
        'Master Bedroom': {'steps': 10},
        'Nursery': {'steps': 5, 'coins': -2},
        "Servant's Quarters": {'keys': 2},
        # Red
        'Archives': {'keys': -4},
        'Chapel': {'coins': -5},
        'Gymnasium': {'steps': -10},
        'Furnace': {'steps': -10},
        'Weight Room': {'steps_divide': 2},
        # Yellow
        'Laundry Room': {'coins': -5}
    }

    # Requirements to create a room: resources that must be >= amount to allow placement
    ROOM_CREATION_REQUIREMENTS = {
        'Great Hall': {'keys': 4},
        'Archives': {'keys': 4},
        'Chapel': {'coins': 5},
        'Laundry Room': {'coins': 5},
        'Gymnasium': {'steps': 10},
        'Furnace': {'steps': 10},
        'Nursery': {'coins': 2},
        'Weight Room': {'steps': 2}
    }
    
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

        # Tie ESC to dices: if ESC pressed consume one dice; if none left, ignore ESC
        key = current_input.get("key_pressed")
        if key == "ESCAPE":
            inv = current_input.get("inventory")
            if inv and getattr(inv, 'dices', 0) > 0:
                inv.dices -= 1
                # allow ESC to continue as a key (e.g., to cancel create)
            else:
                # ignore ESC if no dices left
                new_input = current_input.copy()
                new_input["key_pressed"] = None
                return new_input

        if current_input["win"] or current_input["lose"] : 
            return current_input

        new_input = current_input.copy()

        #if we are still running the game
        if current_input["running"] :

            # if we are in the process of creating a room
            if current_input["ask_Create_room"] : 

                new_input = Engine.__askCreateRoom(current_input)
                
                # Check if all three rooms are blocked and no dices left
                blocked_rooms = new_input.get("blocked_rooms", [])
                if len(blocked_rooms) == 3 and new_input["inventory"].dices == 0:
                    new_input["lose"] = True

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
                            # apply room event if first time entering this instance
                            moved_room = map[new_player_pos[1]][new_player_pos[0]]
                            if moved_room is not None:
                                Engine.__apply_room_event(moved_room, new_input)
                    
                    
                    
                #if the room dosn't exist => ask to create one
                elif map[new_player_pos[1]][new_player_pos[0]] == None: 
                    
                    new_input["ask_Create_room"] = True
                    new_input["cursor"] = 0
                    new_input["room_option"] = Engine.__three_rooms()
                    # compute which rooms are blocked due to insufficient resources
                    new_input["blocked_rooms"] = Engine.__get_blocked_rooms(
                        new_input["room_option"], 
                        inventory
                    )
                    
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
        col,row = input["player_pos"]
        # work on a deep copy of the room so we don't mutate the original
        # room definitions (rooms pool). THat way the placed instance
        # keeps its own 'doors' dict and 'orientation' value
        new_room = copy.deepcopy(new_room)
        # canonical base doors snapshot so rotations are always computed
        # from the original template (!avoid cumulative rotations)
        new_room._base_doors = copy.deepcopy(new_room.doors)
        map = input["map"].copy()
        # Check creation requirements (resources) before actually placing the room
        inv = input.get('inventory')
        req = Engine.ROOM_CREATION_REQUIREMENTS.get(new_room.name)
        if req and inv:
            ok = True
            for k, amt in req.items():
                if getattr(inv, k, 0) < amt:
                    ok = False
                    break
            if not ok:
                # not enough resources -> do not place the room
                return map

        match input["player_orient"]:
            case "N":
                new_room.orientation = 0
                Engine.__apply_orientation(new_room)
                map[row-1][col] = new_room
            case "S":
                new_room.orientation = 180
                Engine.__apply_orientation(new_room)
                map[row+1][col] = new_room
            case "W":
                new_room.orientation = 90
                Engine.__apply_orientation(new_room)
                map[row][col-1] = new_room
            case "E":
                new_room.orientation = -90
                Engine.__apply_orientation(new_room)
                map[row][col+1] = new_room
        # If this room type already exists on the map, rotate previous placed
        # instances of the same room name by +90 degrees
        same_rooms = []
        for r in [c for row_ in map for c in row_ if c is not None]:
            if r.name == new_room.name:
                same_rooms.append(r)

        if len(same_rooms) > 1:
            # rotate previously placed instances only (do not rotate the newly
            # placed room again)
            for r in same_rooms:
                if r is new_room:
                    continue
                Engine.__rotate_room(r, 90)

        # 5% chance to find a random item when creating a room
        try:
            if random.random() < 0.05 and inv is not None:
                # choose a random attribute from inventory.object_list
                obj_attrs = [k for k, v in inv.object_list.__dict__.items()]
                if obj_attrs:
                    choice = random.choice(obj_attrs)
                    setattr(inv.object_list, choice, True)
        except Exception:
            pass

        return map

    def __rotate_room(room: Rooms, delta: int):
        """Rotate a placed room in-place by 'delta' degrees (multiple of 90)

        This updates both the 'orientation' value and the 'doors' dict so
        movement logic will reflect the visual rotation
        """
        # compute new orientation (normalize to multiples of 90)
        new_or = (room.orientation + delta) % 360
        # prefer -90 (270) to match existing code choices
        if new_or == 270:
            new_or = -90
        room.orientation = new_or
        Engine.__apply_orientation(room)

    def __apply_orientation(room: Rooms):
        """Apply the room.orientation to the room.doors based on the
        original base doors snapshot stored on the room instance
        """
        if hasattr(room, "_base_doors"):
            temp = room._base_doors.copy()
        else:
            temp = room.doors.copy()

        orientation = room.orientation
        match orientation:
            case 0:
                room.doors["N"] = temp["N"]
                room.doors["S"] = temp["S"]
                room.doors["W"] = temp["W"]
                room.doors["E"] = temp["E"]
            case 90:
                room.doors["N"] = temp["E"]
                room.doors["S"] = temp["W"]
                room.doors["W"] = temp["N"]
                room.doors["E"] = temp["S"]
            case 180:
                room.doors["N"] = temp["S"]
                room.doors["S"] = temp["N"]
                room.doors["W"] = temp["E"]
                room.doors["E"] = temp["W"]
            case -90:
                room.doors["N"] = temp["W"]
                room.doors["S"] = temp["E"]
                room.doors["W"] = temp["S"]
                room.doors["E"] = temp["N"]

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
                # No rotation: copy values from the temp snapshot back into the
                # original dict in-place. (Btw avoid rebinding 'doors', which would
                # only change the local name)
                doors["N"] = temp["N"]
                doors["S"] = temp["S"]
                doors["W"] = temp["W"]
                doors["E"] = temp["E"]
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

    def __apply_room_event(room: Rooms, input: dict):
        """Apply the defined event for the room instance once per placed instance.

        This mutates the input['inventory'] and input flags (effects_locked, green_costs_zero).
        """
        if hasattr(room, '_event_triggered') and room._event_triggered:
            return

        inv = input.get('inventory')
        if inv is None:
            return

        effects = Engine.ROOM_EVENT_EFFECTS.get(room.name)
        if not effects:
            room._event_triggered = True
            return

        # if effects_locked is set in input, skip positive effects
        locked = input.get('effects_locked', False)

        # helpers
        def give_items(n):
            attrs = [k for k in inv.object_list.__dict__.keys()]
            for _ in range(n):
                a = random.choice(attrs)
                setattr(inv.object_list, a, True)

        for k, v in effects.items():
            if k == 'items' and v > 0:
                give_items(v)
            elif k == 'gems_set_to':
                if not locked:
                    inv.gems = v
            elif k == 'steps_divide':
                # divide steps by v
                inv.steps = max(0, inv.steps // v)
            elif k == 'effects_locked' and v:
                input['effects_locked'] = True
            elif k == 'green_costs_zero' and v:
                input['green_costs_zero'] = True
            else:
                # numeric change
                if isinstance(v, int):
                    if v >= 0:
                        if not locked:
                            if hasattr(inv, k):
                                setattr(inv, k, getattr(inv, k, 0) + v)
                    else:
                        # negative change always applies (deduction)
                        if hasattr(inv, k):
                            setattr(inv, k, max(0, getattr(inv, k, 0) + v))

        room._event_triggered = True

    def __askCreateRoom(current_input : dict) :
        cursor = current_input["cursor"]
        key = current_input["key_pressed"]
        room_option = current_input["room_option"]
        new_input = current_input.copy()
        blocked_rooms = current_input.get("blocked_rooms", [])

        if key == "RIGHT" : 
            cursor = min(cursor + 1, 2)
            # skip blocked rooms
            while cursor in blocked_rooms and cursor < 2:
                cursor += 1
        elif key == "LEFT" : 
            cursor = max(cursor - 1, 0)
            # skip blocked rooms
            while cursor in blocked_rooms and cursor > 0:
                cursor -= 1
        elif key == "RETURN" or key == "SPACE" : 
            # only allow selecting non-blocked rooms
            if cursor not in blocked_rooms:
                new_input["ask_Create_room"] = False
                new_input["cursor"] = None
                new_input["room_option"] = None
                new_input["blocked_rooms"] = []
                new_input["map"] = Engine.__create_room(current_input, room_option[cursor])
            # else: do nothing, room is blocked
        elif key == "ESCAPE":
            new_input["ask_Create_room"] = False
            new_input["cursor"] = None
            new_input["room_option"] = None
            new_input["blocked_rooms"] = []
            
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

        
        
