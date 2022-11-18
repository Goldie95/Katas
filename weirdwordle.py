passwordGuess = ""
allowedGuesses = 5

if __name__ == "__main__":
  while True:
    print("---------NEW GAME----------")  
    print("Welcome to Weird Wordle")
    print("This is a 2 player game.")
    print("Player 1 will enter a password exactly 5 letters long.")
    print("Player 2 will get chances to guess the password to win.")
    print(" ")
    print("Player 1 - Using only alphabetic letters, enter a 5 character password:")
    
    password = ""
    
      
 # This function will validate the password by checking if the input is:
 # 1. Alphabetic 
 # 2. 5 characters in length
    
    def validatePassword():
        validationPassed = False
        while validationPassed == False:
            password = input()
            if password.isalpha:
                if len(password) == 5:
                   validationPassed == True
                   return password
                else:
                     print("You made a mistake, the password was either the wrong length or wasnt alaphabetic characters. Try again.")
                     
    def validateGuess():
        validationComplete = False
        while validationComplete == False:
            passwordGuess = input()
            if passwordGuess.isalpha:
                if len(passwordGuess) == 5:
                   validationComplete == True
                   return passwordGuess
                else:
                    validationComplete == True
                    print("You made a mistake, your guess was either the wrong length or wasnt alaphabetic characters. Try again.")
            
    def checkGuess(password, passwordGuess):
        pattern = []
        for i, letter in enumerate(passwordGuess):
            if passwordGuess[i] == password[i]:
                #print (i + "✔")
                pattern += "✔"
            elif letter in password:
                #print (i + "+")
                pattern += "+"
            else:
                #print (i + "X")
                pattern += "X"
        return ''.join(pattern)      
         
            
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
                if guessNumber < 6:
                    print ("Player 2 wins.")
                    print (" ")
                    endofgame = True
            elif password != passwordGuess:
                if guessNumber == 6:
                    print ("Player 1 wins.")
                    print (" ")
                    endofgame = True
            else:
                continue      
            
            
    game()
    
