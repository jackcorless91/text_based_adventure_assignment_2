def start_game():
  print("Welcome to Jack's house of horrors.")
  print("Start a new game or continue from save?")
  menu_options = ["new", "continue"]
  user_input = ""
  for user_input in menu_options:
    print("Options: new/continue")
    user_input = input()
    if user_input == "new":
      print("new game")
      break
    elif user_input == "continue":
      print("continuing from last save")
      break
    else:
      print("Invalid input, there's 2 options its not that hard lol")


start_game()