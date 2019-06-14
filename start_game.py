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
		print('You win! You chose %s and the computer chose %s.' % (user_choice, cpu_choice))
		return 1
	elif((cpu_choice, user_choice) in win_list):
		print('You lost! You chose %s and the computer chose %s.' % (user_choice, cpu_choice))
		return -1
	else:
		print('It\'s a draw! You chose %s and the computer chose %s.' % (user_choice, cpu_choice))
		return 0


#function that runs the main game
def game():

	#initialiasing score variables
	player_score = 0
	cpu_score = 0

	#making a list of valid user inputs
	input_list = ['rock', 'paper', 'scissors','quit']

	while True:
		user_choice = ''
		#ask for user input and ask again 
		while(user_choice not in input_list):
			user_choice = input("Type rock, paper, scissors or type quit to end the game\n")
			if(user_choice not in input_list):
				print("Please type in the correct options from rock, paper, scissors, quit")

		#if user types quit to quit print the respective scores and announce the winner
		if(user_choice == 'quit'):
			print("Thanks for playing!\nYour score: %s\nComputer's score: %s" % (player_score, cpu_score))
			if(player_score > cpu_score):
				print("You won!")
			elif(player_score < cpu_score):
				print("You lost")
			else:
				print("It's a draw")

			print("Thanks for playing. Hope to see you again soon")
			return

		#pass user choice to the result function to calculate result
		game_result = result(user_choice)
		
		#update scores
		if(game_result == 1 ):
			player_score += 1
		elif(game_result == -1):
			cpu_score += 1

		#print scores
		print("Your score: %s\nComputer's score: %s" % (player_score, cpu_score))


#run game
game()






