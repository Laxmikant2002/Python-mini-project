import random  # Import the random module for generating random choices

game_images = ['rock', 'paper', 'scissors']

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("You chose:", game_images[user_choice])

computer_choice = random.randint(0, 2)  # Generate a random choice for the computer
print("Computer chose:", game_images[computer_choice])

# Determine the winner based on the game rules
if user_choice == 0 and computer_choice == 2:
    print("You win! Rock smashes scissors.")
elif computer_choice == 0 and user_choice == 2:
    print("You lose! Rock smashes scissors.")
elif user_choice > computer_choice:  # Simplified logic for remaining cases
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
else:
    print("It's a draw!")
