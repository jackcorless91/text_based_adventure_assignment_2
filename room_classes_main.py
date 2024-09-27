from classes import player_inventory
from player_class import player

class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def __str__(self):
        return f"{self.name}: {self.description}."



class Room():
  def __init__(self, name, description, is_locked=False, key_required=None, can_break=False, has_crowbar=False):
    self.name = name
    self.description = description
    self.exits = {}
    self.items = []
    self.is_locked = is_locked
    self.key_required = key_required
    self.can_break = can_break
    self.has_crowbar = has_crowbar

  def add_exits(self,direction, location):
    self.exits[direction] = location

  def add_item(self, item):
    if item not in self.items:
      self.items.append(item)
    else:
      print("Item already in inventory")