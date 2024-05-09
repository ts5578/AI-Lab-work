# import random module for computer to play randomly
import random

#printing the rules for the game 
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
	+ "Rock vs Paper -> Paper wins \n"
	+ "Rock vs Scissors -> Rock wins \n"
	+ "Paper vs Scissors -> Scissor wins \n")

while True:
	
	print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
	
	# user inputs the choice from above
	
	choice=int(input("Enter your choice :"))
	
	# if user enters an invalid input ask to enter a valif input
	while choice > 3 or choice <1:
	    choice=int(input('Enter a valid choice please '))
		
		# initialize value of choice_name variable corresponding to choice value
	if choice == 1:
		choice_name= 'Rock'
	elif choice == 2:
		choice_name= 'Paper'
	else:
		choice_name= 'Scissors'
		
		# print user choice
	print('User choice is \n',choice_name)
	print('\nNow its Computers Turn....')
	
	# Computer chooses randomly any number 
	comp_choice = random.randint(1,3)
	
	# looping until comp_choice value
	# is equal to the choice value
	while comp_choice == choice:
		comp_choice = random.randint(1,3)
		
	# initialize value of comp_choice_name
	# variable corresponding to the choice value
	if comp_choice == 1:
		comp_choice_name = 'rock'
	elif comp_choice == 2:
		comp_choice_name = 'paper'
	else:
		comp_choice_name = 'scissor'
	print("Computer choice is \n", comp_choice_name)
	print(choice_name,'Vs',comp_choice_name)
	# we need to check of a draw
	if choice == comp_choice:
		print('Its a Draw',end="")
		result="DRAW"
	# condition for winning	 
	if (choice==1 and comp_choice==2):
		print('paper wins ',end="")
		result='paper'
	elif (choice==2 and comp_choice==1):
		print('paper wins ',end="")
		result='Paper'
		
	
	if (choice==1 and comp_choice==3):
		print('Rock wins \n',end= "")
		result='Rock'
	elif (choice==3 and comp_choice==1):
		print('Rock wins \n',end= "")
		result='rocK'
		
	if (choice==2 and comp_choice==3):
		print('Scissors wins ',end="")
		result='scissor'
	elif (choice==3 and comp_choice==2):
		print('Scissors wins ',end="")
		result='Rock'
	# Printing either user or computer wins or draw
	if result == 'DRAW':
		print("\n<== Its a tie ==>")
	if result == choice_name:
		print("\n<== User wins ==>")
	else:
		print("\n<== Computer wins ==>")
	print("\nDo you want to play again? (Y/N)")
	# if user input n or N then condition is True
	ans = input().lower()
	if ans =='n':
		break
# after coming out of the while loop
# we print thanks for playing
print("thanks for playing")
