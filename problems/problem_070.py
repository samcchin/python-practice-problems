# Write a class that meets these requirements.
#
# Name:       Book
#
# Required state:
#    * author name, a string
#    * title, a string
#
# Behavior:
#    * get_author: should return "Author: «author name»"
#    * get_title:  should return "Title: «title»"
#
# Example:
#    book = Book("Natalie Zina Walschots", "Hench")
#
#    print(book.get_author())  # prints "Author: Natalie Zina Walschots"
#    print(book.get_title())   # prints "Title: Hench"
#
# Do it without pseudocode, this time, from memory. Don't look
# at the last one you just wrote unless you really must.

class Book:
    def __init__(book, author, title):
        book.author = author
        book.title = title

    def get_author(book):
        return "Author: " + book.author

    def get_title(book):
        return "Title: " + book.title


book = Book("Natalie Zina Walschots", "Hench")

print(book.get_author())  # prints "Author: Natalie Zina Walschots"
print(book.get_title())   # prints "Title: Hench"
