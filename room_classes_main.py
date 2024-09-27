class player():
  def __init__(self, name):
    self.name = name
    self.inventory = []

  def add_item(self, item):
    self.inventory.append(item)
    print(f"{item} has been added to your inventory")

  def view_inventory(self):
    if self.inventory:
      print("Current inventory contains: ")
      for item in self.inventory:
        print(f" {item}.")
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
  def __init__(self, name, description, is_locked=False, key_required=None, locked_can_break=False, has_crowbar=False):
    self.name = name
    self.description = description
    self.exits = {}
    self.items = []
    self.is_locked = is_locked
    self.key_required = key_required
    self.can_break = locked_can_break
    self.has_crowbar = has_crowbar

  def add_exits(self,direction, location):
    self.exits[direction] = location

  def add_item(self, item):
    if item not in self.items:
      self.items.append(item)
    else:
      print("Item already in inventory")
  
  def describe(self):
    print(f"You are in {self.name}, {self.description}.")
    if self.is_locked == True:
      print("Hmm looks like this door is locked and requires a key to enter.")
    elif self.locked_can_break == True:
      print("Hmm looks like this door is locked... but maybe it can be broken down?")
    else:
      if self.exits:
        print("In this room you see the following exits: ")
        for direction in self.exits.keys():
          print(f"{direction}")
          # low key dont understand this part
  
  def unlock(self):
    self.is_locked = False
    print(f"{self.name} has now been unlocked.")

  def break_open(self):
    self.locked_can_break = False
    print(f"Keys are for the weak, {self.name} is now broken down.")


class BasementCell(Room):
  def __init__(self):
    super().__init__("Basement cell", "Dimly lit, cold, dark room with nothing but a bed and a crowbar...", has_crowbar=True)

class LockedBasementHallway(Room):
  def __init__(self):
    super().__init__("Basement hallway", "Dark hallway with flickering lights hanging from the roof", is_locked=True, key_required="Basement cell key")

class BasementCellAirVent(Room):
  def __init__(self):
    super().__init__("Basement cell air vent", "Small, dark cramped air vent with something shining at the end... it's a key", locked_can_break=True)
    cell_key = Item("Basement cell key", "A rusty key that looks like it would in the door of the cell")
    self.add_item(cell_key)

class EndBasementHallway(Room):
  def __init__(self):
    super().__init__("End of basement hallway", "Looks like there's a dead end here... but there's something on the ground. Another key!")
    ground_floor_key = Item("Ground floor key", "Newly cut shiny key")
    self.add_item(ground_floor_key)

class GroundFloorBasementEntrance(Room):
  def __init__(self):
    super().__init__("Ground floor basement entrance", "Huge iron door at the top of the staircase.", is_locked=True, key_required="Ground floor key")
    #potential to end the game here if i run out of time 


class Game:
  def __init__(self):
    self.is_running = True
    self.player = player("Player")
    self.player_location = self.create_room()

  def create_room(self):
    basement_cell = BasementCell()
    locked_basement_hallway = LockedBasementHallway()
    basement_cell_air_vent = BasementCellAirVent()
    end_basement_hallway = EndBasementHallway()
    ground_floor_basement_entrance = GroundFloorBasementEntrance()

    basement_cell.add_exits("Open door", locked_basement_hallway)
    basement_cell.add_exits("Open air vent", basement_cell_air_vent)
    basement_cell_air_vent.add_exits("Return to cell", basement_cell)

    locked_basement_hallway.add_exits("Continue down hallway", end_basement_hallway)
    locked_basement_hallway.add_exits("Walk up staircase", ground_floor_basement_entrance)
    end_basement_hallway.add_exits("Return to hallway", locked_basement_hallway)

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
      command = input("Throughout this game you can follow the commands shown on screen or type 'quit' to exit at anytime: ").strip().lower()
      self.run_command(command)

  def run_command(self, command):
    if command == "quit":
      self.quit_game()
    elif command == 'inventory':
      self.player.view_inventory()
    elif command == "look":
      self.look_around()
    elif command.startwith("Take me to "):
      self.move_to_room(command[10:])

  def quit_game(self):
    self.is_running = False
    print("Thank you playing. You are exiting the game...")

  def look_around(self):
    self.player_location.describe()

  def move_to_room(self, direction):
    if direction in self.player_location.exits:
      next_room = self.player_location.exits[direction]

      if next_room.is_locked:
        if self.player.has_item(next_room.key_required):
          print(f"Looks like you can use {next_room.key_required} to unlock the door.")
          next_room.unlock()
      elif next_room.locked_can_break:
        if self.player.has_item(next_room.locked_can_break):
          print(f"Who needs keys? not us. Yo can use {next_room.locked_can_break} to break it open")
      else:
        print("Hmm looks like this door is locked, you need a key to open it.")
        return 
      
      self.player_location = next_room
      print(f"Looks like you can go {direction}.")
    else:
      ("Uh oh! You can't go that way")

if __name__ == "__main__":
  game = Game()
  game.start_game()