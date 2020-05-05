##
# A program for form validation of names, emails, passwords, and address's.
# Student Name: Will Malisch
# Student ID: wmalisch
# Student Number: 250846447

## Define the main function
# @param no parameter, just runs
#
def main():
    # Import all the functions created in string validation
    from stringvalidation import checkAddress
    from stringvalidation import checkName
    from stringvalidation import checkEmail
    from stringvalidation import checkPassword

    # Prompt user input for their name. If it is an invalid name according to checkName function, make them re-input. Once name is valid, move on.
    name = str(input("Enter your first and last name here: "))
    validNam = checkName(name)
    while validNam == False:
        name = str(input("Please try again: "))
        validNam = checkName(name)

    # Prompt user input for their email address. If it is an invalid email according to checkEmail function, make them re-input. Once name is valid, move on.
    email = str(input("Enter your email address here: "))
    validEma = checkEmail(email)
    while validEma == False:
        email = str(input("Please try again: "))
        validEma = checkEmail(email)

    # Prompt user input for their password. If it is an invalid password according to checkPassword function, make them re-input. Once name is valid, move on.
    password = str(input("Enter your password here: "))
    validPass = checkPassword(password)
    while validPass == False:
        password = str(input("Please try again: "))
        validPass = checkPassword((password))

    # Prompt user input for their address. If it is an invalid address according to checkAddress function, make them re-input. Once name is valid, move on.
    address = str(input("Type the address: "))
    validAdd = checkAddress(address)
    while validAdd == False:
        address = str(input("Please try again: "))
        validAdd = checkAddress(address)

    # Use if statement to verfiy all inputs have been validated. It is certain they are all valid, otherwise they would not have
    # Made it past the last steps. Print their information.
    if (validEma == True and validAdd == True and validNam == True and validPass == True):
        print("\nThank you, %s\nYour email is: %s\nYour password is: %s\nYour address is: %s" % (name, email, password, address))
    else:
        return

# Call main to perform the tasks defined in main()
main()
