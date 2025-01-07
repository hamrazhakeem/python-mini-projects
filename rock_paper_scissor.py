import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = {ROCK: '🪨', PAPER: '📄', SCISSORS: '✂️'}
valid_choices = tuple(emojis.keys())
    
def get_user_choice():
    while True:
        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if user_choice in valid_choices:
            return user_choice
        else:
            print('Invalid choice')

def print_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer choice {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if ((user_choice == ROCK and computer_choice == SCISSORS) or 
        (user_choice == PAPER and computer_choice == ROCK) or 
        (user_choice == SCISSORS and computer_choice == PAPER)):
        print('You win')
    elif user_choice == computer_choice:
        print('Tie')
    else:
        print('You lose')

def start_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(valid_choices)

        print_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input('Do you want to continue? (y/n): ').lower()
        if should_continue == 'n':
            break

start_game()