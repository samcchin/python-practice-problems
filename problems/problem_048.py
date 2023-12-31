# Write a function that meets these requirements.
#
# Name:       count_word_frequencies
# Parameters: sentence, a string
# Returns:    a dictionary whose keys are the words in the
#             sentence and their values are the number of
#             times that word has appeared in the sentence
#
# The sentence will contain now punctuation.
#
# This is "case sensitive". That means the word "Table" and "table"
# are considered different words.
#
# Examples:
#    * sentence: "I came I saw I learned"
#      result:   {"I": 3, "came": 1, "saw": 1, "learned": 1}
#    * sentence: "Hello Hello Hello"
#      result:   {"Hello": 3}

# FUNCTION PSEUDOCODE
# function count_word_frequencies(sentence):
def count_word_frequencies(sentence):
    # words = split the sentence
    words = sentence.split(" ")
    # counts = new empty dictionary
    counts = {}
    # for each word in words
    for word in words:
        # if the word is not in counts
        if word not in counts:
            counts[word] = 0
            # counts[word] = 0
        if word in counts:
            # add one to counts[word]
            counts[word] += 1
    # return counts
    return counts


# Test Cases:
print(count_word_frequencies("I came I saw I learned"))
print(count_word_frequencies("Hello Hello Hello"))
