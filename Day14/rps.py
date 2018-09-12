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

def setUserHandName(userInputChoice):
    if userInputChoice == 'R':
        return 'Rock'
    elif userInputChoice == 'S':
        return 'Scissors'
    elif userInputChoice == 'P':
        return 'Paper'
    else:
        return 0

def game_loop():
    hands = [
        Hand('Rock'),
        Hand('Paper'),
        Hand('Scissors'),
    ]

    userInputChoice = input('Please enter [R]ock, [P]aper, or [S]cissors  ').upper()
    #print(userHandChoice)

    userHandChoice = setUserHandName(userInputChoice)
    print(userHandChoice)
    computerChoice = random.choice(hands)



    #print(f'Your {userHandChoice} vs the computers {computerChoice.name}')






if __name__ == '__main__':
    main()
