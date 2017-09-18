#!/usr/bin/python
import getpass
import time
import random

def delay(x):
	time.sleep(x)

guesses = int(1)

print('Welcome to the guess your mates number game\n')
delay(1)
print('select how many players\n')
print('    1.) player - the computer will generate a number for you to guess between 0 and 100\n')
print('    2.) player - your mate will choose a number for you to guess\n')
players = input('[1] or [2]?')

if int(players) == 2:
	theNumber = getpass.getpass('Please enter a number for your mate to guess (NOTE: your input will be hidden): ')
	delay(1)
	print('Alright now hand the keyboard over to your mate he will have to guess. see how many attempts it takes him to guess\n')
elif int(players) == 1:
	theNumber = str(random.randint(0,100))
	delay(0.5)
	print('Okay now its time to guess the number\n')

delay(1)

i = input('please enter a guess\n')

while int(i) != int(theNumber):

	if i == 'quit':
		print ('you lose the answer was ' + theNumber)
		print('you had ' + str(guesses) + ' attempts')
		print()
		print('Game will automatically close in 5 seconds')
		time.sleep(5)
		exit(2)	

		
	print ('#***********************************#')
	print('you chose: ' + i\n)
	if int(i) > int(theNumber):
		print('try lower')
	else:
		print('try higher')
	guesses = guesses+1
	print('enter another guess or type [quit] to give up\n')
	i = input('Please try again:\n')
	
	

print ('#***********************************#') #What is this? Also why did you put "print()" empty? is it like a new line? -ThePythonDoge
print('well done you win'\n)
print(str(i) + ' is right!!!'\n)
print()
print('took ' + str(guesses) + ' guesses'\n)
print('Game will automatically close in 3 seconds'\n)
delay(3)
exit(2);
