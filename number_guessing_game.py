#Each time a number will be guessed
#User gets asked what is the number
#Based on their response, print if it is correct, too high or too low and terminate

import random
def guess_the_number():
    number = random.randint(1, 10)
    return number

def start_game(num):
    try:
        guessed_num = int(input("Guess the number: "))
        if guessed_num == num:
            print("You've guessed the correct number")
        elif guessed_num < num:
            print("Too low")
            start_game(num)
        else:
            print("Too high")
            start_game(num)
    except ValueError:
        print("Please enter a number")
        start_game(num)
        
if __name__ == '__main__':
    number = guess_the_number()
    start_game(number)