################################# Question 2 ###################################
#
# Modify the code below to test your `flip_fair_coin` function
#
# Use an accumulator pattern to run the `flip_fair_coin` function 100 times and
# count how many heads and how many tails you get.
#
# They probably won't be exactly 50 each, but they should be pretty close.

from q1 import flip_fair_coin

num_heads = 0
num_tails = 0
for _ in range(100):
    flip_fair_coin()

print(f"{num_heads = }")
print(f"{num_tails = }")