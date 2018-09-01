#! python3


# Basic pomodoro timer with choice on duration
# uses 4 intervals for long breaks for simplicity

from datetime import datetime
from datetime import timedelta
import time

# needs to be int seconds for sleep
shortBreak = 300

longBreak = 1800

# number of pomodoro iterations before long break
pomoCycles = 4


# gets current time
def getCurrentTime():
    return datetime.today()

# menu to be displayed
def displayMenu():
    print("\nEnter choice for timer length")
    print("1. 1 minutes? \n"
          "2. 15 minutes? \n"
          "3. 25 minutes? \n")



displayMenu()
userChoice = int(input())


if userChoice == 1:
    pomoDuration = timedelta(minutes=1)
elif userChoice == 2:
    pomoDuration = timedelta(minutes=15)
elif userChoice == 3:
    pomoDuration = timedelta(minutes=25)
else:
    print("Invalid Choice")



for _ in range(pomoCycles):
    currentTime = getCurrentTime()
    pomoEndTime = currentTime + pomoDuration

    print(f'\nSee you at {pomoEndTime.hour:02}:{pomoEndTime.minute:02} for more work!')

    while currentTime < pomoEndTime:
        currentTime = getCurrentTime()
        time.sleep(0.02)


    print("\nTime for a short break!")
    currentTime = getCurrentTime()
    time.sleep(shortBreak)

    print("\nBreak time is over!!")




print("\nlong break time!")
time.sleep(longBreak)
