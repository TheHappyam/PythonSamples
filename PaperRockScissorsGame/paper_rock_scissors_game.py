import random

# import Logo and Vs from art.py
from paper_rock_scissors_game_art import game_images
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

def game():
    game_should_continue = True

    user_choice = int(input('Please choose: Type 0 for Paper , 1 for Rock or 2 for Scissors. -1 to Quit.\n'))

    if user_choice == -1:
        screen_clear()
        print('Thank you for playing.')
        game_should_continue = False

    while game_should_continue:

        screen_clear()

        if user_choice >= 3 or user_choice < 0:
            print('Invalid choice, You Lose!\n')

        else:
            print('You chose:')
            print(game_images[user_choice])

            computer_choice = random.randint(0,2)
            print('Computer chose:')
            print(game_images[computer_choice])

            if user_choice == 0 and computer_choice == 2:
                print('You lose...\n')
            elif computer_choice == 2 and user_choice == 0:
                print('You Win!\n')
            elif computer_choice > user_choice:
                print('You Win!\n')
            elif user_choice > computer_choice:
                print('You lose...\n')
            elif user_choice == computer_choice:
                print('Draw~\n')

        user_choice = int(input('Please choose: Type 0 for Paper , 1 for Rock or 2 for Scissors. -1 to Quit.\n'))

# Start the game
game()