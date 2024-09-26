from classes import player_inventory
from player_class import player

class item:
  def __init__(self, name, description):
    self.name = name 
    self.description = description

  def __str__(self):
    return f"{self.name}: {self.description}"


class room():
  def __init__(self, name, description, is_locked=False, key_required=None, can_break=False):
    self.name = name
    self.description = description
    self.exits = {}
    self.items = []
    self.is_locked = is_locked
    self.key_required = key_required
    self.can_break = can_break

  def add_exits(self, direction, location):
    self.exits[direction] = location

  def add_item(self, item):
    if item in self.item:
      self.item.append(item)
    else:
      print("Item already already in inventory.")

  def describe(self):
    print(f"You are in {self.name}, {self.description}.")
    if self.is_locked == True:
      print("Hmmm looks like this door is locked and requires a key to enter.")
    elif self.can_break == True:
      print("Hmmm this door is locked but it broken down with a crowbar.")
    else:
      if self.exits:
        print("In this room are the following exits:")

  def unlock(self):
    self.is_locked = False
    print(f"{self.name} has now been unlocked.")

  def break_open(self):
    self.is_locked = False
    print(f"Keys are for the weak, {self.name} is now broken down.")



class basement_cell(room):
  def __init__(self):
    super().__init__("Basement cell", "Dimly lit cold, dark room")

class locked_basement_hallway(room):
  def __init__(self):
    super().__init__("Basement hallway", "Dark hallway with flickering lights hanging from the roof", is_locked=True, key_required="Basement Hallway Key")

class basement_cell_air_vent(room):
  def __init__(self):
    super().__init__("Basement cell air vent", "Small, dark cramped air vent with something shining at the end... it's a key", can_break=True)
    key = item("Basement Hallway Key", "A rusty key that looks like it would in the door of the cell")
    self.add_item(key)
class end_basement_hallway(room):
  def __init__(self):
    super().__init__("End of basement hallway", "Looks like there's a dead end here... but there's something on the ground. Another key")
    key = item("Ground floor basement entrance key", "Newly cut shiny key")
    self.add_item(key)

class ground_floor_basement_entrance(room):
  def __init__(self):
    super().__init__("Ground floor basement entrance", "You can", is_locked=True, key_required="Ground floor basement entrance key")
    # possibly end the game here







class game:
  def __init__ (self):
    self.is_running = True
    self.player = player("Player")
    self.player_location = self.make_room()

  def make_room(self):
    basement_cell = basement_cell()
    locked_basement_hallway = locked_basement_hallway()
    basement_cell_air_vent = basement_cell_air_vent()
    end_basement_hallway = end_basement_hallway()
    ground_floor_basement_entrance = ground_floor_basement_entrance()


    basement_cell.add_exits("Open door", locked_basement_hallway)
    basement_cell.add_exits("Open air vent", basement_cell_air_vent)
    basement_cell_air_vent.add_exits("Return to cell", basement_cell)

    locked_basement_hallway.add_exits("Continue down hallway", end_basement_hallway)
    locked_basement_hallway.add_exits("Walk up staircase", ground_floor_basement_entrance)
    end_basement_hallway.add_exits("Return up hallway", locked_basement_hallway)

  def start_game(self):
    print("Welcome to Jack's house of horrors.")
    print("Start a new game or continue from save?") 
    player_input = input().strip().lower()
    if player_input == "new":
      self.main_game_loop
    elif player_input == "continue":
      print("yet to create")
      pass
    else:
      print("Invalid input, there are only two options it's not that hard lol.")

  def main_game_loop(self):
    while self.is_running:
      self.player_location.describe()
      command = input("Throughout this game you can follow the commands shown on screen or type 'quit' to exit at anytime: ").strip().lower()
      self.run_command(command)

  def run_command(self, command):
    if command == 'quit':
      self.exit_game()
    elif command == 'inventory':
      self.player.view_inventory()
    elif command == 'look':
      self.look_around()
  # continue with all commands from all rooms


  def exit_game(self):
    self.is_running = False
    print("Thank you playing. You are exiting the game...")

  def look_around(self):
    self.player_location.describe()

  def move_room(self, direction):
    pass

  def move_to_room(self, direction):
    if direction in self.player_location.exits:
      next_room = self.player_location.exits[direction]

      if next_room.is_locked:
        if self.player.has_item(next_room.key_required):
          print(f"Good job! You used {next_room.key_required} to open the door.")
          next_room.unlock()
        else:
          print("Hmmm it looks like this door is locked... try looking for a key.")
          return

      self.player_location = next_room
      print(f"You have now entered {direction}")  
    else:
      print("No, you can't go that way.")



if __name__ == "__main__":
    game = game()
    game.start_game()