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
    if self.