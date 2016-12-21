# Roll the Dice Game
# by Raphael Gutierrez (fb.com/raphael.gutierrez.17)
# Licensed under MIT (https://github.com/ralphgutz/Dice-Rolling-Simulator/blob/master/LICENSE)

import time
import random

min = 1
max = 6

print("=" * 34)
print("= Welcome to Roll the Dice Game. =")
print("=" * 34)

user_input = input("\nRoll the dice? [Y/N] ")

def dice_roll():
	time.sleep(1)
	print("\nRolling dices...")
	time.sleep(1)
	print("Getting the values...\n")
	time.sleep(1)
	dice1 = random.randint(min, max)
	dice2 = random.randint(min, max)
	print("  Dice #1 -> ", dice1)
	print("  Dice #2 -> ", dice2)
	time.sleep(1)
	dices_sum = dice1 + dice2
	print("\n  The sum is", dices_sum)

if user_input == 'Y' or user_input == 'y':
	while (user_input == 'Y' or user_input == 'y'):
		dice_roll()
		user_input = input("\nRoll the dice again? [Y/N] ")

elif user_input == 'N' or user_input == 'n':
	print("Exiting")

else:
	print("Invalid Input!")
	