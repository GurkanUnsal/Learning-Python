import random

def Answer(aNumber):
    if aNumber == 1:
           return 'No'
    elif aNumber == 2:
           return 'Yes'
    elif aNumber == 3:
           return 'Obviously'
    elif aNumber == 4:
           return 'Try again'
    elif aNumber == 5:
           return 'Ask again'
    elif aNumber == 6:
           return 'Do not even think about it'
    elif aNumber == 7:
           return 'Of course'
    elif aNumber == 8:
           return 'Please do not'
    elif aNumber == 9:
           return 'Go for it'

while True:
    print ('What do you want to ask to 8GudiBall?')
    response = input()
    x= random.randint(1, 9)
    print(Answer(x))
