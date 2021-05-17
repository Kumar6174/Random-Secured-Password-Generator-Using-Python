import random

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = [1,2,3,4,5,6,7,8,9,0]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']

n_letters=int(input("How many letters you want in your password?\n"))
n_numbers=int(input("How many numbers you want in your password?\n"))
n_symbols=int(input("How many symbols you want in your password?\n"))

password=""

for char in range(1, n_letters+1):
    password += random.choice(letters)
for char in range(1, n_numbers+1):
    password += str(random.choice(numbers))
for char in range(1, n_symbols+1):
    password += random.choice(symbols)

password=list(password)
random.shuffle(password)

final_password = ""
  
for x in password:
    final_password += x

print("Your new password is : "+final_password)
