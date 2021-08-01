import random
import sys

print ('Lets play ROCK, PAPER and SCISSORS with Gudi!!!')

wins = 0
losses = 0
ties = 0

while True:     #Game Loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: #Player Loop
        print ('Enter your move: (r)ock, (p)aper, (s)cissors. Enter (q) to quit.')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #Quit playing
        if playerMove == 'r' or 'p' or 's':
            break
        print ('Enter your move again as (r)ock, (p)aper, (s)cissors')

    if playerMove == 'r':
        print ('You chose rock')
    elif playerMove == 'p':
        print ('You chose paper')
    elif playerMove == 's':
        print ('You chose scissors')

    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print ('Computer chose rock')
    elif randomNumber == 2:
        computerMove = 'p'
        print ('Computer chose paper')
    elif randomNumber == 3:
        computerMove = 's'
        print ('Computer chose scissors')

    if computerMove == playerMove:
        print ('It is a tie')
        ties = ties + 1
    elif computerMove == 'r' and playerMove == 's':
        print ('Computer wins')
        losses = losses + 1
    elif computerMove == 's' and playerMove == 'p':
        print ('Computer wins')
        losses = losses + 1
    elif computerMove == 'p' and playerMove == 'r':
        print ('Computer wins')
        losses = losses + 1
    elif computerMove == 'p' and playerMove == 's':
        print ('You win!')
        wins = wins + 1
    elif computerMove == 'r' and playerMove == 'p':
        print ('You win!')
        wins = wins + 1
    elif computerMove == 's' and playerMove == 'r':
        print ('You win!')
        wins = wins + 1
