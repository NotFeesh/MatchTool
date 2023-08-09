from game import game
import os

games = []

os.system('CLS')
print('''
Welcome to MatchTool v0.0!
      
This tool is still under development, so many features are missing!
Enter 'help' to view a list of commands
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
            
      game - creation and modification of different game types''')
   elif cmd == 'game':
      try:
         if args[0] == 'create':
            games.append(game())
            print('Successfully created game!')
         elif args[0] == 'modify':
            for game in games:
               if game.game_name == args[1]:
                  os.system('CLS')
                  game.modify()
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
                  break
            else:
               print("Error! That game does not exist.")
         elif args[0] == 'help':
            print('''
Here is more information about the game command and its arguments
         
game create - create a new game type
game list - prints a list of the games currently added
game detail {game} - prints the details of a specified game
game modify {game} - modify the match presets of the game type
game add player {game} {player} - add a player to the game's list of players
game add map {game} {map} - add a map tothe game's map pool
game add character {game} {character} - add a character to the character's character pool
game remove player {game} {player} - remove a player from the game's list of players
game remove map {game} {map} - remove a map from the game's map pool
game remove character {game} {character} - removed a character from the game's character pool
                  ''')
      except IndexError:
         print("Error: You did not provide enough arguments. Please use 'game help' to see proper usage of commands!")
         continue
   else:
      print("Command does not exist! Please use 'help' for a list of commands!")
            