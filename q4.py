################################# Question 4 ###################################
import random

# PART A
# Make a function `roll_die` that simulates a single roll of a die. The number
# of sides on the die will be determined by the parameter sides.

def roll_die(sides):
    """Flip a fair die with a given number of sides

    Parameters:
    sides (int): number of sides on the die
    
    Returns:
    int: returns a number between 1 and sides inclusive with equal probability
    """
    pass

# PART B
# Modify the `main` function to use the code from q3 to test the `roll_die`
# function when the argument is 6.
# You should get similar results to what you got for q3.
def main():
    print(roll_die(6))

if __name__ == "__main__":
    main()