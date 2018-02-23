###############################################################################
# Name:
#  _____              _      _   _  __     _       _                   _    _ 
# |  __ \            (_)    | | | |/ /    | |     | |                 | |  (_)
# | |  | | __ _ _ __  _  ___| | | ' /_   _| | __ _| | _____  _   _ ___| | ___ 
# | |  | |/ _` | '_ \| |/ _ \ | |  <| | | | |/ _` | |/ / _ \| | | / __| |/ / |
# | |__| | (_| | | | | |  __/ | | . \ |_| | | (_| |   < (_) | |_| \__ \   <| |
# |_____/ \__,_|_| |_|_|\___|_| |_|\_\__,_|_|\__,_|_|\_\___/ \__,_|___/_|\_\_|
# Due Date: October 14, 2016
# Description: Hangman
###############################################################################

print('''888                                                           
888                                                           
888                                                           
88888b.   8888b.  88888b.   .d88b.  88888b.d88b.   8888b.  88888b.  
888 "88b     "88b 888 "88b d88P"88b 888 "888 "88b     "88b 888 "88b 
888  888 .d888888 888  888 888  888 888  888  888 .d888888 888  888 
888  888 888  888 888  888 Y88b 888 888  888  888 888  888 888  888 
888  888 "Y888888 888  888  "Y88888 888  888  888 "Y888888 888  888 
                                888                              
                           Y8b d88P                              
                            "Y88P"                               ''')
print("\nBy: Daniel Kulakouski")

word = input("\n\nWould you like to input your own word?: ")

if(word.lower()=='yes' or word.lower()=='y'): #if the user want to input their own word, they can
    secretWord = input("Enter your own word: ")
    for i in range (0,len(secretWord)):
        if(secretWord[i].isalpha()==False and secretWord[i]!=" "): #checks if the word is valid
            print("Invalid input")
            quit()
elif(word.lower()=='no' or word.lower()=='n'):#if the user doesn't want to put their own word, the default word is set
    secretWord = "Alex Shen is a hacker"
else: #if anything invalid is inputted, the appropriate message is printed
    print("Invalid input")
    quit()

attempts = 7 #sets seven attempts
usedLetters = ""
missingLetters = len(secretWord)
letters = ""

for i in range(0,len(secretWord)): #goes through each letter in the word and inserts a "_" or a space
    if(secretWord[i]==" "):
        print(" ",end="")
        missingLetters-=1
    else:
        print("_",end="")

while (attempts>0 and missingLetters>0): #keeps looping until you win or lose
    #ascii art for the person that gets hung
    if(attempts==7):
        print("\n ___________.._______")
        print("| .__________))______|")
        print("| | / /      ||")
        print("| |/ /       ||")
        print("| | /")
        print("| |/")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print('""""""""" _________ |"""""|')
        print('|"|"""""" _________ \'"|"|')
        print("| |                   | |")
        print(": :                   : :")
        print(". .                   . .")

    if(attempts==6):
        print("\n ___________.._______")
        print("| .__________))______|")
        print("| | / /      ||")
        print("| |/ /       ||")
        print("| | /        ||.-''.")
        print("| |/         |/  _  \\")
        print("| |          ||  `/,|")
        print("| |          (\\`_.'")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print('""""""""" _________ |"""""|')
        print('|"|"""""" _________ \'"|"|')
        print("| |                   | |")
        print(": :                   : :")
        print(". .                   . .")
    if(attempts==5):
        print("\n ___________.._______")
        print("| .__________))______|")
        print("| | / /      ||")
        print("| |/ /       ||")
        print("| | /        ||.-''.")
        print("| |/         |/  _  \\")
        print("| |          ||  `/,|")
        print("| |          (\\`_.'")
        print("| |          -`--'.")
        print("| |           . . ")
        print("| |          |   |")
        print("| |          | . |")
        print("| |          |   |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print('""""""""" _________ |"""""|')
        print('|"|"""""" _________ \'"|"|')
        print("| |                   | |")
        print(": :                   : :")
        print(". .                   . .")
    if(attempts==4):
        print("\n ___________.._______")
        print("| .__________))______|")
        print("| | / /      ||")
        print("| |/ /       ||")
        print("| | /        ||.-''.")
        print("| |/         |/  _  \\")
        print("| |          ||  `/,|")
        print("| |          (\\`_.'")
        print("| |         .-`--'.")
        print("| |        /Y . . ")
        print("| |       // |   |")
        print("| |      //  | . |")
        print("| |     ')   |   |")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print('""""""""" _________ |"""""|')
        print('|"|"""""" _________ \'"|"|')
        print("| |                   | |")
        print(": :                   : :")
        print(". .                   . .")
    if(attempts==3):
        print("\n ___________.._______")
        print("| .__________))______|")
        print("| | / /      ||")
        print("| |/ /       ||")
        print("| | /        ||.-''.")
        print("| |/         |/  _  \\")
        print("| |          ||  `/,|")
        print("| |          (\\`_.'")
        print("| |         .-`--'.")
        print("| |        /Y . . Y\\")
        print("| |       // |   | \\\\")
        print("| |      //  | . |  \\\\")
        print("| |     ')   |   |   (`")
        print("| |")
        print("| |")
        print("| |")
        print("| |")
        print('""""""""" _________ |"""""|')
        print('|"|"""""" _________ \'"|"|')
        print("| |                   | |")
        print(": :                   : :")
        print(". .                   . .")
    if(attempts==2):
        print("\n ___________.._______")
        print("| .__________))______|")
        print("| | / /      ||")
        print("| |/ /       ||")
        print("| | /        ||.-''.")
        print("| |/         |/  _  \\")
        print("| |          ||  `/,|")
        print("| |          (\\`_.'")
        print("| |         .-`--'.")
        print("| |        /Y . . Y\\")
        print("| |       // |   | \\\\")
        print("| |      //  | . |  \\\\")
        print("| |     ')   |   |   (`")
        print("| |          ||'")
        print("| |          ||")
        print("| |          ||")
        print("| |         / |")
        print('""""""""" _________ |"""""|')
        print('|"|"""""" _________ \'"|"|')
        print("| |                   | |")
        print(": :                   : :")
        print(". .                   . .")
    if(attempts==1):
        print("\n ___________.._______")
        print("| .__________))______|")
        print("| | / /      ||")
        print("| |/ /       ||")
        print("| | /        ||.-''.")
        print("| |/         |/  _  \\")
        print("| |          ||  `/,|")
        print("| |          (\\`_.'")
        print("| |         .-`--'.")
        print("| |        /Y . . Y\\")
        print("| |       // |   | \\\\")
        print("| |      //  | . |  \\\\")
        print("| |     ')   |   |   (`")
        print("| |          ||'||")
        print("| |          || ||")
        print("| |          || ||")
        print("| |         / | | \\")
        print('""""""""" _________ |"""""|')
        print('|"|"""""" _________ \'"|"|')
        print("| |                   | |")
        print(": :                   : :")
        print(". .                   . .")
    
    newLetter = input("\nEnter your guess: ") #letter that the user guesses
    
    if(newLetter.isalpha()==True or " " in newLetter): #checks if the guess is valid
        if(newLetter[0].lower() in secretWord.lower() and newLetter not in usedLetters):
            for i in range(0,len(secretWord)): #loops through the secret word and checks if the guess is correct or not
                if(newLetter[0].lower() in secretWord[i].lower()):
                    print(secretWord[i],end="")
                    letters+=newLetter[0] #adds the guess to letters which get printed instead of the "_"
                    if(newLetter[0] not in usedLetters): #if the letter hasn't already been guessed, the number of missing letters decreases
                        missingLetters-=1
                elif(secretWord[i].lower() in letters.lower()): #draws the dashes and correctly guessed letters
                    print(secretWord[i],end="")
                elif(secretWord[i]==" "):
                    print(" ",end="")
                else:
                    print("_",end="")
        
                    
        elif(newLetter[0].lower() in usedLetters.lower()): #if the letter has already been guessed, the message gets printed
            print("You already guessed that letter!")
            for i in range (0,len(secretWord)): #draws the word
                if(secretWord[i]==" "):
                    print(" ",end="")
                elif(secretWord[i].lower() in letters.lower()):
                    print(secretWord[i],end="")
                else:
                    print("_",end="")
        else:
            if(newLetter[0].lower() not in usedLetters.lower()): #if the letter has already been guessed, attempts decreases
                attempts-=1
                print("Nope. You have",attempts,"attempts left.")
            else:
                print("You already guessed that letter!\n")
            for i in range (0,len(secretWord)):
                if(secretWord[i]==" "):
                    print(" ",end="")
                elif(secretWord[i].lower() in letters.lower()):
                    print(secretWord[i],end="")
                else:
                    print("_",end="")
        if(newLetter[0].lower() not in usedLetters.lower()):
            usedLetters+=newLetter[0]
    else:
        print("Invalid input") #prints invalid input if the guess isn't valid
        for i in range (0,len(secretWord)):
            if(secretWord[i]==" "):
                print(" ",end="")
            elif(secretWord[i].lower() in letters.lower()):
                print(secretWord[i],end="")
            else:
                print("_",end="")

    print("\nUsed letters: ",usedLetters) #prints the used letters

if(attempts==0): #if you run out of lives, the person dies and you lose
    print("\n ___________.._______")
    print("| .__________))______|")
    print("| | / /      ||")
    print("| |/ /       ||")
    print("| | /        ||.-''.")
    print("| |/         |/  _  \\")
    print("| |          ||  `/,|")
    print("| |          (\\`_.'")
    print("| |         .-`--'.")
    print("| |        /Y . . Y\\")
    print("| |       // |   | \\\\")
    print("| |      //  | . |  \\\\")
    print("| |     ')   |   |   (`")
    print("| |          ||'||")
    print("| |          || ||")
    print("| |          || ||")
    print("| |         / | | \\")
    print('""""""""""|_`-\' `-\' |"""|')
    print('|"|"""""""\ \       \'"|"|')
    print("| |        \ \        | |")
    print(": :         \ \       : :")
    print(". .          `'       . .")
        
    print('''Yb  dP  dP"Yb  88   88     88      dP"Yb  .dP"Y8 888888 d8b 
 YbdP  dP   Yb 88   88     88     dP   Yb `Ybo." 88__   Y8P 
  8P   Yb   dP Y8   8P     88  .o Yb   dP o.`Y8b 88""   `"' 
 dP     YbodP  `YbodP'     88ood8  YbodP  8bodP' 888888 (8) ''')
    print("\nGame over\nThe secret sentence was",secretWord)
    quit()

if(missingLetters<=0): #if you guess all the missing letters, you win
    print('''\n /$$     /$$                        /$$      /$$ /$$           /$$
|  $$   /$$/                       | $$  /$ | $$|__/          | $$
 \  $$ /$$//$$$$$$  /$$   /$$      | $$ /$$$| $$ /$$ /$$$$$$$ | $$
  \  $$$$//$$__  $$| $$  | $$      | $$/$$ $$ $$| $$| $$__  $$| $$
   \  $$/| $$  \ $$| $$  | $$      | $$$$_  $$$$| $$| $$  \ $$|__/
    | $$ | $$  | $$| $$  | $$      | $$$/ \  $$$| $$| $$  | $$    
    | $$ |  $$$$$$/|  $$$$$$/      | $$/   \  $$| $$| $$  | $$ /$$
    |__/  \______/  \______/       |__/     \__/|__/|__/  |__/|__/
                                                                  
                                                                  
                                                                  ''')
    quit()
