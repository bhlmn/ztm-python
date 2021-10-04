import sys
from random import randint


if __name__ == '__main__':
    lower = int(sys.argv[1])
    upper = int(sys.argv[2])
    the_num = randint(lower, upper)

    guess = None
    tries = 0
    while guess != the_num:
        try:
            guess = int(input(f'What do you think the number is? (between {lower} and {upper}) '))
            tries += 1
        except ValueError:
            print(f'Please enter an integer between {lower} and {upper}.')

    print(f'Good job! The number was {the_num}. It took you {tries} tries to guess it!')