# Complete the max_of_three function so that returns the
# maximum of three values.
#
# If two values are the same maximum value, return either of
# them.
# If the all of the values are the same, return any of them
#
# Use the >= operator for greater than or equal to

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def max_of_three(value1, value2, value3):
    if value1 == value2 == value3:
        print(value1 or value2 or value3)
    elif value1 >= value2 and value1 >= value3:
        print(value1)
    elif value2 >= value1 and value2 >= value3:
        print(value2)
    else:
        print(value3)

#Test Case:
# max_of_three(7,5,7)
# max_of_three(1,2,3)
# max_of_three(9,4,7)
# max_of_three(16,2330.5,9)
