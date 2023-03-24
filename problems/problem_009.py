# Complete the is_palindrome function to check if the value in
# the word parameter is the same backward and forward.
#
# For example, the word "racecar" is a palindrome because, if
# you write it backwards, it's the same word.

# It uses the built-in function reversed and the join method
# for string objects.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def is_palindrome(word):
    # first reverse the word and store it in a new variable
    reversed_word = word[::-1]
    # set up condition if the reversed word is equivalent to word
    if reversed_word == word:
        print(word + " is a palindrome!")
    else:
        print(word + " is not a palindrome.")

# Test Cases:
# is_palindrome(word="tree")
# is_palindrome(word="racecar")
# is_palindrome(word="kayak")
