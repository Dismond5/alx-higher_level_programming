#!/usr/bin/python3
"""read_file module. contains a function that reads file"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, 'r') as f:
        print(f.read(), end='')
