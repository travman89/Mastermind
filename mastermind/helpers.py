import subprocess as sp

#validates the users guess
def guess_validation(user_input):
  valid_letters = ['a','b','c','d','e','f']
  if len(user_input) != 4:
    return False
  for letter in user_input:
    if letter not in valid_letters:
      return False
  return True
  
#prints greeting message
def greeting():
  sp.call('clear',shell=True)
  print("Welcome to Mastermind by Travis\n")
  print("The computer is going to generate a 4 letter code. That code will consist of letters [a,b,c,d,e,f]. It is your job to figure the code out! The computer will give you hints after every guess, and it is up to you to use those hints to break the code! A '*' means you have guessed a letter correctly in it's correct location. A '/' means you have guessed a letter correctly, but it is out of order. \nIf you need further instructions on how to play, visit the GitHub page.\n")
  print("Good luck code breakers!\n")

#takes in and validates the user guess
def user_guess():
  while(True):
    user_guess = raw_input("Enter in your code: ")
    if guess_validation(user_guess):
      return user_guess
    else:
      print("\nOOPS! You have entered in an invalid code. Make sure you enter in an all lower case 4 letter code that consists of the letters [a,b,c,d,e,f].\n")

#checks for the victory condition      
def check_win(hint, num_guesses):
  if len(hint) == num_guesses:
    for char in hint:
      if char != '*':
        return False
    return True
  else:
    return False

#displays the win message    
def win_message(guesses):
  print "\nCongratulations! You have discovered the secrent code %s guesses." % (str(guesses))