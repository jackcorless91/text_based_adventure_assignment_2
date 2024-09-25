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

  def start_game(self):
    print("Welcome to Jack's house of horrors.")
    print("Start a new game or continue from save?")
    print("Options: new/continue")

    player_input = input().lower()

    if player_input == "new":
      print("Starting new game...\n")
      self.main_game_loop()
    elif player_input == "continue":
      print("continuing from last save...")

  def main_game_loop(self):
    while self.is_running:
      print("First, let's start with your name.")
      name = input()
      print(f"Okay {name}, let's begin.")
      self.is_running = False
      


  def player_commands(self, command):
    command = command.lower()
    if command == "exit":
      self.playing = False
      print("You are now exiting the game...")
    elif command == "inventory":
      self.player_inventory.view_inventory()

 
if __name__ == "__main__":
  game = game()
  game.start_game()