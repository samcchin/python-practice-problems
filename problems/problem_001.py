# Complete the minimum_value function so that returns the
# minimum of two values.
#
# If the values are the same, return either.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.


def minimum_value(value1, value2):
    if value1 == value2:
        return value1 or value2
    elif value2 < value1:
        return value2
    else:
        return value1

# SC:Test cases below
# minimum_value(23,23)
