################################# Question 6 ###################################
# Using the `random` module and user input, make an interactive game.

# We can take user input by using the `input` function. The argument you give to
# input shows a string in the terminal. The return value of the `input` function
# is whatever the user types before they hit the return key.
user_input = input("Type something here: ")
print("Great! Here's what you typed:")
print(f"{user_input=}")

# This is super open-ended, but some possible suggestions are:
#     * a guessing game where the computer has a number in mind and the user has
#       to guess the number. maybe the computer gives hints, maybe it doesn't
#     * a variation on an existing game, like blackjack
#     * a small choose your own adventure RPG where the computer tells a story
#       and the user can make some choices about where the story goes