import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_letters = []
random_symbols = []
random_numbers = []

random_index = 0
for i in range(nr_letters):
    random_index = random.randint(0, len(letters) - 1)
    random_letters.append(letters[random_index])

for i in range(nr_symbols):
    random_index = random.randint(0, len(symbols) - 1)
    random_symbols.append(symbols[random_index])

for i in range(nr_numbers):
    random_index = random.randint(0, len(numbers) - 1)
    random_numbers.append(numbers[random_index])

total_characters = [random_letters, random_symbols, random_numbers]
character_counter = nr_letters + nr_symbols + nr_numbers
password = ""

for i in range(character_counter):
    type_index = random.randint(0, len(total_characters) - 1)
    character_index = random.randint(0, len(total_characters[type_index]) - 1)
    password += str(total_characters[type_index][character_index])
    total_characters[type_index].pop(character_index)
    if not total_characters[type_index]:
        total_characters.pop(type_index)

print(password)
