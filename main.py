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
      if args[0] == 'create':
         games.append(game())
         print('Successfully created game!')
      elif args[0] == 'modify':
         for game in games:
            if game.game_name == args[1]:
               os.system('CLS')
               game.modify()
               break
      elif args[0] == 'help':
         print('''
      Here is more information about the game command and its arguments
               
      game create - create a new game type
      game modify {modify_this_game} - modify the match presets of the game type
      game add player {game} {player} - add a player to the game's list of players
      game add map {game} {map} - add a map to the game's map pool
      game add character {game} {character} - add a character to the character's character pool
      game remove player {game} {player} - remove a player from the game's list of players
      game remove map {game} {map} - remove a map from the game's map pool
      game remove character {game} {character} - removed a character from the game's character pool
               ''')
            