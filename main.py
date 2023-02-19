'''
SUMMARY:      Generates random numbers for use in  lotteries
DESCRIPTION:  Allows generation of numbers for various lotteries.
AUTHOR/S:     @asaikovski
VERSION:      1.0.0
VERSION HISTORY:
  1.0.0 - Rewritten in Python with input validation
'''
import random
import time
import os

#Generates the unique random numbers
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
def print_spacer():
    print("*"*55)

#decorator to check for a valid input value of ints
def validate_user_input(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result.isnumeric():
            return int(result)
        else:
            print("Input must be an valid number..exiting...")
            exit()
    return wrapper

#Get user input with validation
@validate_user_input
def get_user_input(input_message):
    user_input = input(input_message)
    return user_input

#main
def main():  
    print_spacer()
    print("** Lottery number generator - Python Edition v1.0.0 **")
    print_spacer()
    
    #get input for number of games	
    max_num_games = get_user_input("How many games to play?: ")
    
    #Set the maximum random numbers per game
    max_random_numbers_per_game = get_user_input("Random number pool to use per game?: ")

    #get the maximum numbers per game
    max_numbers_per_game = get_user_input("Maximum numbers per game?: ")

    print_spacer()
    print("\n** Results **")
    for i in range(max_num_games):
        print("Game", i+1, generate_random_numbers(max_random_numbers_per_game, max_numbers_per_game))
    
    print_spacer()

#check for main()
if __name__ == '__main__':
	main()
