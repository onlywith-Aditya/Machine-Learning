# Generate random number
#Loop
    # Ask user to make a guess
    # If not valid number-> Print Error
    # If number < guess no.
    # Print-> Too  Hight
    # If number > guess no.
    # Print-> Too Low
    # If No==Guess.
    # Print Congratualtion. 

import random

guess_No= random.randint(1,100)
while True:
    try:
        sd_No= int(input("Guess The Number between [1-100]: "))
        print(f"Your number is: {sd_No}")

        if sd_No<guess_No:
            print("Too Low")
        elif sd_No>guess_No:
            print("Too High")
        else:
            print(f"Congratulations!!! Guess Number is: {sd_No}")
            break
    except ValueError:
        print("Please enter valid number")


