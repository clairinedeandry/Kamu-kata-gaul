import random

character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_lenght = int(input('masukkan panjang password'))
password = ""

for i in range(pass_lenght):
    password += random.choice(character)

print(password)