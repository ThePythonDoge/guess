#!/usr/bin/python
import getpass
import time
import random

guesses = int(1)

print('Welcome to the guess your mates number game')
print()
time.sleep(1)
print()
print('select how many players')
print('    1.) player - the computer will generate a number for you to guess between 0 and 100')
print('    2.) player - your mate will choose a number for you to guess')
players = input('[1] or [2]?')

if int(players) == 2:
	theNumber = getpass.getpass('Please enter a number for your mate to guess (NOTE: your input will be hidden): ')
	time.sleep(1)
	print()
	print('Alright now hand the keyboard over to your mate he will have to guess. see how many attempts it takes him to guess')
else:
	theNumber = str(random.randint(0,100))
	time.sleep(0.5)
	print('Okay now its time to guess the number')

time.sleep(1)
print()

i=input('please enter a guess: ')

while int(i) != int(theNumber):

	if i == 'quit':
		print ('you lose the answer was ' + theNumber)
		print('you had ' + str(guesses) + ' attempts')
		print()
		print('Game will automatically close in 5 seconds')
		time.sleep(5)
		exit()	

		
	print()
	print ('#***********************************#')
	print()
	print('you chose: ' + i)
	print()
	if int(i) > int(theNumber):
		print('try lower')
	else:
		print('try higher')
	print()
	guesses = guesses+1
	print('enter another guess or type [quit] to give up')
	print()
	i = input('Please try again: ')
	
	

print ('#***********************************#')
print('well done you win')
print()
print(str(i) + ' is right!!!')
print()
print('took ' + str(guesses) + ' guesses')
print()
print('Game will automatically close in 5 seconds')
time.sleep(5)

exit();
