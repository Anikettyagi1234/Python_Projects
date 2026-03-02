import random
letter = ['A', 'B', 'C', 'D', 'E', 'F','G','H','I','J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', ' X', 'Y', 'Z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbole = ['!', '@', ' #', '$', '%', '^', '&', '*', '+', '(', ')']
nm_letters = int(input("How many letters would you like in your password ?\n"))
nm_symbols = int(input("How many Symboles would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))
# Easy_Method 
#EF34%#

password = ""
for char in range (1,nm_letters +1):
    password += random.choice(letter)
for char in range (1,nm_symbols +1):
    password += random.choice(symbole)
for char in range (1,numbers +1):
    password += random.choice(number)
print(password)

# this type of password Easly hacke by Hackers

#Hard_Method 
# E5%D#3t@r4W@SE#23K

password_list = []
for char in range (1,nm_letters +1):
    password_list.append(random.choice(letter))
for char in range (1,nm_symbols +1):
    password_list.append(random.choice(symbole))
for char in range (1,numbers +1):
    password_list.append(random.choice(number))
print(password_list)
random.shuffle(password_list)                        # use a random.shuffle()
print(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your Password is: {password}")
