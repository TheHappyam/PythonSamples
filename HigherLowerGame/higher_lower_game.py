import random

# import Logo and Vs from art.py
from higher_lower_game_art import logo, vs
# import data from game_data.py
from higher_lower_game_data import data
# import only system from os
from os import system, name as os_name


# define Screen Clear function
def screen_clear():
    # for windows
    print(os_name)
    if os_name == 'nt':
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


# Generate a random account from the game data.
def get_random_account():
    """Get data from random account"""
    return random.choice(data)


# Format account data into printable format.
def format_data(account):
    """Format account into printable format: name, description and country"""
    account_name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{account_name}, a {description}, from {country}"


# Check if user is correct.
def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    # Add art (Logo)
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    # Make game repeatable.
    while game_should_continue:
        # Make B become the next A.
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        # Add art (VS)
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Ask user for a guess.
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Get follower count.
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Clear screen between rounds.
        screen_clear()

        # Add art (Logo)
        print(logo)
        # Feedback.
        if is_correct:
            # Score Keeping.
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            # Game would return False if user's answer is wrong
            # Game would also return False if user did not enter A or B
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


# Start the game
game()
