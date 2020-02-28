import random

print('-----------------------------')
print('   GUESS THAT NUMBER GAME')
print('-----------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)
    
    if guess < the_number:
        print('Your guess of {} was too LOW'.format(guess))
    elif guess > the_number:
        print('Your guess of {} was too HIGH'.format(guess))
    else:
        print('you win with the guess of {}!'.format(guess))

