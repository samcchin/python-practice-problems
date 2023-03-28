# Complete the add_csv_lines function which accepts a list
# as its only parameter. Each item in the list is a
# comma-separated string of numbers. The function should
# return a new list with each entry being the corresponding
# sum of the numbers in the comma-separated string.
#
# These kinds of strings are called CSV strings, or comma-
# sepearted values strings.
#
# Examples:
#   * input:  []
#     output: []
#   * input:  ["3", "1,9"]
#     output: [3, 10]
#   * input:  ["8,1,7", "10,10,10", "1,2,3"]
#     output:  [16, 30, 6]
#
# Look up the string split function to find out how to
# split a string into pieces.

# Write out your own pseudocode to help guide you.

def add_csv_lines(csv_lines):
    output = []
    for string in csv_lines:
        if "," in string:
            string_list = (string.split(","))
            num_list = [int(i) for i in string_list]
            sum_of_num_list = sum(num_list)
            output.append(sum_of_num_list)
        else:
            output.append(int(string))
    print(output)


# Test Cases:
print(add_csv_lines([]))
print(add_csv_lines(["3", "1,9"]))
print(add_csv_lines(["8,1,7", "10,10,10", "1,2,3"]))
