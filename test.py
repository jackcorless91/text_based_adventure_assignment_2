class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

class Room:
    def __init__(self, name, description, is_locked=False, required_key=None):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []  # List to hold items in the room
        self.is_locked = is_locked
        self.required_key = required_key

    def add_exit(self, direction, room):
        if direction in self.exits:
            print(f"Cannot add exit in direction {direction}; it already exists.")
        else:
            self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def describe(self):
        print(f"You are in {self.name}. {self.description}")
        if self.items:
            print("You see the following items:")
            for item in self.items:
                print(f"- {item}")
        if self.is_locked:
            print("The room is locked. You need a key to enter.")
        else:
            if self.exits:
                print("You can see the following exits:")
                for direction in self.exits.keys():
                    print(f"- {direction.capitalize()}")

    def unlock(self):
        self.is_locked = False
        print(f"{self.name} is now unlocked.")

class Kitchen(Room):
    def __init__(self):
        super().__init__("Kitchen", "A cozy kitchen filled with the smell of fresh bread.")
        key = Item("Golden Key", "A shiny golden key that unlocks the locked room.")
        self.add_item(key)

class Hallway(Room):
    def __init__(self):
        super().__init__("Hallway", "A long, dimly lit hallway.")

class Library(Room):
    def __init__(self):
        super().__init__("Library", "A quiet library filled with ancient books.")
        book = Item("Ancient Tome", "An old book filled with forgotten knowledge.")
        self.add_item(book)

class Garden(Room):
    def __init__(self):
        super().__init__("Garden", "A beautiful garden filled with colorful flowers.")
        flower = Item("Flower", "A vibrant flower with a sweet fragrance.")
        self.add_item(flower)

class Bedroom(Room):
    def __init__(self):
        super().__init__("Bedroom", "A serene bedroom with a comfortable bed.")
        note = Item("Note", "A note that says 'Find the key!'.")
        self.add_item(note)

class LockedRoom(Room):
    def __init__(self):
        super().__init__("Locked Room", "A mysterious locked room.", is_locked=True, required_key="golden key")

class Character:
    def __init__(self, name):
        self.name = name
        self.inventory = []  # Player's inventory

    def add_item(self, item):
        self.inventory.append(item)
        print(f"You picked up {item.name}.")

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"You dropped {item.name}.")
        else:
            print(f"You don't have a {item.name}.")

    def has_item(self, item_name):
        return any(item.name.lower() == item_name.lower() for item in self.inventory)

    def show_inventory(self):
        if self.inventory:
            print("You have the following items:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")

class Game:
    def __init__(self):
        self.is_running = True
        self.player = Character("Hero")
        self.current_location = self.create_rooms()

    def create_rooms(self):
        kitchen = Kitchen()
        hallway = Hallway()
        library = Library()
        garden = Garden()
        bedroom = Bedroom()
        locked_room = LockedRoom()

        # Set exits
        kitchen.add_exit("north", hallway)
        hallway.add_exit("south", kitchen)
        hallway.add_exit("east", library)
        hallway.add_exit("west", garden)
        hallway.add_exit("up", bedroom)  # Adding a new exit to the bedroom
        bedroom.add_exit("down", hallway)
        library.add_exit("west", hallway)
        library.add_exit("north", locked_room)
        locked_room.add_exit("south", library)

        return kitchen  # Start in the kitchen

    def start(self):
        print("Welcome to the Adventure Game!")
        self.main_loop()

    def main_loop(self):
        while self.is_running:
            self.current_location.describe()
            command = input("Enter a command (or 'quit' to exit): ").strip().lower()
            self.handle_command(command)

    def handle_command(self, command):
        if command == 'quit':
            self.quit_game()
        elif command == 'look':
            self.look_around()
        elif command.startswith('go '):
            self.move_to_location(command[3:])
        elif command.startswith('take '):
            self.take_item(command[5:])
        elif command == 'inventory':
            self.player.show_inventory()
        else:
            print("I don't understand that command.")

    def quit_game(self):
        self.is_running = False
        print("Thanks for playing!")

    def look_around(self):
        self.current_location.describe()

    def move_to_location(self, direction):
        if direction in self.current_location.exits:
            next_room = self.current_location.exits[direction]

            if next_room.is_locked:
                if self.player.has_item(next_room.required_key):
                    print(f"You use the {next_room.required_key} to unlock the door.")
                    next_room.unlock()
                else:
                    print("The door is locked. You need a key to enter.")
                    return

            self.current_location = next_room
            print(f"You go {direction}.")
        else:
            print("You can't go that way.")

    def take_item(self, item_name):
        for item in self.current_location.items:
            if item.name.lower() == item_name.lower():
                self.player.add_item(item)
                self.current_location.remove_item(item)
                return
        print(f"There is no {item_name} here.")

if __name__ == "__main__":
    game = Game()
    game.start()