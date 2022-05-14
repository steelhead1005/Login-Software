from random import randint
import time

# The login function allows the user to input a username and password, which it checks against the file
# and returns True if the details match
def login():
    # Open the files in read mode
    usernameFile = open("usernames.txt", 'r')
    passwordFile = open("passwords.txt", 'r')

    # Create arrays with all of the usernames and passwords in them
    userArray = (usernameFile.read()).split()
    passArray = (passwordFile.read()).split()
    # index variable used to keep track of the indexes that line up for password and username
    index = 0
    # Take username input
    userIn = input("Enter a username: ")
    # Remove leading or trailing spaces
    userIn = userIn.strip()
    # Prompt password input
    passIn = input("Enter a password: ")
    # Remove leading or trailing spaces
    passIn = passIn.strip()

    # Search for username in the array
    while index < (len(userArray) - 1) and userArray[index] != userIn:
        index += 1
    # Set passFound to the same index as the index of the username (so the username and password match up)
    passFound = passArray[index]
    # Close the files as they are no longer necessary (and cannot be closed after the return command)
    usernameFile.close()
    passwordFile.close()
    # Add a logging in effect
    print("Logging in...")
    time.sleep(3)
    # If the details match, return True otherwise return False
    if passIn == passFound and userIn == userArray[index]:
        print("Login successful. Welcome", userIn)
        return True
    else:
        print("Login failed. Invalid username or password.")
        return False



def register(): 
    # Function prompts user for a username and password, giving them the option to randomly generate one
    # after which it repeats to them their username and password before writing them to a file.

    # Open files
    usernameFile = open("usernames.txt", 'a+')
    passwordFile = open("passwords.txt", 'a+')
    accountFile = open("accounts.txt", 'a+')

    # Declare username and password variables, prompting user for a username
    username = input("Please enter a username: ")
    # Remove leading or trailing spaces
    username = username.strip()
    password = ""

    # Give user the choice of a randomly generated or regular password
    userIn = input("Enter a password or leave blank to generate a randomized password: ")
    # Remove leading or trailing spaces
    userIn = userIn.strip()
    # Handle the user's choice
    if userIn == "":
        # Give the user a choice between a combination of letters, symbols, and numbers
        print("Choose which characters you want included in your randomized password:")
        print("[l]")
        print("[n]")
        print("[s]")
        userIn = input("Combination (ie: lns for letters numbers and symbols): ")
        # Prompt user for the length of their password (this is ignored if the user doesn't input correctly for the previous choice)
        length = input("Enter password length: ")
        # Remove leading or trailing spaces
        length = length.strip()
        # Set the user input to lowercase in case the user had caps lock or similar on
        userIn = userIn.lower()
        # Check if user entered a valid input
        if "l" in userIn or "n" in userIn or "s" in userIn:
            # Call the passGen function
            password = passGen("l" in userIn, "n" in userIn, "s" in userIn, int(length))
        else:
            # Inform the user of their mistake and call the passGen function
            print("Invalid input, generating password with letters, numbers and symbols of 16 characters length.")
            password = passGen(True, True, True, 16)
        print("Generating your password...")
        time.sleep(3)
    else:
        # When randomizer is not chosen, just set the password to whatever else the user chose
        password = userIn

    # Display the username and password (so the user can check it over, or write it down)
    print("Account successfully registered.")
    print("Username: ", username)
    print("Password: ", password)
    # Write the usernames and passwords to their respective files
    accountFile.write("Username: " + username + " Password: " + password + "\n")
    usernameFile.write(username + " ")
    passwordFile.write(password + " ")

    # Close the files
    usernameFile.close()
    passwordFile.close()
    accountFile.close()


def passGen(randLet, randNum, randSym, len):
    # Generates a random password based on the choice of symbols numbers or letters and the length

    genPass = ""
    # Large decision area where each case is considered
    if randLet and randNum and randSym:
        for i in range(len):
            r = randint(1, 3) # Randoizes whether it is a symbol, number or letter
            if r == 1:
                genPass += genRandLet()
            elif r == 2:
                genPass += str(randint(0, 9))
            else:
                genPass += genRandSym()

    elif (randLet and randNum) or (randNum and randSym) or (randSym and randLet):
        if randLet and randNum:
            for i in range(len):
                r = randint(1, 2) # Randomizes between letters and numbers
                if r == 1:
                    genPass += genRandLet()
                else:
                    genPass += str(randint(0,9))
        elif randLet and randSym:
            for i in range(len):
                r = randint(1, 2) # Randomizes between letters and symbols
                if r == 1:
                    genPass += genRandLet()
                else:
                    genPass += genRandSym()
        else:
            for i in range(len):
                r = randint(1, 2) # Randomizes between symbols and numbers
                if r == 1:
                    genPass += genRandSym()
                else:
                    genPass += str(randint(0,9))

    else: # The section in which only a single type (letters, symbols, or numbers) is used
        if randLet:
            for i in range(len):
                genPass += genRandLet()
        elif randNum:
            for i in range(len):
                genPass += str(randint(0,9))
        else:
            for i in range(len):
                genPass += genRandSym()
    return genPass


def genRandLet(): # Generates a random letter by parsing a randomized integer into a character
    genned = str(chr(randint(65, 90)))
    r = randint(1, 2)
    if r == 1:
        genned = genned.lower()
    return str(genned)


def genRandSym(): # Generates a random symbol by parsing a randomized integer into a character
    r = randint(33, 64)
    if r > 60:
        r += 62
    elif r > 54:
        r += 36
    elif r > 47:
        r += 10
    return str(chr(r))
    


def viewAccounts(): # Reads the accounts.txt file
    accountFile = open("accounts.txt", 'r')
    print(accountFile.read())
    accountFile.close()



def deleteAccounts(): # Opens all files in write mode, deleting all of their contents and thus resetting them
    accountFile = open("accounts.txt", 'w')
    usernameFile = open("usernames.txt", 'w')
    passwordFile = open("passwords.txt", 'w')
    accountFile.write("")
    usernameFile.write("")
    passwordFile.write("")
    accountFile.close()
    usernameFile.close()
    passwordFile.close()



# BEGIN Main
x = True # flag for mainLoop, triggered by the user inputting the exit command
logged = False # boolean for being logged in
userChoice = "" # choice of user for operation

print("***Welcome***")
while x:

    if logged: #Menu for being logged in
        print("Choose your operation:")
        print("[v] - View accounts")
        print("[r] - Register a new account")
        print("[d] - Delete all registered accounts")
        print("[x] - Logout of account")
        print("[e] - Exit the program")
        userChoice = input("Choice: ").lower()
        if userChoice == "v":
            viewAccounts()
        elif userChoice == "e":
            x = False
        elif userChoice == "d":
            deleteAccounts()
        elif userChoice == "r":
            register()
        elif userChoice == "x":
            logged = False
        else:
            print("Please input a valid operation.")

    else: #Menu for users trying to log in
        print("Choose your operation:")
        # Opens username file
        usernameFile = open("usernames.txt", 'r')
        # Create arrays with all of the usernames and passwords in them
        userArray = (usernameFile.read()).split()
        # Checks if there are any registerd accounts
        if len(userArray) != 0:
            print("[l] - Login with an existing account")
        print("[r] - Register a new account")
        print("[e] - Exit the program")
        userChoice = input("Choice: ").lower()
        # Only allows the user to login if there is a registered account
        if len(userArray) != 0:
            if userChoice == "l":
                logged = login()
        if userChoice == "r":
            register()
        elif userChoice == "e":
            x = False
        else:
            print("Please input a valid operation.")

print("")
print("Exiting...")
print("3...")
time.sleep(1) # Wait 1 second
print("2...")
time.sleep(1) # Wait 1 second
print("1...")
time.sleep(1) # Wait 1 second
print("Goodbye")
