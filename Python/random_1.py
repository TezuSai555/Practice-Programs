import random
num=random.randint(1,20)
guess=int(input('Enter your guess:'))
while num!=guess:
    if guess<num:
        print('too low!😒')
    else:
        print('too high!😢')
    guess=int(input('Guess Again🤔 :'))
print('Congratulations! You Won👌')