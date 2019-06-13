# Make a single player rock paper scissors using python 3

import random

#function to handle the game logic
#user choice passed as parameter as a string in lower case
#returns 1 if user wins, -1 if the cpu wons and 0 if its a draw
def result(user_choice):
	#list of possible choices for the cpu to choose from
	choice_list = ['rock', 'paper', 'scissors']
	cpu_choice = random.choice(choice_list)

	#list of possible win combinations
	win_list = [('paper', 'rock'), ('rock', 'scissors'), ('scissors', 'paper')]

	#if a tuple of user_choice then cpu_choice exists in win list that means that the user won and vice versa. Otherwise it is a draw.
	if((user_choice, cpu_choice) in win_list):
		print('You win! You chose %s and the computer chose %s.'(user_choice, cpu_choice))
		return 1
	elif((cpu_choice, user_choice) in win_list):
		print('You lost! You chose %s and the computer chose %s.'(user_choice, cpu_choice))
		return -1
	else:
		print('It\'s a draw! You chose %s and the computer chose %s.'(user_choice, cpu_choice))
		return 0




