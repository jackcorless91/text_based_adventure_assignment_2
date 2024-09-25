# from app import name

class start_new_game():
  pass

class continue_save_game():
  pass

class reset_game():
  pass

class basement_corridor():
  pass


class player_inventory:
  def __init__(self):
    self.items = []
  
  def add_item(self, item):
    self.items.append(item)
    print(f"{item} has been added to your inventory")

  def remove_item(self, item):
    if item in self.items:
      self.items.remove(item)
      print(f"{item} has been removed from your inventory")

  def view_inventory(self):
    if self.items:
      print("Current inventory contains: ")
      for item in self.items:
        print(f"| {item} |")
    else: 
      print("No items in your inventory :(.")

# player_inventory = player_inventory()
# player_inventory.add_item("Basement Key")
# player_inventory.add_item("Rusty Crowbar")


class game:
  def __init__(self):
    self.is_running = True
    self.inventory = player_inventory()

  def start_game(self):
    print("Welcome to Jack's house of horrors.")
    print("Start a new game or continue from save?")
    print("Options: new/continue")

    player_input = input().lower()

    if player_input == "new":
      print("Starting new game...\n")
      self.intro_game_loop()
    elif player_input == "continue":
      print("continuing from last save...")

  def intro_game_loop(self):
    while self.is_running:
      print("First, let's start with your name.")
      name = input()
      print(f"Firstly {name}, here are some universal commands you can access throughout your journey.")
      print("Options: exit, inventory.\n")
      print(f"Okay {name}, type 'start' to begin.\n")
      command = input().lower()
      self.player_commands(command)

      self.is_running = False
      #close loop for now bc havent written more
      

  def main_game_loop(self):
    print("You wake up in a dimly lit room on a cold concrete floor with nothing but a bed.")
    print("As you stand you notice a large windowless door and an air vent close to the bed.")
    print("What would you like to do?")
    print("Go for the door, check out vent or explore the room.")
    print("Options: door/vent/explore")
    


  # def player_commands(self, command):
  #   command = command.lower()
  #   if command == "exit":
  #     self.playing = False
  #     print("You are now exiting the game...")
  #   elif command == "inventory":
  #      self.inventory.view_inventory()
  #   if command == "start":
  #     print("starting your game...")
  #     print(f"Good luck.\n")
  #     self.main_game_loop()


  def player_commands(self, command):
    command = command.lower()

    command_options = {
      "look": self.look_around,
      "quit": self.quit_game,
      "inventory": self.inventory,
      "pick up": self.inventory.add_item,
      
      "north": self.direction.north,
      "south":self.direction.south,
      "east": self.direction.east,
      "west": self.direction.west

    }
    

  def move_new_location(self, direction):
    pass

 
if __name__ == "__main__":
  game = game()
  game.start_game()