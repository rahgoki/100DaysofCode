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

# returns Hand with rock, paper, scissors as name property
def setUserHandName(userHandChoice):
    if userHandChoice == 'R':
        return Hand('Rock')
    elif userHandChoice == 'S':
        return Hand('Scissors')
    elif userHandChoice == 'P':
        return Hand('Paper')
    else:
        return 0

# if user wins...print this message
def winMessage():
    return 'You Win!!'

# if user is defeated...print this message
def loseMessage():
    return 'You have been defeated!!'


# game logic
def game_loop():
    # create list of objects for computer to chose from
    hands = [
        Hand('Rock'),
        Hand('Paper'),
        Hand('Scissors'),
    ]

    while True:
        # get user input as char and convert to full name
        userHandChoice = setUserHandName(input('Please enter [R]ock, [P]aper, [S]cissors, 0 to exit  ').upper())

        # random choice to compare to
        computerChoice = random.choice(hands)

        # lazy error handling
        if userHandChoice == 0:
            print('***Exiting***')
            break



        print(f'Your {userHandChoice.name} vs the computers {computerChoice.name}')


        if userHandChoice.name == computerChoice.name:
            print('It''s a tie!!!')
        # user choses rock
        elif userHandChoice.name == 'Rock' and computerChoice.name == 'Scissors':
            print(winMessage())
        elif userHandChoice.name == 'Rock' and computerChoice.name == 'Paper':
            print(loseMessage())
        # user choses paper
        elif userHandChoice.name == 'Paper' and computerChoice.name == 'Rock':
            print(winMessage())
        elif userHandChoice.name == 'Paper' and computerChoice.name == 'Scissors':
            print(loseMessage())
        # user choses scissors
        elif userHandChoice.name == 'Scissors' and computerChoice.name == 'Paper':
            print(winMessage())
        elif userHandChoice.name == 'Scissors' and computerChoice.name == 'Rock':
            print(loseMessage())
        else:
            print('something went wrong')





if __name__ == '__main__':
    main()
