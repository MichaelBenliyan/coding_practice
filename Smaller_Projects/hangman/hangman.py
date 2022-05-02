from random import choice
with open("animals.txt") as animals: 
    animals_list = [line.lower().rstrip() for line in animals]
hanging_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
guesses = []
incorrect_guess_count = 0
mystery_word = list(choice(animals_list))
visible_mystery_word = list(map(lambda x: "_" if x != " " else x, mystery_word))
print("___________________________________")
print(hanging_stages[incorrect_guess_count])
print()
print(" ".join(visible_mystery_word))
print()

while incorrect_guess_count < 6:
    if incorrect_guess_count < 7: 
        guess = input("Guess a letter: ").lower().strip()
        if len(guess.strip()) > 1 or guesses.count(guess) > 0:
            if guesses.count(guess) > 0:
                print()
                print("You already guessed that silly goose. " + "\U0001F61C")
                print()
            else:
                print()
                print("You broke a rule.\nPlease enter only one letter next time.")
                print()
        else: 
            correct_guess = False
            for i in range(len(mystery_word)):
                char = mystery_word[i]
                if char == guess:
                    visible_mystery_word[i] = char
                    correct_guess = True
            if correct_guess == True: 
                guesses.append(guess)
                if visible_mystery_word == mystery_word:
                    print("___________________________________")
                    print() 
                    print("".join(visible_mystery_word))
                    print()
                    print("CONGRADULATIONS, YOU WON! ")
                    print("\U0001F973"+"\U0001F973"+"\U0001F973"+"\U0001F973"+"\U0001F973")
                    print()
                    break
                else:
                    print("___________________________________")
                    print(hanging_stages[incorrect_guess_count])
                    print("CORRECT!" + " " + "\U0001F525")
                    print("Already Guessed: {}".format(" ".join(guesses)))
                    print()
                    print(" ".join(visible_mystery_word))
                    print()
            elif correct_guess == False: 
                guesses.append(guess)
                if incorrect_guess_count + 1 < 6:
                    incorrect_guess_count += 1 
                    print("___________________________________")
                    print(hanging_stages[incorrect_guess_count])
                    print("Nice try." + " " + "\U0001F44E")
                    print("Already Guessed: {}".format(" ".join(guesses)))
                    print()
                    print(" ".join(visible_mystery_word))
                    print()
                elif incorrect_guess_count + 1 == 6:
                    incorrect_guess_count += 1
                    print("___________________________________")
                    print(hanging_stages[incorrect_guess_count])
                    print()
                    print("You lost." + " " + "\U0001F622")
                    print("The word was: {}".format("".join(mystery_word)))
                    print()





