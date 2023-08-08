class game:
  
  def __init__(self):
    self.mappool = []
    self.charpool = []
    
    self.game_name = input("Please enter the name of the game: ")
    self.player_num = int(input("Please enter the number of players that will play in each match: ")) # fix this to deny invalid inputs
    self.default_elo = int(input("Please enter the default elo of players for the game: ")) # this too
    
    #Maps
    self.has_mappool = False
    response = ""
    while response != "y" and response != "n":
      response = input("Does your game have a map pool? (y/n): ")
    if response == "y":
      self.has_mappool = True
      #Adding Maps
      self.add_map()

    #Characters
    self.has_charpool = False
    response = ""
    while response != "y" and response != "n":
      response = input("Does your game have a character pool? (y/n): ")
    if response == "y":
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
    response = ""
    while response != "y" and response != "n":
      response = input("Would you like to change the name of the game? (y/n): ")
    if response == 'y':
      self.game_name = input("Type new game name: ")
    
    response = ""
    while response != "y" and response != "n":
      response = input("Would you like to change player count of each match? (y/n): ")
    if response == 'y':
      self.player_num = int(input("Enter new player number: "))
    
    response = ""
    while response != "y" and response != "n":
      response = input("Would you like to change the default elo for new players? (y/n): ")
    if response == 'y':
      self.player_num = int(input("Enter new default elo: "))

    response = ""
    while response != "y" and response != "n":
      response = input("Would you like to remove the map pool?: (y/n) ")
    if response == 'y':
      self.has_mappool = False
      self.mappool.clear()
    
    response = ""
    while response != "y" and response != "n":
      response = input("Would you like to remove the character pool?: (y/n) ")
    if response == 'y':
      self.has_charpool = False
      self.charpool.clear()