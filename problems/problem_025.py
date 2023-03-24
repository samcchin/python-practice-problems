# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
def calculate_sum(values):
    # If the list of values is empty, return None
    if values == []:
        return None
    else:
        # Set the sum counter to 0 and iterate through list to add num
        sum = 0
        for num in values:
            sum += num
        print(sum)

# # Test Cases:
# calculate_sum([1, 2, 3])
# calculate_sum([5,10,20])
