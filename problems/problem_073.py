# Write a class that meets these requirements.
#
# Name:       Student
#
# Required state:
#    * name, a string
#
# Behavior:
#    * add_score(score)   # Adds a score to their list of scores
#    * get_average()      # Gets the average of the student's scores
#
# Example:
#    student = Student("Malik")
#
#    print(student.get_average())    # Prints None
#    student.add_score(80)
#    print(student.get_average())    # Prints 80
#    student.add_score(90)
#    student.add_score(82)
#    print(student.get_average())    # Prints 84
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

class Student:
    def __init__(student, name):
        student.name = name
        student.scores = []

    def add_score(student, score):
        student.scores.append(score)

    def get_average(student):
        if student.scores == []:
            return None
        else:
            sum_of_grades = 0
            count = len(student.scores)
            for grade in student.scores:
                sum_of_grades += grade
            average = sum_of_grades / count
            return int(average)


# Test Example:
student = Student("Malik")

print(student.get_average())    # Prints None
student.add_score(80)
print(student.get_average())    # Prints 80
student.add_score(90)
student.add_score(82)
print(student.get_average())    # Prints 84
