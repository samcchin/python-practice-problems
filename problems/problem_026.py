# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average

def calculate_grade(values):
    sum = 0
    for scores in values:
        sum += scores
    average = sum / len(values)

    if average >= 90:
        print("A")
    elif average < 90 and average >= 80:
        print("B")
    elif average < 80 and average >= 70:
        print("C")
    elif average < 70 and average >= 60:
        print("D")
    else:
        print("F")

# #Test Cases
# calculate_grade([80, 80, 80])
# calculate_grade([60, 30, 90, 80,100])
# calculate_grade([90,80,100])
# calculate_grade([70, 65, 45, 55])
