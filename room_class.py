from item_class import Item
from player_class import Player

class Room:
    def __init__(self, name, description, is_locked=False, key_required=None):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.is_locked = is_locked
        self.key_required = key_required

    def add_exits(self, direction, location):
        self.exits[direction.lower()] = location

    def add_item(self, item):
        if item not in self.items:
            self.items.append(item)

    def describe(self):
        print(f"You are in {self.name}, {self.description}.")
        if self.is_locked:
            print("Hmm looks like this door is locked and requires a key to enter.")
        else:
            print("This exit is open.")
        
        if self.exits:
            print("In this room, you see the following exits:")
            for direction in self.exits.keys():
                print(f" - {direction}")

    def unlock(self):
        self.is_locked = False
        print(f"{self.name} has now been unlocked.")

class BasementCell(Room):
    def __init__(self):
        super().__init__("Basement cell", "Dimly lit, cold, dark room with nothing but a bed and a crowbar...")

class LockedBasementHallway(Room):
    def __init__(self):
        super().__init__("Basement hallway", "Dark hallway with flickering lights hanging from the roof", is_locked=True, key_required="Basement cell key")

class BasementCellAirVent(Room):
    def __init__(self):
        super().__init__("Basement cell air vent", "Small, dark cramped air vent with something shining at the end... it's a key.")
        self.cell_key = Item("Basement cell key", "A rusty key that looks like it would fit in the door of the cell.")
        self.add_item(self.cell_key)

    def collect_key(self, player):
        if self.cell_key in self.items:
            player.add_item(self.cell_key)
            self.items.remove(self.cell_key)

class EndBasementHallway(Room):
    def __init__(self):
        super().__init__("End of basement hallway", "Looks like there's a dead end here... but there's something on the ground. Another key!")
        self.ground_floor_key = Item("Ground floor key", "Newly cut shiny key.")
        self.add_item(self.ground_floor_key)

    def collect_key(self, player):
        if self.ground_floor_key in self.items:
            player.add_item(self.ground_floor_key)
            self.items.remove(self.ground_floor_key)

class GroundFloorBasementEntrance(Room):
    def __init__(self):
        super().__init__("Ground floor basement entrance", "Huge iron door at the top of the staircase.", is_locked=True, key_required="Ground floor key")