
import random
import passw



answers = input("[?] How many password would you like to generate? ")
if answers == "" or answers == " ":
    amount = 1
else:
    amount = answers
    
print(passw.generate_password(amount, True))