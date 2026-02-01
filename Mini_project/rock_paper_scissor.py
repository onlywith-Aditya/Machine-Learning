# Ask user to make choice
# If choice is not valid 
    # Print Error
# Else 
    # Let the computer makes choice.
        # Print Choice(Emojis)
    # Determine the Winner
    # Ask the user if they want to continue
    # If not
        # Terminate
#-----------------------------
import random


# Now instead of using If and else statements for emojis we are gonna used dictornary.



def get_user_choice():
    while True:
        # This is not very effective way.

        # if user_choice != Rock and user_choice != Scissor and user_choice != Paper:
        #     print("Invalid Choice!!!")
        # Instead used truple or list. Truple bec. we can't modify in that.

        user_choice= input("Rock, Papaer, or Scissors? (r/p/s): ").lower()

        if user_choice not in choices:
            print("Invalid Choice!!!")
            continue
        else:
            return user_choice
        

def display_choices(user_choice, computer_choice):
    print(f"You Chose: {emojis[user_choice]}")
    print(f"Computer Chose: {emojis[computer_choice]}")
    

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice != computer_choice:
        if (
        (user_choice == Rock and computer_choice == Scissor) or
        (user_choice == Scissor and computer_choice == Paper) or
        (user_choice == Paper and computer_choice == Rock)):
            print("You Win") 
        else:
            print("You Lose")
    else:
        print("BIG ERROR!!!!!")

def play_game():
    while True:

        user_choice= get_user_choice()

        computer_choice= random.choice(choices)

        # Display Choices
        display_choices(user_choice, computer_choice)
        

        # Detemine a winner
        winner(user_choice, computer_choice)
        

        should_continue= input("Continue? (y/n): ").lower()
        if should_continue == 'n':
            break
    print("Thank You | The End---------------------|")


#--------------------------Void main

Rock= 'r'
Paper= 'p'
Scissor= 's'

emojis= {
    Rock: '🪨',
    Scissor: '✂️',
    Paper: '📃'
}

choices= tuple(emojis.keys())

play_game()
