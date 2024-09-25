from app import name

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
      print("{name} contains: ")
    

  