import custom_func
import random

# Constants
GAME_VALUES = ["rock", "paper", "scissor"]

# Global counters
total_play_value = 0
user_win_value = 0


def play_game(user_choice: str) -> None:
    """Simulate one round of the game."""
    global total_play_value, user_win_value

    # Computer Choice
    computer_choice = random.choice(GAME_VALUES)
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"The computer chose: {computer_choice.capitalize()}")

    # Determine Winner
    if user_choice.startswith("r") and computer_choice == "scissor":
        user_win_value, total_play_value = custom_func.game_win_strike("You win! Rock beats Scissor.", user_win_value, total_play_value)
    elif user_choice.startswith("p") and computer_choice == "rock":
        user_win_value, total_play_value = custom_func.game_win_strike("You win! Paper beats Rock.", user_win_value, total_play_value)
    elif user_choice.startswith("s") and computer_choice == "paper":
        user_win_value, total_play_value = custom_func.game_win_strike("You win! Scissor beats Paper.", user_win_value, total_play_value)
    elif user_choice.startswith(computer_choice[0]):
        user_win_value, total_play_value = custom_func.game_tie_strike(user_win_value, total_play_value)
    else:
        user_win_value, total_play_value = custom_func.game_lose_strike(f"You lose! {computer_choice.capitalize()} beats {user_choice.capitalize()}.", user_win_value, total_play_value)


# Main Program
if __name__ == "__main__":
    # Initial Prompt
    while True:
        entry = input("It is a Rock, Paper, Scissor game.\nIf you want to play type (yes/no): ").strip().lower()
        if custom_func.initial_prompt(entry):
            break

    # Ask for the player's name
    name = input("Enter Your Name: ").strip().capitalize()
    print(f"\nHello, {name}. Welcome to Rock, Paper, Scissor game.")
    print("""\nYour choices are:
        Rock = R
        Paper = P
        Scissor = S""")

    # Game Loop
    while True:
        user_choice = input("\nEnter Your Choice: ").strip().lower()
        if user_choice in ["rock", "r", "paper", "p", "scissor", "s"]:
            play_game(user_choice)
        elif user_choice == "exit":
            custom_func.exit()
        elif user_choice == "reset":
            print("Starting a new round...\n")
            total_play_value = 0
            user_win_value = 0
            continue
        else:
            print("""Invalid choice! Please choose from:
        Rock = R
        Paper = P
        Scissor = S \nIf you want to exit type (exit) \nIf you want to reset game type (reset)""")
