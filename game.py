from prompts import yes_no, int_input

class game_class:
  
  def __init__(self, name, version, player_num=0, default_elo=0, has_mappool=False, has_charpool=False, mappool=[], charpool=[], players={}):
    self.game_name = name
    self.version = version
    self.player_num = player_num
    self.default_elo = default_elo
    self.has_mappool = has_mappool
    self.has_charpool = has_charpool
    self.mappool = mappool
    self.charpool = charpool
    self.players = players

  def add_map(self):
    #Adding Maps
      print("Please enter the maps you would like to add to the map pool. Type 'exit' and press enter to stop.")
      added_map = ""
      while added_map != "exit":
        added_map = input()
        self.mappool.append(added_map)
      self.mappool.pop()
  
  def remove_map(self):
    print("Please enter the characters you would like to remove from the character pool. Type 'exit' and press enter to stop.")
    removed_char = ""
    while removed_char != 'exit':
      removed_char = input()
      try: 
        self.mappool.pop(removed_char)
      except IndexError:
        print(f"Error: No character by name {removed_char} found!")
  
  def add_char(self):
    #Adding Characters
      print("Please enter the characters you like to add to the character pool. Type 'exit' and press enter to stop.")
      added_char = ""
      while added_char != "exit":
        added_char = input()
        self.charpool.append(added_char)
      self.charpool.pop()
  
  def remove_char(self):
    print("Please enter the characters you would like to remove from the character pool. Type 'exit' and press enter to stop.")
    removed_char = ""
    while removed_char != 'exit':
      removed_char = input()
      try: 
        self.charpool.pop(removed_char)
      except IndexError:
        print(f"Error: No character by name {removed_char} found!")
  
  def add_player(self):
    print("Please enter the names of the players you would like to add to the game. Type 'exit' and press enter to stop.")
    added_player = ""
    while added_player != "exit":
      added_player = input()
      self.players[added_player] = self.default_elo
    self.players.popitem()
  
  def remove_player(self):
    print("Please enter the names of the players you would like to remove from the game. Type 'exit' and press enter to stop.")
    removed_player = ""
    while removed_player != "exit":
      for key in self.players:
        self.players.pop(removed_player, None)
  
  def remove_player(self):
    player_name = input(f"Please ")
  
  def modify(self, current_version):
    if yes_no("Would you like to change the name of the game?"):
      self.game_name = input("Type new game name: ")
    
    if yes_no("Would you like to change player count of each match?"):
      self.player_num = int_input("Enter new player count: ")
    
    if yes_no("Would you like to change the default elo for new players?"):
      self.default_elo = int_input("Enter new default elo: ")
    
    if yes_no("Would you like to add players to the game?"):
      self.add_player()
    
    if yes_no("Would you like to remove players from the game?"):
      self.remove_player()

    if self.has_mappool == True:
      if yes_no("Would you like to remove the map pool?"):
        self.has_mappool = False
        self.mappool.clear()
    else:
      if yes_no("Woud you like to add a map pool?"):
        self.has_mappool = True
        self.add_map()
  
    if self.has_charpool == True:
      if yes_no("Would you like to remove the character pool?"):
        self.has_charpool = False
        self.charpool.clear()
    else:
      if yes_no("Would you like to add a character pool?"):
        self.has_charpool = True
        self.add_char()
    
    self.version = current_version
    
    print("Game successfully modified!")
