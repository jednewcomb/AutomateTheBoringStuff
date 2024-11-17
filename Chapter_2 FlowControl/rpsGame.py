import random, sys
def printPlayerChoice(playerChoice):
    if playerChoice == 'q':
        sys.exit()
    elif playerChoice == 'r':
        print('ROCK versus...')
    elif playerChoice == 'p':
        print('PAPER versus...')
    else:
        print('SCISSORS versus...')

def getComputerChoice(number):
     if number == 0:
        print('ROCK')
        return 'r'
     elif number == 1:
        print('PAPER')
        return 'p'
     else:
        print('SCISSORS')
        return 's'
        
print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses,  %s Ties' % (wins, losses, ties))
    print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')

    playerChoice = input()
    printPlayerChoice(playerChoice)
    computerChoice = getComputerChoice(random.randint(0, 2))

    if playerChoice == computerChoice:
        print('It is a tie!')
        ties += 1
        continue

    if playerChoice == 'r':
        if computerChoice == 's':
            print('You win!')
            wins += 1
        else:
            print('You lose!')
            losses += 1

    if playerChoice == 'p':
        if computerChoice == 'r':
            print('You win!')    
            wins += 1
        else:
            print('You lose!')
            losses += 1

    if playerChoice == 's':
        if computerChoice == 'p':
            print('You win!')
            wins += 1
        else:
            print('You lose!')
            losses += 1