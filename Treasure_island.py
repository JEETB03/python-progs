print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


a = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ")

if a == "left":
    b = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ")

    if b == "wait":
        c = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which one do you choose? ")

        if c == "red":
            print("It opened to a pit of fire. You slipped into it and died. Game over.")
        elif c == "yellow":
            print("You found the treasure! You used it to create a kingdom of your own. You Win!")
        elif c == "blue":
            print("You enter a room of beasts. They ripped you apart. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")

    elif b == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("Invalid input. Game Over.")

elif a == "right":
    print("You fell off a cliff. Game Over.")

else:
    print("Invalid input. Game Over.")
