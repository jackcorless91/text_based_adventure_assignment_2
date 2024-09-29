import pickle

from player_class import Player
from item_class import Item
from room_class import Room, BasementCell, LockedBasementHallway, BasementCellAirVent, EndBasementHallway, GroundFloorBasementEntrance

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
    
    def save_game(self):
        with open("savegame.pkl", "wb") as f:
            pickle.dump((self.player, self.player_location), f)
            print("Game saved!")

    def load_game(self):
        try:
            with open("savegame.pkl", "rb") as f:
                self.player, self.player_location = pickle.load(f)
                print("Game loaded!")
        except FileNotFoundError:
            print("No saved game found.")

    def start_game(self):
        print("Welcome to Jack's house of horrors.")
        print("Start a new game or continue from save?") 
        print("Avaliable commands: 'new', or 'continue'")
        player_input = input().strip().lower()
        if player_input == "new":
            player_name = input("Enter your player name: ")
            self.player = Player(player_name)
            self.player_location = self.create_room()
            self.main_game_loop()
        elif player_input == "continue":
            print("Yet to create this.")
            self.load_game()
            self.main_game_loop()
        else:
            print("Invalid input, there's only two options.")
      
    def main_game_loop(self):
        while self.is_running:
            self.player_location.describe()
            print("Available commands: 'quit', 'inventory', 'look', 'save', or enter one of the exits.")
            command = input("Enter your command: ").strip().lower()
            self.run_command(command)

    def run_command(self, command):
        if command == "quit":
            self.quit_game()
        elif command == 'inventory':
            self.player.view_inventory()
        elif command == "look":
            self.look_around()
        elif command == "save":
            self.save_game()
        elif command in self.player_location.exits:
            self.move_to_room(command)
        else:
            print("Invalid command.")

    def quit_game(self):
        self.is_running = False
        print("Thank you for playing. You are exiting the game...")

    def look_around(self):
        self.player_location.describe()

    def move_to_room(self, direction):
        next_room = self.player_location.exits[direction]

        if isinstance(self.player_location, BasementCellAirVent):
            self.player_location.collect_key(self.player)

        if isinstance(self.player_location, EndBasementHallway):
            self.player_location.collect_key(self.player)

        if next_room.is_locked:
            if self.player.has_item(next_room.key_required):
                print(f"Looks like you can use {next_room.key_required} to unlock the door.")
                next_room.unlock()
                self.player_location = next_room
                print(f"You have now entered {next_room.name}.")
                
                if isinstance(next_room, GroundFloorBasementEntrance):
                    print("Congratulations! You've escaped the basement!")
                    self.quit_game()
            else:
                print("Hmm looks like this door is locked, you need a key to open it. Keep looking...")
        else:
            self.player_location = next_room
            print(f"You have now entered {next_room.name}.")

if __name__ == "__main__":
    game = Game()
    game.start_game()
