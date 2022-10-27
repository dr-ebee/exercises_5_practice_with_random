################################# Question 3 ###################################
import random

# PART A
# Make a function `roll_d6` that simulates a single roll of a six-sided die. The
# function will return 1, 2, 3, 4, 5, or 6 with equal probability.

def roll_d6():
    """Flip a fair 6-sided die
    
    Returns:
    int: returns a number between 1 and 6 inclusive with equal probability
    """
    pass

# PART B
# Modify the code below to test your `roll_d6` function
#
# Use an accumulator pattern to run the `roll_d6` function 600 times and
# count how many times it returns 6.
#
# We expect on average this will be 1/6 * 600 = 100. But because it's random
# it will be a little bit different each time.
def main():
    num_sixes = 0
    for _ in range(600):
        roll_d6()

    print(f"{num_sixes = }")

if __name__ == "__main__":
    main()