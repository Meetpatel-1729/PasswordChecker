# I, Meet Patel, student number 000794612, certify that all code submitted
# is my own work; that I have not copied it from any other source.
# I also certify that I have not allowed my work to be copied by others.

# function to check if password is valid or not 
def passwordIsOk( password ):
    validLength = True
    validUpper = False
    validNumber = False
    validSpace = True
    validCharacter = True
    flag = False
    loop = 0
    condition = "Please enter a valid password! your password does not contain following:"
 
    length = len( password )

    # checks whether the length of password is at least 10 or not  
    if not length >= 10:
        validLength = False
        condition = "It has less than 10 characters."

    # loop to execute for each of the character
    while loop < length:

        #checks if the password contain a capital letter or not
        if password[ loop ].isupper():
            validUpper = True

        #checks if the password contain a number or not       
        if password[ loop ].isdecimal():
            validNumber = True

        #checks if the password contain any space or not    
        if password[ loop ].isspace():
            validSpace = False
        loop += 1
		
    if not validUpper:
        condition += "\nIt does not contain a capital letter."
    if not validNumber:
        condition += "\nIt does not contain any digit."
    if not validSpace:
        condition += "\nIt contains space."
    

    # checks if the password contain $, #, %, &, * or not    
    if not ("$" in password or "#" in password or "%" in password or "&" in password or "*" in password ):
        validCharacter = False
        condition += "\nIt does not contain any special character."

    # checks all the condition for the valid password
    if ( validLength == True and validUpper == True and validNumber == True and validSpace == True and validCharacter == True):
        flag = True
    else:
        print(condition)
        
    return flag


password = input("Please enter a password: ")

while not passwordIsOk( password ):
    password = input("\nPlease enter a password: ")

print("VALID password!")
