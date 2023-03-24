# Complete the is_divisible_by_5 function to return the
# word "buzz" if the value in the number parameter is
# divisible by 5. Otherwise, just return the number.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def is_divisible_by_5(number):
    # set up condition if number is divisble by 5 to return buzz
    if number % 5 == 0:
        print("buzz")
    else:
        print(number)

# # Test Cases
# is_divisible_by_5(3)
# is_divisible_by_5(5)
# is_divisible_by_5(225)
