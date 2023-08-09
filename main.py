from game import game_class
from pathlib import Path
from prompts import int_input, yes_no
import json
import os
from sys import exit

def load(object, attribute, default):
   try:
      return object[attribute]
   except KeyError:
      print(f"Error: {object['game_name']} has no '{attribute}' attribute. It was set to a default value of {default}.")
      return default

def save(games, save_path):
   data = []
   for game in games:
      temp = {}
      temp["game_name"] = game.game_name
      temp["version"] = game.version
      temp["player_num"] = game.player_num
      temp["default_elo"] = game.default_elo
      temp["has_mappool"] = game.has_mappool
      temp["has_charpool"] = game.has_charpool
      temp["mappool"] = game.mappool
      temp["charpool"] = game.charpool
      temp["players"] = game.players
      data.append(temp)
   with open(save_path, 'w') as file:
      json.dump(data, file, indent=2)

def main():
   current_version = 0.01

   games = []

   os.system('CLS')

   save_path = Path('./save.json')

   if save_path.exists():
      with open(save_path, 'r') as file:
         data = json.load(file) #to list of dictionaries
      
      for obj in data:
         try:
            game_name = obj['game_name']
         except KeyError:
            print("Error: One of the objects in your save file has no 'game_name' attribute, and was not loaded.")
            continue

         version = load(obj, 'version', current_version)
         player_num = load(obj, 'player_num', 0)
         default_elo = load(obj, 'default_elo', 0)
         has_mappool = load(obj, 'has_mappool', False)
         has_charpool = load(obj, 'has_charpool', False)
         mappool = load(obj, 'mappool', [])
         charpool = load(obj, 'charpool', [])
         players = load(obj, 'players', {})

         games.append(game_class(game_name, version, player_num, default_elo, has_mappool, has_charpool, mappool, charpool, players))


   print(f'''Welcome to MatchTool v{current_version}!
         
This tool is still under development, so many features are missing!
Enter 'help' to view a list of commands
         
Please don't forget to run 'save' before closing out of the application!
         ''')
   while True:
      args = input().split(' ')
      cmd = args[0]
      args.pop(0)

      if cmd == '':
         os.system('CLS')
      elif cmd == 'help':
         print('''
Here is a list of commands. For more information about each command, type '{cmd} help'.
      
game - creation and modification of different game types
               ''')
      elif cmd == 'game':
         try:
            if args[0] == 'create':
               name = input("Please enter the name of the game: ")

               player_num = int_input("Please enter the number of players that will play in each match: ")

               default_elo = int_input("Please enter the default elo of players for the game: ")

               has_mappool = False
               mappool = []
               if yes_no("Does your game have a map pool?"):
                  has_mappool = True
                  print("Please enter the maps you would like to add to the map pool. Type 'exit' and press enter to stop.")
                  added_map = ""
                  while added_map != "exit":
                     added_map = input()
                     mappool.append(added_map)
                  mappool.pop()

               has_charpool = False
               charpool = []
               if yes_no("Does your game have a character pool?"):
                  has_charpool = True
                  print("Please enter the characters you would like to add to the character pool. Type 'exit' and press enter to stop.")
                  added_char = ""
                  while added_char != "exit":
                     added_char = input()
                     charpool.append(added_char)
                  charpool.pop()

               games.append(game_class(name, current_version, player_num, default_elo, has_mappool, has_charpool, mappool, charpool))
               print("Game successfully created!\n")
            elif args[0] == 'help':
               print('''Here is more information about the game command and its arguments
            
game create - create a new game type
game list - prints a list of the games currently added
game detail {game} - prints the details of a specified game
game modify {game} - modify the match presets of the game type
                     ''')
            elif args[0] == 'modify':
               for game in games:
                  if game.game_name == args[1]:
                     os.system('CLS')
                     game.modify(current_version)
                     break
               else:
                  print("Error! That game does not exist.")
            elif args[0] == 'list':
               for game in games:
                  print(f'- {game.game_name}\n')
            elif args[0] == 'detail':
               for game in games:
                  if game.game_name == args[1]:
                     os.system('CLS')
                     print(f'''{game.game_name}
Version: {game.version} {"(Warning: This game is outdated! Please use 'game modify' to update it!)" if game.version < current_version else ''}
                           
Players per match: {game.player_num}

Default elo for starting players: {game.default_elo}
   ''')
                     if game.has_mappool:
                        print("Map Pool:")
                        for map in game.mappool:
                           print(f'{map}\n')
                     if game.has_charpool:
                        print("Char Pool:")
                        for char in game.charpool:
                           print(f'{char}\n')
                     if len(game.players) > 0:
                        print("Players:")
                        for player in game.players:
                           print(f'{player} - {game.players[player]}\n')
                     break
               else:
                  print("Error! That game does not exist.")
         except IndexError:
            print("Error: You did not provide enough arguments. Please use 'game help' to see proper usage of commands!")
            continue
      
      elif cmd == 'save':
         save(games, save_path)
      elif cmd == 'exit':
         exit()
      else:
         print("Command does not exist! Please use 'help' for a list of commands!")

if __name__ == "__main__":
    main()
            