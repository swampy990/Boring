#This is a guess the number game
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

#Ask the player for a number 6 times

for guessesTaken in range(1, 7):
    print('Take a Guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your Guess is too low')
    elif guess > secretNumber:    print('Your Guess is too high')
    else:
        break


if guess == secretNumber:
        print('Good Job! You guessed my number in ' + str(guessesTaken))
else:
        print('Nope, the number I was thinking of was ' + str(secretNumber))