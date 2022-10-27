################################# Question 5 ###################################
# Now use an accumulator pattern to run the `roll_die` function 600 times with a
# different argument -- try the argument 12 -- and count how many times it
# returns 6.
#
# We expect on average this will be 1/12 * 600 = 50. But because it's random
# it will be a little bit different each time.

from q4 import roll_die

def main():
    # YOUR CODE HERE!
    print(roll_die(12))

if __name__ == "__main__":
    main()