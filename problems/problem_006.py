# Complete the can_skydive function so that determines if
# someone can go skydiving based on these criteria
#
# * The person must be greater than or equal to 18 years old, or
# * The person must have a signed consent form

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def can_skydive(age, has_consent_form):
    # * The person must be greater than or equal to 18 years old, or
    # * The person must have a signed consent form
    if age >= 18 or has_consent_form is True:
        print("You can go skydiving!")
    else:
        print("You cannot go skydiving.")

# Test case:
# can_skydive(17,False)
# can_skydive(18,False)
# can_skydive(40,True)
# can_skydive(12,True)
