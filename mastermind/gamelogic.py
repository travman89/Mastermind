from helpers import user_guess, greeting, check_win, win_message
from computerlogic import ComputerLogic
    
#game loop
def game_loop():
  num_guesses = 4
  greeting()
  computer_logic = ComputerLogic(num_guesses)
  computer_logic.generate_code()
  
  while(True):
    hint = computer_logic.evaluate_guess(user_guess())
    if check_win(hint, num_guesses):
      win_message(computer_logic.get_guess_count())
      break
    else:
      print ("\nYour hint is: " + str(hint))
      
      
      
      
    
    