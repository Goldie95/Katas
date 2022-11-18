# The getpass function allows users to enter an input that is not visible. See validatePassword function.
import getpass

password = ""
passwordGuess = ""
allowedGuesses = 5
welcome = """
************************************************************
*                                                          *
*            Welcome to the Weird Wordle Game              *
*                                                          *
************************************************************

"""

if __name__ == "__main__":
  while True:
    print(welcome)
    print("INSTRUCTIONS:")
    print("- This is a 2 player game.")
    print("- Player 1 will enter a password exactly 5 letters long.")
    print("- Player 2 will get chances to guess the password to win.")
    print(" ")
    print("KEY:")
    print("✔ - Letter is correct and in the correct position.")
    print("+ - Letter is correct but not in the correct position.")
    print("X - Letter is incorrect.")
    print(" ")
    print("Player 1 - Using only alphabetic letters, enter a 5 character password:")
      
 # This function will validate and retun the password (in uppercase) by checking if the input is:
 # 1. Alphabetic 
 # 2. 5 characters in length
 # It also uses the getpass function to hide the entry so player 2 cannot see the input.
    
    def validatePassword():
        validationPassed = False
        while validationPassed == False:
            password = getpass.getpass()
            if password.isalpha() == True and len(password) == 5:
                validationPassed == True
                return password.upper()
            else:
                print("You made a mistake, the password was either the wrong length or wasnt alaphabetic characters. Try again.")
 
 # This function will validate and return the guess (in uppercase) by checking if the input is:
 # 1. Alphabetic 
 # 2. 5 characters in length 
                 
    def validateGuess():
        validationComplete = False
        while validationComplete == False:
            passwordGuess = input()
            if passwordGuess.isalpha and len(passwordGuess) == 5:
                   validationComplete == True
                   return passwordGuess.upper()
            else:
                validationComplete == True
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
                pattern += "X"
        return ''.join(pattern)      
 
 # This function contains a while loop to iterate through the number of guesses and check has two possible outcomes
 # outcome 1 - Password is guessed correctly within the allowed guesses - Player 2 wins.
 # outcome 2 - Password isnt guessed correctly wihtin the allowed guesses - Player 1 wins and word is displayed.         
            
    def game():
        endofgame = False
        guessNumber = 1
        
        password = validatePassword()
        
        while endofgame == False:
            print("Guess number " + str(guessNumber))
            print("Player 2, please make your guess:")
            passwordGuess = validateGuess()
            pattern = checkGuess(password, passwordGuess)
            print (pattern)
            guessNumber = guessNumber + 1
        
            if password == passwordGuess:
                if guessNumber < (allowedGuesses + 1):
                    print ("Player 2 wins. It took you " + str(guessNumber - 1) + " guesses to find the weird wordle.")
                    print (" ")
                    endofgame = True
            elif password != passwordGuess:
                if guessNumber == (allowedGuesses +1):
                    print ("Player 1 wins. The word was '" + password + "'")
                    print (" ")
                    endofgame = True
            else:
                continue      
            
            
    game()
    
