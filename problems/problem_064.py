# Write a function that meets these requirements.
#
# Name:       temperature_differences
# Parameters: highs: a list of daily high temperatures
#             lows: a list of daily low temperatures
# Returns:    a new list containing the difference
#             between each high and low temperature
#
# The two lists will be the same length
#
# Example:
#     * inputs:  highs: [80, 81, 75, 80]
#                lows:  [72, 78, 70, 70]
#       result:         [ 8,  3,  5, 10]


def temperature_differences(highs, lows):
    difference_list = []

    for index in range(0, len(highs)):
        difference = highs[index] - lows[index]
        difference_list.append(difference)
    print(difference_list)

# Test Case
# highs = [80, 81, 75, 80]
# lows = [72, 78, 70, 70]
# temperature_differences(highs,lows)

# Set up new list to store difference
# Using for loop, subtract the highs[i] - lows[i]
# Store difference in new list
# Return new list
