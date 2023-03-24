# Complete the can_make_pasta function to
# * Return true if the ingredients list contains
#   "flour", "eggs", and "oil"
# * Otherwise, return false
#
# The ingredients list will always contain three items.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def can_make_pasta(ingredients):
    completed_list = []
    for item in ingredients:
        if item == "flour" or item == "eggs" or item == "oil":
            completed_list.append(item)
    if len(completed_list) == 3:
        print("You can make pasta!")
    else:
        print("You do not have all of the ingredients to make pasta.")

# Test Cases:
# can_make_pasta(ingredients=["oil", "flour"])
# can_make_pasta(ingredients=["oil", "eggs", "flour"])
# can_make_pasta(ingredients=["water", "eggs", "flour"])
# can_make_pasta(ingredients=["rosemary", "oil", "eggs", "sugar", "flour"])
# can_make_pasta(ingredients=["rosemary", "oil", "eggs", "sugar"])
