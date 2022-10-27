################################# Question 1 ###################################
import random

# PART A
# Modify the function called flip_fair_coin that returns "heads" half the time
# and "tails" half the time.

def flip_fair_coin():
    """Flip a fair coin
    
    Returns:
    str: returns either "heads" or "tails" with equal probability
    """
    #pass

# PART B
# Modify the function main that uses a for loop to run the `flip_fair_coin`
# function 10 times and print out the result each time
def main():
    print(flip_fair_coin())

if __name__ == "__main__":
    main()