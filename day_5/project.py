# password generator
import random

print("Welcome to the python password generator")

letter = []
for i in range(97, 123):
    letter.append(chr(i))

for i in range(65, 91):
    letter.append(chr(i))

symbols = []
for i in range(33, 48):
    if chr(i) != "'" and chr(i) != '"':
        symbols.append(chr(i))
for i in range(59, 65):
    if chr(i) != "'" and chr(i) != '"':
        symbols.append(chr(i))

numbers = []
for i in range(48, 58):
    numbers.append(chr(i))

password_length = int(input("How many char do you want to include in your password? "))
is_include_letter = input("Do you want to include letter? y/n -> ") == 'y'
is_include_symbol = input("Do you want to include symbol? y/n -> ") == 'y'
is_include_number = input("Do you want to include number? y/n -> ") == 'y'

char = []

if is_include_letter:
    char = char + letter

if is_include_symbol:
    char = char + symbols

if is_include_number:
    char = char + numbers

password = []
for length in range(1, password_length + 1):
    password.append(random.choice(char))

random.shuffle(password)

new_password = ""
for new_char in password:
    new_password += new_char

print(f"Your password is : {new_password}")

