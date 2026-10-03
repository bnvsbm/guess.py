import random
number = random.randint(1,10)
guess = int(input('Guess the number:'))

if guess==number:
    print('Excellent')
else:
    print('Try again')