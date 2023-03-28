# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]

def halve_the_list(list):
    half_list_length = int(len(list)/2)
    if len(list) % 2 == 0:
        return list[:half_list_length], list[half_list_length:]
    else:
        return list[:half_list_length+1], list[half_list_length+1:]


# Test Case:
print(halve_the_list([1, 2, 3, 4]))
print(halve_the_list([1, 2, 3]))
