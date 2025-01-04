import random

rolled_dice = 0
def roll_dice():
    global rolled_dice
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "y":
        no_of_dice = int(input("Enter the number of dice to roll: "))
        for i in range(no_of_dice):
            print(random.randint(1, 6), end=" ")
        rolled_dice += 1
        print()
        roll_dice() 
    elif choice == "n":
        print(f"You rolled the dice {rolled_dice} times.")
        print("Goodbye!")
    else:
        print("Enter the correct choice!")
        roll_dice()

if __name__ == '__main__':
    roll_dice()