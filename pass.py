import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "^", "(", ")", "*", "+"]

print("welcome to password generator")
letter_choice = int(input("How many letters do you want? \n"))

number_choice = int(input("How many numbers do you want? \n"))

symbols_choice = int(input("how many symbols do you want? \n"))

# password = " "

# for char in range(1, letter_choice):
#     password += random.choice(letters)

# for char in range(1, number_choice):
#     password += random.choice(numbers)

# for char in range(1, symbols_choice):
#     password += random.choice(symbols)

# print(password)


password_list = []

for char in range(0, letter_choice):
    password_list.append(random.choice(letters))

for char in range(0, number_choice):
    password_list.append(random.choice(numbers))

for char in range(0, symbols_choice):
    password_list.append(random.choice(symbols))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(password)