import random

Digit1 = random.randint(1, 9)
Digit2 = random.randint(1, 9)
Digit3 = random.randint(1, 9)
Digit4 = random.randint(1, 9)
Digit5 = random.randint(1, 9)


print('You have 3 tries to guess each digit of a 5 digit number. Lets see if you can do it!')
print('Good Luck!')

Name = input('What is you name?')

while True:
    Guess = int(input(f'What is you guess for the first digit {Name}?'))
    if Digit1 == Guess:
        print('Congrats! You did it! Lets move on to another digit!')
        Guess = int(input(f'What is you guess for the second digit {Name}?'))
        if Digit2 == Guess:
            print('Nice! Lets go to the third digit!')

    if Digit1 > Guess:
        print('Too low Try again')
    else:
        print('Too high, try again')