#!python3

from rpsClass import Hand
import random

def main():
    print_header()
    game_loop()


def print_header():
    print('------------------------------------')
    print('        Rock Paper Scissors')
    print('------------------------------------\n\n')


def game_loop():
    hands = [
        Hand('Rock'),
        Hand('Paper'),
        Hand('Scissors'),
    ]

    userHandChoice = input('Please enter [R]ock, [P]aper, or [S]cissors  ').upper()
    #print(userHandChoice)

    computerChoice = random.choice(hands)

    print(f'Your {userHandChoice} vs the computers {computerChoice.name}')



if __name__ == '__main__':
    main()
