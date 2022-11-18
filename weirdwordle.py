# The getpass function allows users to enter an input that is not visible. See validatePassword function.
import getpass

password = ""
passwordGuess = ""
allowedGuesses = 5
wordlength = 5

# Below I used an Ascii art text generator https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
# Just copy and paste into a string varible, dont forget to use x3 quatation marks (""") at open and close to use multiline text.
welcome = """
*******************************************************************
*    __    __     _         _   __    __              _ _         *
*   / / /\ \ \___(_)_ __ __| | / / /\ \ \___  _ __ __| | | ___    *
*   \ \/  \/ / _ \ | '__/ _` | \ \/  \/ / _ \| '__/ _` | |/ _ \   *
*    \  /\  /  __/ | | | (_| |  \  /\  / (_) | | | (_| | |  __/   *
*     \/  \/ \___|_|_|  \__,_|   \/  \/ \___/|_|  \__,_|_|\___|   *
*                                                                 *
*******************************************************************
"""
playerOneWins = """
______ _                         __    _    _ _           _ 
| ___ \ |                       /  |  | |  | (_)         | |
| |_/ / | __ _ _   _  ___ _ __  `| |  | |  | |_ _ __  ___| |
|  __/| |/ _` | | | |/ _ \ '__|  | |  | |/\| | | '_ \/ __| |
| |   | | (_| | |_| |  __/ |    _| |_ \  /\  / | | | \__ \_|
\_|   |_|\__,_|\__, |\___|_|    \___/  \/  \/|_|_| |_|___(_)
                __/ |                                       
               |___/ 
"""

playerTwoWins = """
______ _                         _____   _    _ _           _ 
| ___ \ |                       / __  \ | |  | (_)         | |
| |_/ / | __ _ _   _  ___ _ __  `' / /' | |  | |_ _ __  ___| |
|  __/| |/ _` | | | |/ _ \ '__|   / /   | |/\| | | '_ \/ __| |
| |   | | (_| | |_| |  __/ |    ./ /___ \  /\  / | | | \__ \_|
\_|   |_|\__,_|\__, |\___|_|    \_____/  \/  \/|_|_| |_|___(_)
                __/ |                                         
               |___/
"""

if __name__ == "__main__":
  while True:
    print(welcome)
    print("INSTRUCTIONS:")
    print("- This is a 2 player game.")
    print("- Player 1 will enter a password exactly 5 letters long.")
    print("- Player 2 will get 5 chances to guess the password to win.")
    print(" ")
    print("KEY:")
    print("✔ - Letter is correct and in the correct position.")
    print("+ - Letter is correct but not in the correct position.")
    print("x - Letter is incorrect.")
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
            if password.isalpha() == True and len(password) == wordlength:
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
            if passwordGuess.isalpha() == True and len(passwordGuess) == wordlength:
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
 # outcome 1 - Password is guessed correctly within the allowed guesses - Player 2 wins.
 # outcome 2 - Password isnt guessed correctly wihtin the allowed guesses - Player 1 wins and word is displayed.         
            
    def game():
        endofgame = False
        guessNumber = 1
        
        password = validatePassword()
        
        while endofgame == False:
            print("------------------------------------")
            print("Attempt number " + str(guessNumber))
            print("Player 2, please make your guess:")
            passwordGuess = validateGuess()
            pattern = checkGuess(password, passwordGuess)
            print (pattern)
            guessNumber = guessNumber + 1
        
            if password == passwordGuess:
                if guessNumber < (allowedGuesses + 1):
                    print (playerTwoWins)
                    print ("It took you " + str(guessNumber - 1) + " attempt(s) to guess the weird wordle.")
                    print (" ")
                    endofgame = True
                    startOver()
            elif password != passwordGuess:
                if guessNumber == (allowedGuesses +1):
                    print (playerOneWins)
                    print ("The word was '" + password + "'.")
                    print (" ")
                    endofgame = True
                    startOver()
            else:
                continue      
            
            
    game()
    
