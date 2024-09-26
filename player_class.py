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