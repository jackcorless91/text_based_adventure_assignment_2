from classes import start_new_game, continue_save_game, reset_game, basement_corridor

def start_game():
  print("Welcome to Jack's house of horrors.")
  print("Start a new game or continue from save?")
  # menu_options = ["new", "continue"]
  # user_input = ""
  # for user_input in menu_options:
  print("Options: new/continue")
  user_input = input()
  if user_input == "new":
    print("starting new game...\n")
    start_new_game()
    new_game_test()
  elif user_input == "continue":
    print("Continuing from last save...\n")
    continue_save_game()
  else:
    print("Invalid input, there's 2 options its not that hard lol.")
# convert all to lower case, case insesitivty showing as invalid input

def new_game_test():
  print("New game has begun...")
  print("Let's start with your name: ")
  name = input()
  print(f"Good luck, {name}\n")
  print("You wake up in a dimly lit room with a cold concrete floor.")
  print("As you stand you notice a large windowless door and an air vent close to the bed.")
  print("What would you like to do?")
  print("Go for the door, check out vent or explore the room.")
  print("Options: door/vent/explore")

  options = ["door", "vent", "explore"]
  basement_room_key = False
  crowbar = False
  user_input = input()
  while user_input in options:
    if user_input == "door" and basement_room_key == False:
      print("Hmmm... locked.")
      print("looks like you need a key.")
      print("Better keep looking")
      break
    elif user_input == "door" and basement_room_key == True:
      print("Fits like a glove!")
      print("The door slowly creeks open and you find yourself in a hallway.")
      break
      basement_corridor()
      


start_game()

