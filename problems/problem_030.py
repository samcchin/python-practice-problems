# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def find_second_largest(values):
    if values == []:
        print("None")
    elif len(values) == 1:
        print("None")
    else:
        sorted_list = sorted(values)
        second_largest_index = len(sorted_list)-2
        second_largest_num = sorted_list[second_largest_index]
        print(second_largest_num)

# Test Cases:
# find_second_largest([1])
# find_second_largest([1,2,4,5,6,4])
# find_second_largest([1,2,4,5,6,4,3,2])
# find_second_largest([])
# find_second_largest([3,2,1,4])
