import random

while True:
    number = random.randint(1,10)
    print ('Guess a number between 1 and 10. You have 4 guesses')

    for guessesTaken in range (1,5):
        print ('Take a guess')
        guess = int(input())

        if guess > number:
            print ('That guess is too high')
        elif guess < number:
            print ('That guess is too low')
        else:
            break

    if guess != number:
        print ('Bad luck. The number was ' + str(number))
    else:
        print ('Gratz. You got it in ' + str(guessesTaken) + ' guesses')
