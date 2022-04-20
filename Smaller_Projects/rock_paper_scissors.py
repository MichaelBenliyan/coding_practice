import random

print('''
______              _        ______                           _____        _
| ___ \            | |       | ___ \                         /  ___|      (_)
| |_/ / ___    ___ | | __    | |_/ /__ _  _ __    ___  _ __  \ `--.   ___  _  ___  ___   ___   _ __  ___
|    / / _ \  / __|| |/ /    |  __// _` || '_ \  / _ \| '__|  `--. \ / __|| |/ __|/ __| / _ \ | '__|/ __|
| |\ \| (_) || (__ |   <  _  | |  | (_| || |_) ||  __/| | _  /\__/ /| (__ | |\__  \__ \| (_) || |   \__ |
\_| \_|\___/  \___||_|\_\( ) \_|   \__,_|| .__/  \___||_|( ) \____/  \___||_||___/|___/ \___/ |_|   |___/
                         |/              | |             |/                                              
                                         |_|                                                             \n''')

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

options = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("")
print(options[user_choice])
print()
print("Computer Chooses:")
comp_choice = random.randint(0,2)
print(options[comp_choice])
print("_________________________")
if comp_choice == 0:
    if user_choice == 0:
        print("It's a DRAW!")
    elif user_choice == 1:
        print("You WIN!")
    elif user_choice == 2: 
        print("You Lose.")
elif comp_choice == 1:
    if user_choice == 0:
        print("You Lose.")
    elif user_choice == 1:
        print("It's a DRAW!")
    elif user_choice == 2: 
        print("You WIN!")
elif comp_choice == 2:
    if user_choice == 0:
        print("You WIN!")
    elif user_choice == 1:
        print("You Lose.")
    elif user_choice == 2: 
        print("It's a DRAW!")
print()
