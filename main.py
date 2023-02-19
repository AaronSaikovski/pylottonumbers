'''
SUMMARY:      Generates random numbers for use in  lotteries
DESCRIPTION:  Allows generation of numbers for Lotto, OzLotto and Powerball
			  Lotto - Allows for 1-45 numbers with 6 numbers per game and a maximum of 50 games per entry
			  Ozlotto - Allows for 1-47 numbers with 7 numbers per game and a maximum of 50 games per entry
			  Powerball - Allows for 1-35 numbers with 7 numbers per game and 1-20 single number for the Powerball number with a total maximum of 50 games per entry
AUTHOR/S:     asaikovski
VERSION:      1.0.0
VERSION HISTORY:
  1.0.0 - Rewritten in Python
'''

import random
import time
import os


def generate_random_numbers(maxVal, numbersPerGame):
    # Create a list to store the generated numbers
    numbers = []

    # seed the randomizer
    random.seed(time.time())

    # Generate random numbers until we have numbersPerGame of them
    while len(numbers) < numbersPerGame:
        # Generate a random number between 1 and maxVal
        n = random.randint(1, maxVal)

        # Check if the number has already been generated
        duplicate = False
        for v in numbers:
            if v == n:
                duplicate = True
                break

        # If the number is not a duplicate, add it to the list
        if not duplicate:
            numbers.append(n)

    # return the results list
    return numbers

#Spacer string
def printSpacer():
    print("*"*50)



def main():  
    printSpacer()
    print("** Lottery number generator - Python v1.0.0 **")
    printSpacer()
    
    #get input for number of games	
    max_num_games = int(input("How many games to play?: "))
    
    #Set the maximum random numbers per game
    max_random_numbers_per_game = int(input("Random number pool to use per game?: "))

    #get the maximum numbers per game
    max_numbers_per_game = int(input("Maximum numbers per game?: "))

    printSpacer()
    print("\n** Results **")
    for i in range(max_num_games):
        print("Game", i+1, generate_random_numbers(max_random_numbers_per_game, max_numbers_per_game))
    
    printSpacer()

#check for main()
if __name__ == '__main__':
	main()
