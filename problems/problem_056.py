# Write a function that meets these requirements.
#
# Name:       num_concat
# Parameters: two numerical parameters
# Returns:    the concatenated string conversions
#             of the numerical parameters
#
# Examples:
#     input:
#       parameter 1: 3
#       parameter 2: 10
#     returns: "310"
#     input:
#       parameter 1: 9238
#       parameter 2: 0
#     returns: "92380"


def num_concat(num1, num2):
    result = str(num1) + str(num2)
    print(result)

# Test cases
# num_concat(9238,0)
# num_concat(10,3)
# num_concat(45, 29)
# num_concat(415, 2239)
