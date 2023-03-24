# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(is_workday, is_sunny):
    # Create empty list to store gear for the day
    gear = []
    if is_sunny == "Y" and is_workday == "Y":
        gear.append("umbrella")
        gear.append("laptop")
    elif is_workday == "Y":
        gear.append("laptop")
    elif is_sunny == "Y" and is_workday == "N":
        gear.append("surfboard")
    else:
        print("No gear is needed for today!")

    print(gear)

# Test Cases:
# gear_for_day(is_workday = "Y", is_sunny = "N")
# gear_for_day(is_workday = "N", is_sunny = "N")
# gear_for_day(is_workday = "Y", is_sunny = "Y")
# gear_for_day(is_workday = "N", is_sunny = "Y")
