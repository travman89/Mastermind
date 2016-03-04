# Mastermind
Small text based representation of the game Mastermind written in python

#How to Play
Mastermind is a code breaking game where the player is tasked with breaking a code by using clues given to them by the other player. This rendition of the game generates a code that is 4 characters long and consists of the letters [a,b,c,d,e,f]. Codes can have multiples of the same letter, so while a code could be 'fced' it could also be 'aaaa'. After you guess the computer player will give you a hint representing how close you got to guessing the correct code. A '*' means that you have guessed a letter correctly and in the correct order in the code.  A '/' means that you have guessed a letter correctly, but it is in the wrong spot. Let's look at an example of how the computer's algorithm generates the hints.

For this example we will be using the computer generated code of 'bdcd'.

For our first guess we will enter in 'abcd'. The computer will spit back ['*','/','/'] since we guessed only 1 letter correctly in its correct spot and 2 more letters correctly in incorrect spots. We will now use this information to further narrow down our code guesses.

For our next guess we will enter in 'eeee'. The computer will spit back [] as the hint since the code does not contain any 'e' characters. We can now eliminate 'e' from all of our future guesses.

After several rounds of guessing you should be honing in on the correct code, and once you have broken it, the computer will signal that you have won.

#Setup
The game is written in python, so to play simply navigate to the mastermind directory and run the following command:
>python mastermind.py

