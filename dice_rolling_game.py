import random

def welcome_message():
    print("Roll the dice? (y/n)")
    choice = input()
    return choice

def roll_dice():
    choice = welcome_message()
    if choice == choice.lower() == "y":
        print((random.randint(1, 6), random.randint(1, 6)))
        roll_dice()
    elif choice == choice.lower() == "n":
        print("Goodbye!")
    else:
        print("Enter the correct choice!")
        roll_dice()

if __name__ == '__main__':
    roll_dice()