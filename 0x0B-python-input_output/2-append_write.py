#!/usr/bin/python3
""" contains a function that appends a text file."""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8)
    and returns the number of characters"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(test)
