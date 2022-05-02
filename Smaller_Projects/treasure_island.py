print('''*******************************************************************************\n
          |                   |                  |                     |\n
 _________|________________.=""_;=.______________|_____________________|_______\n
|                   |  ,-"_,=""     `"=.|                  |\n
|___________________|__"=._o`"-._        `"=.______________|___________________\n
          |                `"=._o`"=._      _`"=._                     |\n
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______\n
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |\n
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________\n
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |\n
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______\n
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |\n
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________\n
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____\n
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_\n
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____\n
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_\n
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____\n
/______/______/______/______/______/______/______/______/______/______/_____ /\n
*******************************************************************************''')
print("Welcome to Treasure Island, your mission is to find the treasure!")

choice_1 = input('''You see two paths cut through the forest ahead of you. 
Which path would you like to take? Right or Left? ''').lower()
print("________________________________________________________________________")
print("")
if choice_1 == "right":
    print("You were ambushed by a tribe of canibals. Game Over.")
    print("________________________________________________________________________")
    print("")
else: 
    choice_2 = input('''You trecked through the forest for 2 days. You\'re 
hungry, exhausted, and stink. In front of you is a huge magical castle. 
However, there is a large moat full of aligators surrounding it. You can either 
swim through the moat now or wait for the aligators to go to sleep. 
What will you do? Swim or Wait? ''').lower()
    print("________________________________________________________________________")
    print("")
    if choice_2 == "swim":
        print('''You really chose to swim through it? The aligators tore you 
apart in seconds. Game Over.''')
        print("________________________________________________________________________")
        print("")

    else: 
        choice_3 = input('''You managed to swim passed all the aligators
as they were sleeping and make it to 
the entrance of the castle.(Crazy I 
know, but you\'re just that stealthy 
apparently) Now you have a choice 
between three doors. 
Which door will you pick? Red, Blue, or Yellow? ''').lower()
        print("________________________________________________________________________")
        print("")
        if choice_3 == "blue" or choice_3 == "Red":
            print("It was a trap! A slab of needles smushed you into soup. Game Over.")
            print("________________________________________________________________________")
            print("")
        else:
            print('''You sneak in the door and see a winding staircase. 
You move down the staircase and with each
step you get a better view of the treasure 
below. Mountains of gold as far as the eye
can see. You jump in for a swim, the 
treasure is yours! 
You Win!''')
            print("________________________________________________________________________")
            print("")

