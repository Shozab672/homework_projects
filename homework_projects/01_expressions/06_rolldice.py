## Problem Statement

#Simulate rolling two dice, and prints results of each roll as well as the total.

## Starter Code


def main():
    print("Roll the dice! :)")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()


## Solution


"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""
# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES: int = 6

def main():
    
    # Setting a seed is useful for debugging (uncomment the line below to do so!)
    # random.seed(1)
    
    # Roll dice
    dice1: int = random.randint(1, NUM_SIDES)
    dice2: int = random.randint(1, NUM_SIDES)
    
    # Get their total
    total: int = dice1 + dice2
    
    # Print out the results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First dice:", dice1)
    print("Second dice:", dice2)
    print("Total of two dice:", total)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

