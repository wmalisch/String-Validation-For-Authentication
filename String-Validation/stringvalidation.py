##
# A program for form validation of names, emails, passwords, and address's.
# Student Name: Will Malisch
# Student ID: wmalisch
# Student Number: 250846447

# Define the checkName function
def checkName(name):

    # Declare validName as a variable now, instead of doing it later
    validName = True

    # Convert all hyphens to spaces because all validity criteria are the same for each
    name = name.replace("-", " ")

    # Test if the character in position == 0 is alpha. If it is alpha
    # Declare validFirstCharacter is equal to true, otherwise equal
    # False
    found = False
    position = 0
    while not found and position <= len(name):
        if name[position].isalpha() != True:
            position = position + 1
        else:
            found = True
    validFirstCharacterType = (position == 0)

    # Test if the first character type if both alpha and is uppercase. At the beginning, establish whether or not it is alpha.
    # If it is alpha, move on to estalish if it is uppercase. If it is declare the first character is valid
    if validFirstCharacterType != True:
        validFirstCharacter = False
    else:
        if name[position].isupper():
            validFirstCharacter = True
        else:
            validFirstCharacter = False

    # Define the minimum length of the string
    # The string must be at least 3 characters long
    if len(name) >= 3:
        validNameLen = True
    else:
        validNameLen = False

    # Count the amount of spaces. If it counts at least
    # 1 spaces, validSpace equals true. if spaces, validSpace is false
    spaceCount = 0
    for i in range(len(name)):
        if name[i] == " ":
            spaceCount = spaceCount + 1
    validSpace = (spaceCount >= 1)

    # Find the position of the space. We will use this later to test the validity of characters
    # And strins, within the inputted name
    spacePos = 0
    found = False
    while not found and spacePos < len(name):
        if name[spacePos] == " ":
            found = True
        else:
            spacePos = spacePos + 1

    nextCharacterPos = spacePos + 1

    # Using the spacePos, create a program to check if characters to
    # right of space are characters. If they are, declare validRightChar as True
    # Do this by making sure all the alpha and spcae characters to the right of the space are equal to the length
    # Of any characters to the right of the space
    length = 0
    characterCount = 0
    validRightChar = False
    for i in range(spacePos + 1, len(name)):
        length = length + 1
        if name[i].isalpha() or name[i] == " ":
            characterCount = characterCount + 1

    if characterCount != length:
        validRightChar = False
    else:
        validRightChar = True

    # Using the position of the space, make sure that the next
    # character is uppercase.
    if nextCharacterPos >= len(name):
        validSpaceCharacter = False
    else:
        if name[nextCharacterPos].isupper():
            validSpaceCharacter = True
        else:
            validSpaceCharacter = False

    # Create program that makes sure all characters to left of space
    # or hyphen are alpha. Do this using the position of the space found
    validLeftChar = True
    for i in range(1, spacePos):
        if name[i].isalpha():
            validLeftChar = True
        else:
            validLeftChar = False

    # Create the while loop that tests all the following
    # address criteria:
    # validLRightChar
    # validLeftChar
    # validSpace
    # validSpaceCharacter
    # validNameLen
    # validFirstCharacter
    while validName:
        if validFirstCharacter != True:
            validName = False
            print("Invalid, first letter must be uppercase.")
            return validName
        elif validNameLen != True:
            validName = False
            print("Invalid, name must be at lease 3 characters in the sequence: alpha, " ", alpha.")
            return validName
        elif validSpaceCharacter != True:
            validName = False
            print("Invalid, first letter after the space must be uppercase.")
            return validName
        elif validSpace != True:
            validName = False
            print("Invalid, there must be a space or hyphen in the name to separate first and last names.")
            return validName
        elif validLeftChar != True:
            validName = False
            print("Invalid, only allowed alphabetic characters to the left of the space or hyphen.")
            return validName
        elif validRightChar != True:
            validName = False
            print("Invalid, only allowed alphabetic characters to the right of the space or hyphen.")
            return validName
        else:
            validName  = True
            return validName
        # All of the validity rules have been established. This function is complete

# Define the checkName function
def checkEmail(email):

    # Declare validName as a variable now, instead of doing it later
    validEmail = True

    # Count the amount of @ symbols. Make sure there is only one using a boolean expression in validAt
    atCount = 0
    for i in range(len(email)):
        if email[i] == "@":
            atCount = atCount + 1
    validAt = (atCount == 1)

    # Identify the position index of the @ symbol. This code
    # Goes through all indexes in the email string, until it finds
    # One @ symbol.
    atPos = 0
    found = False
    while not found and atPos < len(email):
        if email[atPos] == "@":
            found = True
        else:
            atPos = atPos + 1

    # Validate if there is one period. The function runs through the
    # Email string and counts how many periods there are. validPeriod is
    # Declared true if there is only 1
    periodCount = 0
    for i in range(len(email)):
        if email[i] == ".":
            periodCount = periodCount + 1
    validPeriod = (periodCount == 1)

    # Find the position of the period in email string
    periodPos = 0
    found = False
    while not found and periodPos < len(email):
        if email[periodPos] == ".":
            found = True
        else:
            periodPos = periodPos + 1

    # Create the validFirstString rule. The first string is valid if
    # all characters before the @ symbol are alpha-numeric. This excludes all
    # special characters such as: !@#$%^&*()
    for i in range(0, atPos):
        if email[i].isalpha() or email[i].isnumeric():
            validFirstString = True
        else:
            validFirstString = False

    # Validate the second string (from @ symbol to period) is alphabetic.
    # It takes the length of the string from @ to period, and compares that to
    # the length of only the alpha characters in that string. If they are equal
    # Second String is valid.
    characterCount = 0
    length = 0
    validSecondString = False
    for i in range(atPos + 1, periodPos):
        length = length +1
        if email[i].isalpha():
            characterCount = characterCount + 1
    if characterCount != length:
        validSecondString = False
    else:
        validSecondString = True

    # Program to validate that the email string ends with .com, .net, .org, or .ca
    if email.endswith("com") or email.endswith("net") or email.endswith("org") or email.endswith("ca"):
        validEnding = True
    else:
        validEnding = False

    # Create the while loop that tests all the following email criteria:
    # validEnding
    # validSecondString
    # validFirstString
    # validPeriod
    # validAt
    while validEmail:
        if validAt != True:
            validEmail = False
            print("Invalid, you need exactly 1 @ symbol in your email. It should be between a set of alpha-numeric characters\non the left, and alpha on the right.")
            return validEmail
        elif validPeriod != True:
            validEmail = False
            print("Invalid, can have only 1 period in your email. It should be before your top level domain (Ex. com, net, org, ca).")
            return validEmail
        elif validFirstString != True:
            validEmail = False
            print("Invalid, your first string (anything before the @ symbol) must only contain alpha and numeric characters. This excludes: !@#$%^&*().")
            return validEmail
        elif validSecondString != True:
            validEmail = False
            print("Invalid, your second string (anything between the @ symbol and period) must be only alpha characters.")
            return validEmail
        elif validEnding != True:
            validEmail = False
            print("Invalid, you need a proper top level domain. These include: .com, .net, .org, .ca.")
            return validEmail
        else:
            validEmail = True
            return validEmail
        # All of the validity rules have been established. This function is complete

# Define the checkPassword function
def checkPassword(password):

    # Declare boolean expression for overall validity of password
    validPassword = True

    # Counts the amount of spaces. If it counts 0
    # spaces, validSpace equals true. if spaces, validSpace is false
    spaceCount = 0
    for i in range(len(password)):
        if password[i] == " ":
            spaceCount = spaceCount + 1
    validSpace = (spaceCount == 0)

    # Checks if the password has at least 1
    # number. if password has 1 or more numbers validNum equals true
    validDig = False
    positionNum = 0
    while not validDig and positionNum < len(password):
        if password[positionNum].isdigit():
            validDig = True
        else:
            positionNum = positionNum + 1

    # Checks if the the password is eight
    # characters. If password is eight or more characters
    # validLen equals true
    passLen = len(password)
    validLen = (passLen >= 8)

    # Takes a count of the number of uppercase
    # characters. If this value is >= to 1, validUp equals True
    upperCount = 0
    for i in range(len(password)):
        if password[i].isupper():
            upperCount = upperCount + 1
    validUp = (upperCount >= 1)

    # Takes a count of the number of lowercase
    # characters. If this value is >= to 1, validUp equals True
    lowerCount = 0
    for i in range(len(password)):
        if password[i].islower():
            lowerCount = lowerCount + 1
    validLower = (lowerCount >= 1)

    # Create the while loop that tests all the following password critera:
    # validLen
    # validDig
    # validSpace
    validPassword = True
    while validPassword:
        if validSpace != True:
            print("Invalid, you are not allowed spaces in your password")
            validPassword = False
            return validPassword
        elif validLen != True:
            validPassword = False
            print("Invalid, your password needs to be at least 8 characters")
            return validPassword
        elif validDig != True:
            validPassword = False
            print("Invalid, your password needs at least one number.")
            return validPassword
        elif validUp != True:
            validPassword = False
            print("Invalid, your password needs at least one uppercase character.")
            return validPassword
        elif validLower != True:
            validPassword = False
            print("Invalid, your password needs at least one lowercase character.")
            return validPassword
        else:
            validPassword = True
            return validPassword
        # All of the validity rules have been established. This function is complete

# Define the checkAddress function
def checkAddress(address):

    # Establish the validAddress as a boolean express. Use this later in program
    validAddress = True

    # Counts the amount of spaces. If it counts at least
    # 1 spaces, validSpace equals true. if spaces, validSpace is false
    spaceCount = 0
    for i in range(len(address)):
        if address[i] == " ":
            spaceCount = spaceCount + 1
    validSpace = (spaceCount > 0)

    #  Identify the position index of the first space
    spacePos = 0
    found = False
    while not found and spacePos < len(address):
        if address[spacePos] == " ":
            found = True
        else:
            spacePos = spacePos + 1

    # Using the spacePos, check if characters to
    # left of space are numbers
    # If the are, declare validDig as True
    validDig = True
    for i in range(1, spacePos):
        if address[i].isdigit():
            validDig = True
        else:
            validDig = False

    # Using the spacePos, check if characters to
    # right of space are characters
    # If the are, declare validChar as True
    characterCount = 0
    length = 0
    validChar = False
    for i in range(spacePos + 1, len(address)):
        length = length + 1
        if address[i].isalpha() or address[i] == " ":
            characterCount = characterCount + 1
    if characterCount != length:
        validChar = False
    else:
        validChar = True

    # Create the while loop that tests all the following
    # address criteria:
    # validLChar
    # validDig
    # validSpace
    while validAddress:
        if validSpace != True:
            validAddress = False
            print("Invalid, you need at least 1 space, and it must be after the house number.")
            return validAddress
        elif validDig != True:
            validAddress = False
            print("Invalid, you need at least 1 number at the beginning of your address, before a space.")
            return validAddress
        elif validChar != True:
            validAddress = False
            print("Invalid, you need at least 1 character or word after the space.")
            return validAddress
        else:
            validAddress = True
            return validAddress
        # All of the validity rules have been established. This function is complete
