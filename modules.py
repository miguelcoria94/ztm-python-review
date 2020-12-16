import sys
import random 

num_to_guess = random.randint(1, 10)


while True:
    try:
        guess = input('Guess a number 1-10 \n')
        if int(guess) < 0:
            print('Your number is to low')
        elif int(guess) > 10:
            print('Your number is to high')
        elif int(guess) == num_to_guess:
            print("You guessed the right number !!")
            break
        else:
            print("Try Again")
    except ValueError:
        print("I said guess a number")
    
