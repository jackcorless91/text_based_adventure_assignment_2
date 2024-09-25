from classes import player_inventory

# class room:
#   def __init__(self, name, description):
#     self.name = name
#     self.description = description 
#     self.exits = {}

#   def room_exits(self, direction, location):
#     self.exits = [location]

#   def description(self):
#     print(f"You are in {self.name}. {self.description}")
#     if self.exits:
#       print("You can can see a way out")


# class cell(room):
#   def __init__(self):
#     super().__init__("cell", "")



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



class basement_cell(room):
  def __init__(self):
    super().__init__("Basement cell", "Dimly lit cold, dark room")


class basement_hallway(room):
  def __init__(self):
    super().__init__("Basement hallway", "Dark hallway with flickering lights hanging from the roof", is_locked=True, key_required="Basement Hallway Key")
