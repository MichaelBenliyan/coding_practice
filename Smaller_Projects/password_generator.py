import random
print("Welcome to Password Generator!")
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = [i for i in "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

password = []
solution = ""
print()
num_letters = int(input("How many letters would you like in your password? "))
print()
num_symbols = int(input("How many symbols would you like? "))
print()
num_numbers = int(input("How many numbers would you like? "))
print()

for n in range(0, num_letters):
    password.append(random.choice(letters))
for n in range(0, num_symbols):
    password.append(random.choice(symbols))
for n in range(0, num_numbers):
    password.append(random.choice(numbers))
random.shuffle(password)
for char in password: 
    solution += str(char)
print(f"Here is your password: {solution}")

