from prompts import yes_no, int_input

class game:
  
  def __init__(self):
    self.mappool = []
    self.charpool = []
    
    self.game_name = input("Please enter the name of the game: ")
    self.player_num = int_input("Please enter the number of players that will play in each match: ")
    self.default_elo = int_input("Please enter the default elo of players for the game: ")
    
    #Maps
    self.has_mappool = False
    if yes_no("Does your game have a map pool?"):
      self.has_mappool = True
      self.add_map()

    #Characters
    self.has_charpool = False
    if yes_no("Does your game have a character pool?"):
      self.has_charpool = True
      #Adding Characters
      self.add_char()

  def add_map(self):
    #Adding Maps
      print("Please enter the maps you would like to add to the map pool. Type 'exit' and press enter to stop.")
      added_map = ""
      while added_map != "exit":
        added_map = input()
        self.mappool.append(added_map)
      self.mappool.pop()
  
  def add_char(self):
    #Adding Characters
      print("Please enter the characters you like to add to the character pool. Type 'exit' and press enter to stop.")
      added_char = ""
      while added_char != "exit":
        added_char = input()
        self.charpool.append(added_char)
      self.charpool.pop()
  
  def modify(self):
    if yes_no("Would you like to change the name of the game?"):
      self.game_name = input("Type new game name: ")
    
    if yes_no("Would you like to change player count of each match?"):
      self.player_num = int_input("Enter new player count: ")
    
    if yes_no("Would you like to change the default elo for new players?"):
      self.player_num = int_input("Enter new default elo: ")

    if self.has_mappool == True:
      if yes_no("Would you like to remove the map pool?"):
        self.has_mappool = False
        self.mappool.clear()
  
    if self.has_charpool == True:
      if yes_no("Would you like to remove the character pool?"):
        self.has_charpool = False
        self.charpool.clear()
    
    print("Game successfully modified!")