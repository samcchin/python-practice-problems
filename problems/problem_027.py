# Complete the max_in_list function to find the
# maximum value in a list
#
# If the list is empty, then return None.
#

def max_in_list(values):
    if values == []:
        return None
    else:
        print(max(values))

# Test Cases
max_in_list([22, 24, 26, 900])
max_in_list([0])
max_in_list([1.4, 5, 601])
