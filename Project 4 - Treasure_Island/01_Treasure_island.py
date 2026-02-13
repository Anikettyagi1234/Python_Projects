print('''
*******************
          |                   |                  |                     |
 ___|____.=""_;=.__|_____|_
|                   |  ,-"_,=""     "=.|                  |
|___________________|__"=._o___|"=.______________|___________________
          |                "=._o"=._      ______:=._o "=._."_.-="'"=.______ "=._."_.-="'"=.__________________|_______
|                   |___"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .  ` ,  "-._"-._   ". '__|___________________
          |           |o"=._ , " ; .". ,  "-._"-._; ;              |
 _________|___________| ;-.o"=._; ."  '."\ . "_____|_| ;     (#) -.o "=._.--"_o.-; ;    "-.o"=__/ " ,__.--o;   |
|___________________|_| ;     (#) -.o "=.__o____|___________________
____/______/__/__.__    __/__/__/__/___/______/____
/______/______/__/__/    _| _  _/__/___"=._o._; | ;_.--"o.--"_/__/__/=._o--.__/__/__/__/__/_"=.o|o_.--""_____________"=.__| _"o_/__/__/__/__/__/__/__/__/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************
''')
print(" Welcome to Treasure Island. Yoir mission is to Find the Treasure. ")
Choice1 = input(" You are at cross road. where do you want to go? Type 'Left' or 'Rigth' :- " ).lower()

if Choice1 == "left":
   #Continue in a Game.
    choice2 = input(" You come to a Lake. There is an island in the middle of the  Lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
    if choice2 == "wait":
        choice3 = input(" You arrive at the island unharmed. There is a house with 3 doors. One Red, One Yellow, One Blue.which colour do you choice?").lower()
        if choice3 == "red" or choice3 == "blue":
            print("It is a Room Full of Fire. Game Over.")
        elif choice3 == "yellow":
            print(" YOU Found the Treasure! You Win!")
        else:
           print("You choice a door that does'n exist. Game Over")
    else:
       print("You get attacked by an angry trout. Game Over")
else:
    print("You fell into a hole. Game Over.")