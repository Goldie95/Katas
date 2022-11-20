# The getpass function allows users to enter an input that is not visible. See validatePassword function.
import getpass
import random
import csv
import os

password = ""
passwordGuess = ""
allowedGuesses = 5
wordlength = 5


# Below I used an ASCII art text generator https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
# Just copy and paste into a string varible, dont forget to use x3 quatation marks (""") at open and close to use multiline text.
welcome = """
*******************************************************************
*    __    __     _         _   __    __              _ _         *
*   / / /\ \ \___(_)_ __ __| | / / /\ \ \___  _ __ __| | | ___    *
*   \ \/  \/ / _ \ | '__/ _` | \ \/  \/ / _ \| '__/ _` | |/ _ \   *
*    \  /\  /  __/ | | | (_| |  \  /\  / (_) | | | (_| | |  __/   *
*     \/  \/ \___|_|_|  \__,_|   \/  \/ \___/|_|  \__,_|_|\___|   *
*                                                                 *
*                        1 Player Version                         *
*                                                                 *
*******************************************************************
"""
playerWins = """
__   __            _    _ _       
\ \ / /           | |  | (_)      
 \ V /___  _   _  | |  | |_ _ __  
  \ // _ \| | | | | |/\| | | '_ \ 
  | | (_) | |_| | \  /\  / | | | |
  \_/\___/ \__,_|  \/  \/|_|_| |_|
"""

playerLoses = """
__   __            _                    
\ \ / /           | |                   
 \ V /___  _   _  | |     ___  ___  ___ 
  \ // _ \| | | | | |    / _ \/ __|/ _ |
  | | (_) | |_| | | |___| (_) \__ \  __/
  \_/\___/ \__,_| \_____/\___/|___/\___|
"""
difficultyoptions = """To select your option please enter the bracketed number: 
(1) - Very Easy - 3 Letters
(2) -   Easy    - 4 Letters 
(3) -  Medium   - 5 Letters 
(4) -   Hard    - 6 Letters
(5) - Very Hard - 7 Letters"""

if __name__ == "__main__":
  while True:
    print(welcome)
    print("INSTRUCTIONS:")
    print("- This is a 1 player game.")
    print("- You have to 5 attempts to guess a randomly generated password.")
    print(" ")
    print("KEY:")
    print("✔ - Letter is correct and in the correct position.")
    print("+ - Letter is correct but not in the correct position.")
    print("x - Letter is incorrect.")
    print(" ")
      
 # This function will select the txt file depending on the difficulty rating chosen in def game and select a random word.
    
    def getrandomPassword(wordfile):
        with open (wordfile,'r') as filestream:
            for line in filestream:
                wordlist = line.split(",")
        password = (random.choice(wordlist))
        return password.upper()
        
 # This function will validate and return the guess (in uppercase) by checking if the input is:
 # 1. Alphabetic 
 # 2. The same length characters as the diffuclty chosen.
                 
    def validateGuess(difficulty):
        validationComplete = False
        while validationComplete == False:
            passwordGuess = input()
            if passwordGuess.isalpha() == True and len(passwordGuess) == (int(difficulty) + 2):
                   validationComplete == True
                   return passwordGuess.upper()
            else:
                print("You made a mistake, your guess was either the wrong length or wasnt alaphabetic characters. Try again.")
 
 # This function will check the users guess by enumerating through each letter using an index (i) and add a symbol to the pattern.
 # The pattern will then be joined to form the "wordle pattern".
            
    def checkGuess(password, passwordGuess):
        pattern = []
        for i, letter in enumerate(passwordGuess):
            if passwordGuess[i] == password[i]:
                pattern += "✔"
            elif letter in password:
                pattern += "+"
            else:
                pattern += "x"
        return ''.join(pattern)      
 
 # This function is to simply start a new game at the end of a completed game.
    def startOver():
        input("Press Enter to start a new game...")
 
 # This function contains a while loop to iterate through the number of guesses and check has two possible outcomes
 # outcome 1 - Password is guessed correctly within the allowed guesses - You win!
 # outcome 2 - Password isnt guessed correctly wihtin the allowed guesses - You Lose!      
            
    def game():
        endofgame = False
        guessNumber = 1
        difficultyList = ["Very Easy", "Easy", "Medium", "Hard", "Very Hard" ]
        currentDirectory = os.getcwd()
        
 # In this part of the def game fuction we letting the user select their difficulty.         
        print("Select your difficulty:")
        print (difficultyoptions)
        while True:
            difficulty = input(":")
            if int(difficulty) not in range(1,6):
                print("Error, Please select a diffuclty using the numbers assciated with the diffuclty setting.")
            else:
                print ("You have selected difficulty level '" + difficultyList[(int(difficulty)-1)] + "'")
                print ("Good Luck!")
                break
 # Here we are building the string to find the correct word txt file in the wordLists folder and using it to get a random word.
        wordfile = (currentDirectory + "/wordLists/" + str((int(difficulty)) + 2) + "LetterWords.txt")
        password = getrandomPassword(wordfile)
 #       print(password) # TEST ONLY
        while endofgame == False:
            print("------------------------------------")
            print("Attempt number " + str(guessNumber))
            print("Enter your guess:")
            passwordGuess = validateGuess(difficulty)
            pattern = checkGuess(password, passwordGuess)
            print (pattern)
            guessNumber = guessNumber + 1
        
            if password == passwordGuess and guessNumber <= (allowedGuesses + 1):
                    print (playerWins)
                    print ("It took you " + str(guessNumber - 1) + " attempt(s) to guess the weird wordle.")
                    print (" ")
                    endofgame = True
                    startOver()
            elif password != passwordGuess and guessNumber == (allowedGuesses + 1):
                    print (playerLoses)
                    print ("The word was '" + password + "'.")
                    print (" ")
                    endofgame = True
                    startOver()
            else:
                continue      
            
            
    game()
    
