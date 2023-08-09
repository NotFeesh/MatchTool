def yes_no(question):
  response = ""
  while response != 'y' and response != 'n' and response != 'yes' and response != 'no':
    response = input(f'{str(question)} (y/n): ').lower()
  if response == 'y' or response == 'yes' return True else return False

def int_input(question):
  try:
    return int(input(question))
  except ValueError:
    print("Please enter a number!")
    int_input(question)