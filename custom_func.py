import sys

def exit() -> None:
    """Exit the game."""
    print("Exited successfully")
    sys.exit()

def initial_prompt(entry: str) -> bool:
    """Process the initial game prompt."""
    if entry == "yes":
        return True
    elif entry == "no":
        exit()
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        return False

def game_win_strike(msg: str, user_win_value: int, total_play_value: int) -> tuple:
    """Update and display user stats on a win."""
    total_play_value += 1
    user_win_value += 1
    print(msg)
    print(f"Your current wins: {user_win_value} out of {total_play_value}")
    return user_win_value, total_play_value

def game_lose_strike(msg: str, user_win_value: int, total_play_value: int) -> tuple:
    """Update and display user stats on a loss."""
    total_play_value += 1
    user_win_value -= 1
    print(msg)
    print(f"Your current wins: {user_win_value} out of {total_play_value}")
    return user_win_value, total_play_value

def game_tie_strike(user_win_value: int, total_play_value: int) -> tuple:
    """Update and display user stats on a tie."""
    total_play_value += 1
    print("It's a tie!")
    print(f"Your current wins: {user_win_value} out of {total_play_value}")
    return user_win_value, total_play_value
