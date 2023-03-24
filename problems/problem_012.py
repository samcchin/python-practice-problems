# Complete the fizzbuzz function to return
# * The word "fizzbuzz" if number is evenly divisible by
#   by both 3 and 5
# * The word "fizz" if number is evenly divisible by only
#   3
# * The word "buzz" if number is evenly divisible by only
#   5
# * The number if it is not evenly divisible by 3 nor 5
#
# Try to combine what you have done in the last two problems
# from memory.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def fizzbuzz(number):
    # Set condition The word "fizzbuzz" if number is evenly divisible by
    # both 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    # Set condition The word "fizz" if number is evenly divisible by 3
    elif number % 3 == 0:
        print("fizz")
    # Set condition The word "buzz" if number is evenly divisible by 5
    elif number % 5 == 0:
        print("buzz")
    # Set condition to print num if neither divisble by 3 or 5
    else:
        print(number)

# Test Cases
# fizzbuzz(3)
# fizzbuzz(15)
# fizzbuzz(5)
# fizzbuzz(298)
# fizzbuzz(1)
