class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item.name} has been added to your inventory.")

    def view_inventory(self):
        if self.inventory:
            print("Current inventory contains:")
            for item in self.inventory:
                print(f" - {item.name}.")
        else: 
            print("No items in your inventory :(.")

    def has_item(self, item_name):
        return any(item.name.lower() == item_name.lower() for item in self.inventory)

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}."

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

class Game:
    def __init__(self):
        self.is_running = True
        self.player = Player("Player")
        self.player_location = self.create_room()

    def create_room(self):
        basement_cell = BasementCell()
        locked_basement_hallway = LockedBasementHallway()
        basement_cell_air_vent = BasementCellAirVent()
        end_basement_hallway = EndBasementHallway()
        ground_floor_basement_entrance = GroundFloorBasementEntrance()

        basement_cell.add_exits("open door", locked_basement_hallway)
        basement_cell.add_exits("open air vent", basement_cell_air_vent)
        basement_cell_air_vent.add_exits("return to cell", basement_cell)

        locked_basement_hallway.add_exits("continue down hallway", end_basement_hallway)
        locked_basement_hallway.add_exits("walk up staircase", ground_floor_basement_entrance)
        end_basement_hallway.add_exits("return to hallway", locked_basement_hallway)

        return basement_cell

    def start_game(self):
        print("Welcome to Jack's house of horrors.")
        print("Start a new game or continue from save?") 
        player_input = input().strip().lower()
        if player_input == "new":
            self.main_game_loop()
        elif player_input == "continue":
            print("Yet to create this.")
            self.is_running = False
        else:
            print("Invalid input, there's only two options. You can do it lol.")
      
    def main_game_loop(self):
        while self.is_running:
            self.player_location.describe()
            print("Available commands: 'quit', 'inventory', 'look', or one of the exits.")
            command = input("Enter your command: ").strip().lower()
            self.run_command(command)

    def run_command(self, command):
        if command == "quit":
            self.quit_game()
        elif command == 'inventory':
            self.player.view_inventory()
        elif command == "look":
            self.look_around()
        elif command in self.player_location.exits:
            self.move_to_room(command)
        else:
            print("Invalid command or direction.")

    def quit_game(self):
        self.is_running = False
        print("Thank you for playing. You are exiting the game...")

    def look_around(self):
        self.player_location.describe()

    def move_to_room(self, direction):
        next_room = self.player_location.exits[direction]

        # Check if entering the air vent room to collect the key
        if isinstance(self.player_location, BasementCellAirVent):
            self.player_location.collect_key(self.player)

        # Check if entering the end of basement hallway to collect the key
        if isinstance(self.player_location, EndBasementHallway):
            self.player_location.collect_key(self.player)

        if next_room.is_locked:
            if self.player.has_item(next_room.key_required):
                print(f"Looks like you can use {next_room.key_required} to unlock the door.")
                next_room.unlock()
                self.player_location = next_room
                print(f"You have now entered {next_room.name}.")
                
                # End the game when entering the Ground floor basement entrance
                if isinstance(next_room, GroundFloorBasementEntrance):
                    print("Congratulations! You've escaped the basement!")
                    self.quit_game()
            else:
                print("Hmm looks like this door is locked, you need a key to open it.")
        else:
            self.player_location = next_room
            print(f"You have now entered {next_room.name}.")

if __name__ == "__main__":
    game = Game()
    game.start_game()
