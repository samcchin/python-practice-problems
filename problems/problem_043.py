# Complete the find_indexes function which accepts two
# parameters, a list and a search term. It returns a new
# list that contains the indexes of the search term in
# the search list.
#
# Remember that indexes in Python are zero-based. That
# means the first element in the list is index 0.
#
# Examples:
#   * search_list:  [1, 2, 3, 4, 5]
#     search_term:  4
#     result:       [3]
#   * search_list:  [1, 2, 3, 4, 5]
#     search_term:  6
#     result:       []
#   * search_list:  [1, 2, 1, 2, 1]
#     search_term:  1
#     result:       [0, 2, 4]
#
# Look up the enumerate function to help you with this problem.

def find_indexes(search_list, search_term):
    result = []
    for index, item in enumerate(search_list):
        if item == search_term:
            result.append(index)
    return result


# Test Case:
print(find_indexes([1, 2, 3, 4, 5], 4))
print(find_indexes([1, 2, 3, 4, 5], 6))
print(find_indexes([1, 2, 1, 2, 1], 1))
