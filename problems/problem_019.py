# Complete the is_inside_bounds function which has the
# following parameters:
#   x: the x coordinate to check
#   y: the y coordinate to check
#   rect_x: The left of the rectangle
#   rect_y: The bottom of the rectangle
#   rect_width: The width of the rectangle
#   rect_height: The height of the rectangle
#
# The is_inside_bounds function returns true if all of
# the following are true
#   * x is greater than or equal to rect_x
#   * y is greater than or equal to rect_y
#   * x is less than or equal to rect_x + rect_width
#   * y is less than or equal to rect_y + rect_height

def is_inside_bounds(x, y, rect_x, rect_y, rect_width, rect_height):
    # Create variables for ease of reference
    width = rect_x + rect_width
    height = rect_y + rect_height
    # Set up condition statement that all four are met
    if x >= rect_x and y >= rect_y and x <= width and y <= height:
        # return True
        print("is inside bounds")

    else:
        # return False
        print("is outside bounds")

# Test Cases
# is_inside_bounds(x=10,
#                  y=20,
#                  rect_x=2,
#                  rect_y=8,
#                  rect_width=13,
#                  rect_height=20)

# is_inside_bounds(x=10,
#                  y=20,
#                  rect_x=21,
#                  rect_y=8,
#                  rect_width=13,
#                  rect_height=20)
