# Complete the is_inside_bounds function which takes an x
# coordinate and a y coordinate, and then tests each to
# make sure they're between 0 and 10, inclusive.

def is_inside_bounds(x, y):
    # Ensure x and y coordinate are both within 0 and 10
    if x >= 0 and x <= 10 and y >= 0 and y <= 10:
        # return x, y is True
        print("Is within bounds")
    else:
        # return x, y is False
        print("Is outside bounds")

# Test Cases
# is_inside_bounds(2,3)
# is_inside_bounds(21,3)
# is_inside_bounds(0,10)
