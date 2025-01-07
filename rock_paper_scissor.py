import random

valid_choices = ('r', 'p', 's')
emojis = {'r': '🪨',
            'p': '📄', 
            's': '✂️'}
    
while True:
    user_choice = input('Rock, paper, or scissors? (r/p/s): ')
    if user_choice not in valid_choices:
        print('Invalid choice')
        continue

    computer_choice = random.choice(valid_choices)
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer choice {emojis[computer_choice]}')

    if ((user_choice == 'r' and computer_choice == 's') or 
        (user_choice == 'p' and computer_choice == 'r') or 
        (user_choice == 's' and computer_choice == 'p')):
        print('You win')
    elif user_choice == computer_choice:
        print('Tie')
    else:
        print('You lose')

    continue_choice = input('Do you want to continue? (y/n): ')
    if continue_choice.lower() == 'n':
        break
    