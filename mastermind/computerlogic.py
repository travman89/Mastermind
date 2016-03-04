import random

class ComputerLogic:
  """Computer Logic for analyzing user input"""
  #this can be edited for different code complexity
  valid_letters = ['a','b','c','d','e','f']
  generated_guess = []
  guess_hint = []
  guess_tracker = {}
  guess_length = 0
  num_guesses = 0
  
  def __init__(this, code_length):
    this.guess_length = code_length
  
#generates the code for the player to guess
  def generate_code(this):
    this.generated_guess = []
    for i in range(this.guess_length):
      this.generated_guess.append(this.valid_letters[random.randint(0,5)])
  
#evaluates the user's guess and spits back the hint
  def evaluate_guess(this, user_guess):
  #reset the hint and guess tracker
    this.num_guesses+=1
    this.guess_hint = []
    this.guess_tracker = {}
  #check for correct guesses
    for i in range(len(user_guess)):
      if user_guess[i] == this.generated_guess[i]:
        this.guess_hint.append('*')
        if user_guess[i] in this.guess_tracker:
          this.guess_tracker[user_guess[i]] = this.guess_tracker[user_guess[i]] + 1
        else:
          this.guess_tracker[user_guess[i]] = 1
  #check for almost correct guesses
    for i in range(len(user_guess)):
    #if the guess is in the generated code and not equivalent to its counterpart
      if (user_guess[i] in this.generated_guess) and (user_guess[i] != this.generated_guess[i]):
        #check to see if it is already logged in dictionary
        if user_guess[i] in this.guess_tracker:
          #check to see
          if this.guess_tracker[user_guess[i]] < this.generated_guess.count(user_guess[i]):
            this.guess_hint.append('/')
            this.guess_tracker[user_guess[i]] = this.guess_tracker[user_guess[i]] + 1
        else:
          this.guess_hint.append('/')
          this.guess_tracker[user_guess[i]] = 1
    return this.guess_hint
  
  def get_guess_count(this):
    return this.num_guesses