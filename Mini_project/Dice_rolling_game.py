#Loop
    # Ask: Roll the dice?
    # If user enter "y"
    #   Generate two random number
    #   Print them
    # If user enter "n"
    #   Print Thank you message
    #   Terminates
    # Else
    #   Print Invalid Choice 

import random

while True:
    roll=input("Roll the dice? (y/n)").lower()
    if roll == "y":
        roll_1=random.randint(1,6)
        roll_2=random.randint(1,6)
        print(f'{roll_1},{roll_2}')
    elif roll == 'n':
        print("Thanks for playing")
        break
    else:
        print("Invalid!!!")

print("END")

