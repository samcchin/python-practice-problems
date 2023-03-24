# Complete the sum_of_squares function which accepts
# a list of numerical values and returns the sum of
# each item squared
#
# If the list of values is empty, the function should
# return None
#
# Examples:
#   * [] returns None
#   * [1, 2, 3] returns 1*1+2*2+3*3=14
#   * [-1, 0, 1] returns (-1)*(-1)+0*0+1*1=2
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def sum_of_squares(values):
    if values == []:
        print(None)
    else:
        sum = 0
        for num in values:
            squared_num = num ** 2
            sum += squared_num
        print(sum)

# Test Cases:
# sum_of_squares([1,2,3,4])
# sum_of_squares([0,2,1,0])
# sum_of_squares([1,1,1,1])
# sum_of_squares([0])
# sum_of_squares([0])

# Return None if the list is empty
# Loop through each num in the list and square it
# Add the result of each squared value
# Return an integer value
