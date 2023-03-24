# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

def has_quorum(attendees_list, members_list):
    # Define condition if quorum has been met
    if attendees_list > (members_list * .5):
        print("Quorum has been met.")
    # Defoine condition if quorum has not been met
    else:
        print("Quorum has not been met based on the number of attendees.")

# # Test Cases
# has_quorum(24, 100)
# has_quorum(4, 10)
# has_quorum(5, 20)
# has_quorum(240, 300)
