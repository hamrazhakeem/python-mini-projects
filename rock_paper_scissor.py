import random

valid_choices = ('r', 'p', 's')
emojis = {'r': '🪨',
            'p': '📄', 
            's': '✂️'}
    
def get_user_choice():
    while True:
        user_choice = input('Rock, paper, or scissors? (r/p/s): ')
        if user_choice in valid_choices:
            return user_choice
        else:
            print('Invalid choice')

def print_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer choice {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if ((user_choice == 'r' and computer_choice == 's') or 
        (user_choice == 'p' and computer_choice == 'r') or 
        (user_choice == 's' and computer_choice == 'p')):
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