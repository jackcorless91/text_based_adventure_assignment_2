from classes import player_inventory
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