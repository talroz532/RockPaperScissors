import random

ComputerChoice = ["rock", "paper", "scissors"]

print('To exit, press x')

gameLoop = True

while(gameLoop):
	inputUser =input('Enter your choice: ["rock", "paper", "scissors"] \n').lower()
	value = random.choice(ComputerChoice)
	if inputUser == value:
		print(f'{inputUser} | {value} TIED! \n')

	elif inputUser== "rock" and value=="paper":
		print(f'{inputUser} | {value} You LOST! \n')

	elif inputUser== "rock" and value=="paper":
		print(f'{inputUser} | {value} You WON! \n')

	elif inputUser== "paper" and value=="rock":
		print(f'{inputUser} | {value} You WON! \n')

	elif inputUser== "paper" and value=="scissors":
		print(f'{inputUser} | {value} You LOST! \n')

	elif inputUser== "scissors" and value=="rock":
		print(f'{inputUser} | {value} You LOST! \n')

	elif inputUser== "scissors" and value=="paper":
		print(f'{inputUser} | {value} You WON! \n')

	elif inputUser=='x':
		print('Bye Bye! \n')
		gameLoop = False
	else:
		print('invalid Input! \n')
		gameLoop = False
