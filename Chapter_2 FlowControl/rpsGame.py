import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0

while True:
    print(str(wins) + ' Wins ' + str(losses) + ' Losses ' + str(ties) + ' Ties')
    print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
    playerChoice = input()

    if playerChoice == 'q':
        sys.exit()
    elif playerChoice == 'r':
        print('ROCK versus...')
    elif playerChoice == 'p':
        print('PAPER versus...')
    else:
        print('SCISSORS versus...')

    computerChoice = random.randint(0, 2)
    
    if computerChoice == 0:
        computerChoice = str('r')
        print('ROCK')
    elif computerChoice == 1:
        computerChoice = str('p')
        print('PAPER')
    else:
        computerChoice = ('s')
        print('SCISSORS')

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