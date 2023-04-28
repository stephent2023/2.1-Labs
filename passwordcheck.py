# write an application that checks the strength of a password.
# Requirements:
# 
# Write a class that has a method that checks the password strength.
# Use factors like length, upper/lower case and if it has a number and special character.
# ratings should be very weak - weak - moderate - strong - very strong 
# Check against a list of common passwords 10-20 common password = very weak
# User input that loops until the user quits
# User input that loops until the user quits
# A dictionary that returns a history of passwords/strengths whilst in the loop.
# Code must be pushed to a repo and 1 person per group must share with me. 
# 12.15 deadline

class PasswordChecker:
    def __init__(self, password):
        self.password = password

    def checkPassword(self):
        common_passwords = ["password","qwerty","password123","Password","123456","abcdefg"]
        upperChars, lowerChars, specialChars, digits, length = 0, 0, 0, 0, 0
        length = len(self.password)
        if self.password in common_passwords:
            return"Very weak\n"
        else:
            if (length < 6):
                return"Weak\n"
            else:
                for i in range(0, length):
                    if (self.password[i].isupper()):
                        upperChars += 1
                    elif (self.password[i].islower()):
                        lowerChars += 1
                    elif (self.password[i].isdigit()):
                        digits += 1
                    else:
                        specialChars += 1
            if (upperChars != 0 and lowerChars != 0 and digits != 0 and specialChars != 0):
                if (length >= 10):
                    return"Very Strong\n"
                else:
                    return"Strong\n"
            else:
                if (upperChars == 0):
                    return"Moderate\n"
                else:
                    return"Strong\n"

def try_again():
    while True:
        answer = input("Do you want to try another password? Answer yes or no: ")
        if answer == "yes":
            password = input("Please enter password: ")
            password1 = PasswordChecker(password)
            strength = password1.checkPassword()
            print("This password is",strength)
            password_history.update({password:strength.strip("\n")})
            print(password_history)      
        elif answer == "no":
            break
        else:
            print(" ")

password_history = {}

password = input("Please enter password: ")
password1 = PasswordChecker(password)
strength = password1.checkPassword()
print("This password is",strength)
password_history.update({password:strength.strip("\n")})
print(password_history)

try_again()
