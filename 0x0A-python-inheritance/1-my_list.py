#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """MyList class - inherits from lists"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
