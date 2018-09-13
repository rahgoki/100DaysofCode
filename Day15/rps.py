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

# if user wins...print this message and return 1 to incremement userScore
def winMessage():
    print('You Win!!')
    return 1

# if user is defeated...print this message and return 0 to not increment userScore
def loseMessage():
    print('You have been defeated on this go around!')
    return 0


# game logic
def game_loop():
    # create list of objects for computer to chose from
    hands = [
        Hand('Rock'),
        Hand('Paper'),
        Hand('Scissors'),
    ]

    # used to track whether the user wins or the computer
    userScore = 0

    # number of matches played in 1 "game"
    # count used for loop and numTurns for final message
    numTurns = 3
    numTurnsCount = numTurns

    while numTurnsCount > 0:
        # get user input as char and convert to full name
        userHandChoice = setUserHandName(input('Please enter [R]ock, [P]aper, [S]cissors, 0 to exit  ').upper())

        # random choice to compare to
        computerChoice = random.choice(hands)

        # lazy error handling
        if userHandChoice == 0:
            print('***Exiting***')
            break

        print(f'Your {userHandChoice.name} vs the computers {computerChoice.name}')

        # check to see who won and display appropriate message
        if userHandChoice.name == computerChoice.name:
            print('It''s a tie!!!')
        # user choses rock
        elif userHandChoice.name == 'Rock' and computerChoice.name == 'Scissors':
            #print(winMessage())
            userScore += winMessage()
            numTurnsCount -= 1
        elif userHandChoice.name == 'Rock' and computerChoice.name == 'Paper':
            #print(loseMessage())
            userScore += loseMessage()
            numTurnsCount -= 1
        # user choses paper
        elif userHandChoice.name == 'Paper' and computerChoice.name == 'Rock':
            #print(winMessage())
            userScore += winMessage()
            numTurnsCount -= 1
        elif userHandChoice.name == 'Paper' and computerChoice.name == 'Scissors':
            #print(loseMessage())
            userScore += loseMessage()
            numTurnsCount -= 1
        # user choses scissors
        elif userHandChoice.name == 'Scissors' and computerChoice.name == 'Paper':
            #print(winMessage())
            userScore += winMessage()
            numTurnsCount -= 1
        elif userHandChoice.name == 'Scissors' and computerChoice.name == 'Rock':
            #print(loseMessage())
            userScore += loseMessage()
            numTurnsCount -= 1
        else:
            print('something went wrong')


    if userScore > 1:
        print(f'You won with a score of {userScore} out of {numTurns}')
    else:
        print(f'You lose with a score of {userScore} out of {numTurns}')





if __name__ == '__main__':
    main()
