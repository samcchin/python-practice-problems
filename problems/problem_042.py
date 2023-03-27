# Complete the pairwise_add function which accepts two lists
# of the same size. It creates a new list and populates it
# with the sum of corresponding entries in the two lists.
#
# Examples:
#   * list1:  [1, 2, 3, 4]
#     list2:  [4, 5, 6, 7]
#     result: [5, 7, 9, 11]
#   * list1:  [100, 200, 300]
#     list2:  [ 10,   1, 180]
#     result: [110, 201, 480]
#
# Look up the zip function to help you with this problem.

def pairwise_add(list1, list2):
    # Create new list to store sum of each corresponding element
    summed_list = []
    # Zip the two lists so that they become tuples within a list
    new_list = list(zip(list1, list2))
    # Loop through the zipped list
    for item in new_list:
        # Sum the value at the zero index and first index within the tuple
        sum = item[0]+item[1]
        # Add the sum value into the created list
        summed_list.append(sum)
    print(summed_list)

# # Test Case:
# pairwise_add([1, 2, 3, 4], [4, 5, 6, 7])
# pairwise_add([100, 200, 300],[ 10,   1, 180])
