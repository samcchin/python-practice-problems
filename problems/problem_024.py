# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_average(values):
    if values == []:
        return None
    else:
        sum = 0
        for num in values:
            sum += num
        average = sum / len(values)
        print(average)

# # Test Cases:
# calculate_average([1,2,3])
# calculate_average([4,5,6])
