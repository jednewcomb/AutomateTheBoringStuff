import random

number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

guess = 0
guessCount = 0
while (guess != number):
    print('Take a guess.')
    
    guess = int(input())
    if guess > number:
        print('Your guess is too high')
    elif guess < number:
        print('Your guess is too low.')
    guessCount += 1

print('Good job! You guessed my number in ' + str(guessCount) + ' guesses')