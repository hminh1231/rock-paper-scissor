import random
import time
import sys
from random import randrange

playerscore = 0
computerscore = 0
round = 0
computerchoice = ['rock', 'paper', 'scissor']
intro1 = '''Welcome to the Squid game 2.0 \n
This time, you will play a game called "rock, paper, scissor"'''

for i in intro1.split():
    sys.stdout.write(f"{i} ")
    sys.stdout.flush()
    time.sleep(0.5)

time.sleep(2)
print('\nAre you ready?')
time.sleep(1)
print('1.Yes \n2. No')
time.sleep(1)
userchoice = int(input('What is your choice: '))

while userchoice == 1:
    round += 1
    print(f'Round {round} start')
    time.sleep(1)
    userplay = input("Rock, paper or Scissor: ")
    fixword = userplay.lower()
    while fixword not in computerchoice:
        userplay = input('This is not valid, please choose again: ')
        fixword = userplay.lower()
    result = random.choice(computerchoice)
    time.sleep(1)
    print(f'Your choice is {fixword}')
    time.sleep(1)
    print('And computer choice is: ')
    time.sleep(2)
    print(result)

    if fixword == result:
        print('You are safe this time')
    elif (fixword == 'rock' and result == 'scissor') or (fixword == 'scissor' and result == 'paper') \
        or (fixword == 'paper' and result == 'rock'):
        print('You win this round')
        playerscore += 1
    else:
        print('You loose')
        computerscore += 1
    print('')
    time.sleep(1)

    if computerscore == 2 and playerscore < 2:
        print('Careful, you already loose 2 round, You only have 1 chance left only')
    elif computerscore == 2 and playerscore == 2:
        print('Careful, you only have 1 chance left, the next round will decide your fate')
    elif computerscore == 3:
        print("You loose, you won't have any squid now")
        time.sleep(2)
        break
    elif playerscore == 3:
        print('Congrat, you win this game, see you in next game')
        time.sleep(2)
        break
    
    
 
    

