#!usr/bin/python3
"""contains a function that writes a text files"""


def write_file(filename="", text=""):
    """ writes a string to a text file(UTF8) and returns
    the number of characters written."""
    with open(filename, 'w') as f:
        return f.write(text)
